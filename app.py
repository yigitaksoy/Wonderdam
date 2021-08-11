import os
import cloudinary.api
import cloudinary
import cloudinary.uploader
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for, jsonify)
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
from flask_paginate import Pagination, get_page_args
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


load_dotenv()


app = Flask(__name__)

CORS(app)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# -- Admin User --- #
ADMIN = 'admin'


# -- Cloudinary Settings -- #
cloudinary.config(
    cloud_name = os.getenv('CLOUD_NAME'), 
    api_key=os.getenv('API_KEY'), 
    api_secret=os.getenv('API_SECRET'))


# -- Flask Mail Settings -- # 
mail_settings = {
    "MAIL_SERVER": os.environ.get('MAIL_SERVER'),
    "MAIL_PORT": os.environ.get('MAIL_PORT'),
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": os.environ.get('MAIL_USE_SSL'),
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),
    "SECURITY_EMAIL_SENDER": os.environ.get("SECURITY_EMAIL_SENDER")
}


# -- Update application settings
app.config.update(mail_settings)

# -- Create instance of Flask Mail
mail =Mail(app)

mongo = PyMongo(app)


# -- Set Pagination for posts per page -- #
POSTS_PER_PAGE = 5


# -- Paginate Posts -- #
def paginate_posts(posts, per_page):
    page = int(request.args.get('page', 1))
    offset = (page - 1) * per_page
    return posts[offset: offset + per_page]


# -- Paginate Search Results -- #
def paginate_search(posts, per_page):
    page = int(request.args.get('page', 1))
    offset = (page - 1) * per_page
    return posts[offset: offset + per_page]


def paginate_args(posts, per_page):
    page = int(request.args.get('page', 1))
    total=len(posts)
    return Pagination(page=page, per_page=per_page, total=total)


# -- Homepage --- #
@app.route("/")
@app.route("/homepage")
def homepage():

    posts = list(mongo.db.posts.find().sort("post_date", 1))
    pagination_posts = paginate_posts(posts, POSTS_PER_PAGE)
    pagination = paginate_args(posts, POSTS_PER_PAGE)
    page_num = request.args.get('page', 1, type=int)

    return render_template(
        "index.html", posts=pagination_posts, 
                    pagination=pagination, page_num=page_num)


# -- Blog Post -- #
@app.route("/blog_post/<post_id>", methods=["GET"])
def blog_post(post_id):

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("blog_post.html", post=post)


# -- Search Posts --- #
@app.route("/search", methods=["GET", "POST"])
def search():

    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))

    total=len(posts)
    pagination_posts = paginate_posts(posts, POSTS_PER_PAGE)
    pagination = paginate_args(posts, POSTS_PER_PAGE)

    return render_template("index.html", posts=pagination_posts, 
                    pagination=pagination, total=total)


# -- User Register --- #
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        # Check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password == confirm_password:
            register = {
                "name": request.form.get("name").lower(),
                "last_name": request.form.get("last_name").lower(),
                "email": request.form.get("email").lower(),
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.form.get("password")),
                "registered": datetime.today().strftime("%d %b, %Y")
        }
            mongo.db.users.insert_one(register)

            # Put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash("Passwords do not match!", "error")
            return redirect(url_for("register"))
    return render_template("register.html")


# -- User Login --- #
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        # Check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Username doesn't exist")
            return redirect(url_for("login"))

    return render_template("login.html")


# -- User Profile --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in to see your Profile Page')
        return redirect(url_for("login"))
    else:
        if session["user"] == username:
            # Grab the session user's username from db
            username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
            # Get all the posts by current users 
            posts = list(mongo.db.posts.find(
                {"author": session["user"]}).sort("post_date", 1))
        else:
            flash('You cant see other users profile')
            return redirect(url_for("homepage"))   
        # Render user profile page
        return render_template("profile.html", username=username, posts=posts)


# -- Delete Account --- #
@app.route("/delete_account/<username>")
def delete_account(username):

    if session.get('user') == None:
        flash("You need to sign in to delete your account")
        return redirect(url_for("login"))
    else:
        if session["user"] == username:
            mongo.db.users.remove({"username": username})
            flash("User Successfully Deleted")
            session.pop("user")
            return redirect(url_for("homepage"))  
        else:
            flash("You can't delete other users accounts!")
            return redirect(url_for("homepage"))
    

# -- User Logout --- #
@app.route("/logout")
def logout():

    # Remove user from session cookie   
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("homepage"))


# -- Add Post --- #
@app.route("/add_post", methods=["GET", "POST"])
def add_post():

    if session.get('user') == None:
        flash("Please sign in to post")
        return redirect(url_for("login"))
    else:
        if request.method == "POST":
            # Check if post already exists in db
            existing_post = mongo.db.posts.find_one(
            {"post_title": request.form.get("post_title")}
            )
            app.logger.info('in upload route')
            cloudinary.config(
                cloud_name = os.getenv('CLOUD_NAME'), 
                api_key=os.getenv('API_KEY'), 
                api_secret=os.getenv('API_SECRET'))
            upload_result = None
            file_to_upload = request.files['post_image']
            app.logger.info('%s file_to_upload', file_to_upload)

            if file_to_upload:
                upload_result = cloudinary.uploader.upload(file_to_upload)
                app.logger.info(upload_result)

            post = {
                "post_title": request.form.get("post_title"),
                "post_category": request.form.get("post_category"),
                "post_content": request.form.get("post_content"),
                "post_image": upload_result["url"],
                "post_address": request.form.get("post_address"),
                "website": request.form.get("website"),
                "post_date": datetime.today().strftime("%d %B, %Y"),
                "author": session["user"]
            }
            if existing_post:
                flash("Post already exists")
                return render_template("add_post.html")
            mongo.db.posts.insert_one(post)
            flash("You've successfully posted!")
            return redirect(url_for("homepage"))

        categories = mongo.db.categories.find().sort("post_category", 1)
        return render_template("add_post.html", categories=categories)



# -- Edit Post --- #
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    if session.get('user') == None:
        flash("Please sign in to edit this post")
        return redirect(url_for("login"))
    else:
        if session.get('user') == 'author' or session.get('user') == ADMIN:
            if request.method == "POST":
                app.logger.info('in upload route')
                cloudinary.config(
                        cloud_name = os.getenv('CLOUD_NAME'), 
                        api_key=os.getenv('API_KEY'), 
                        api_secret=os.getenv('API_SECRET'))
                upload_result = None
                file_to_upload = request.files['post_image']
                app.logger.info('%s file_to_upload', file_to_upload)
                if file_to_upload:
                    upload_result = cloudinary.uploader.upload(file_to_upload)
                    app.logger.info(upload_result)

                submit = {
                    "post_title": request.form.get("post_title"),
                    "post_category": request.form.get("post_category"),
                    "post_content": request.form.get("post_content"),
                    "post_image": upload_result["url"],
                    "post_address": request.form.get("post_address"),
                    "website": request.form.get("website"),
                    "post_date": datetime.today().strftime("%d %B, %Y"),
                    "author": session["user"]
                }
                mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
                flash("Post Successfully Updated")
            post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
            categories = mongo.db.categories.find().sort("post_category", 1)
            return render_template("edit_post.html", post=post, categories=categories)
        else:
            flash('You cant edit other users Posts!')
            return redirect(url_for("homepage"))



# -- Delete Post --- #
@app.route("/delete_post/<post_id>")
def delete_post(post_id):
    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in to delete your post')
        return redirect(url_for("login"))
    else:
        if session.get('user') == 'author' or session.get('user') == ADMIN:
            mongo.db.posts.remove({"_id": ObjectId(post_id)})
            flash("Post Successfully Deleted")
            return redirect(url_for("homepage"))
        else:
            flash("You cant delete other users posts!")
            return redirect(url_for("homepage"))


# -- Add Category --- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:
        #Allow admin user to add new categories
        if session['user'] == ADMIN:
            if request.method == "POST":
                # Check if category already exists in db
                existing_category = mongo.db.categories.find_one(
                {"post_category": request.form.get("post_category")})
                category = {
                    "post_category": request.form.get("post_category")}
                if existing_category:
                    flash("Category already exists")
                    return render_template("add_category.html")
                else:
                    mongo.db.categories.insert_one(category)
                    flash("New Category Added")
                    return redirect(url_for("dashboard"))
            return render_template("add_category.html")
        else:
            flash('You are not authorized to perform this operation')
            return redirect(url_for("homepage"))


# -- Delete Category --- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:
        # Allow admin user to delete categories 
        if session['user'] == ADMIN:
            mongo.db.categories.remove({"_id": ObjectId(category_id)})
            flash("Category deleted")

        else:
            flash('You are not authorized to perform this operation')
            return redirect(url_for("homepage"))

        return redirect(url_for("dashboard"))


# -- Edit Category --- #
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:    
        # Allow admin user to edit categories
        if session['user'] == ADMIN:
            if request.method == "POST":
                submit = {
                    "post_category": request.form.get("post_category")
                }

                mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
                flash("Category Successfully Updated")
                return redirect(url_for("dashboard"))

            category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
            return render_template("edit_category.html", category=category)

        else:
            flash('You are not authorized to perform this operation')
            return redirect(url_for("homepage"))


# -- Admin Dashboard --- #
@app.route("/dashboard")
def dashboard(): 

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:
        if session['user'] == ADMIN:
            categories = list(mongo.db.categories.find().sort("post_category", 1))
            total_categories = mongo.db.categories.count()
            users = list(mongo.db.users.find().sort("username", 1)) 
            total_users = mongo.db.users.count()
            posts = list(mongo.db.posts.find().sort("post_date", -1))
            total_posts = mongo.db.posts.count()
        else:
            flash('You are not authorized to perform this operation')
            return redirect(url_for("homepage"))

        return render_template("dashboard.html", categories=categories, total_categories=total_categories, 
                                                    users=users, total_users=total_users, 
                                                        total_posts=total_posts, posts=posts)


# -- Delete Registered User -- #
@app.route("/delete_user/<user_id>")
def delete_user(user_id):

    # Check if user is signed in
    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:
        if session['user'] == ADMIN:
            mongo.db.users.remove({"_id": ObjectId(user_id)})
            flash("User Successfully Deleted")
        else:
            flash('You cant delete other users accounts!')
            return redirect(url_for("homepage"))

        return redirect(url_for("dashboard"))


# -- Delete User Post --- #
@app.route("/delete_user_post/<post_id>")
def delete_user_post(post_id):

    if session.get('user') == None:
        flash('Please sign in as Admin User to perform this action')
        return redirect(url_for("login"))
    else:
        if session['user'] == ADMIN:
            mongo.db.posts.remove({"_id": ObjectId(post_id)})
            flash("Post Successfully Deleted")
        else:
            flash('You cant delete other users posts!')
            return redirect(url_for("homepage"))

        return redirect(url_for("dashboard"))


# -- Contact --- #
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        with app.app_context():
            msg = Message(subject="New Email From Wonderdam Blog")
            msg.recipients = [os.environ.get("MAIL_USERNAME")]
            msg.sender = request.form.get("emailaddress")
            name = request.form.get("name")
            message = request.form.get("message")
            msg.body = (f"Name: {name} \n"
                        f"Email: {msg.sender} \n"
                        f"Message: {message} \n")
            mail.send(msg)
            flash("Your Message Sent Successfully!")
            return redirect(url_for("contact"))

    return render_template("contact.html")



##################
# Error Handlers #
##################

# -- 404 Error --- #
@app.errorhandler(404)
def page_not_found(e):
    """
    Renders a custom 404 error page 
    """
    return render_template("404.html"), 404


# -- 500 Error --- #
@app.errorhandler(500)
def server_not_found(e):
    """
    Renders a custom 500 error page 
    """
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)