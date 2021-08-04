import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


# -- Admin User --- #
def admin_user():

    return session['user'] == 'admin'


# -- Homepage --- #
@app.route("/")
@app.route("/homepage")
def homepage():

    posts = list(mongo.db.posts.find())

    return render_template(
        "index.html", posts=posts)


# -- Blog Post -- #
@app.route("/blog_post/<post_id>", methods=["GET", "POST"])
def blog_post(post_id):

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    return render_template("blog_post.html", post=post)


# -- Search Posts --- #
@app.route("/search", methods=["GET", "POST"])
def search():

    query = request.form.get("query")
    posts = list(mongo.db.posts.find({"$text": {"$search": query}}))

    return render_template("index.html", posts=posts)


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
                "password": generate_password_hash(request.form.get("password"))
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
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# -- User Profile --- #
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if session["user"] == username:
        # Grab the session user's username from db
        username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    else:
        flash('You are not authorized to perform this operation')
        return redirect(url_for("homepage"))   
        # Return profile page with user's unique name   
    return render_template("profile.html", username=username)


# -- Delete Account --- #
@app.route("/delete_account/<username>")
def delete_account(username):

    if session.get("user"):
        mongo.db.users.remove({"username": username})
        flash("User Successfully Deleted")
        session.pop("user")
        return redirect(url_for("homepage"))
    else:
        flash("You are not authorized to perform this operation")
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

    if session.get("user"):
        if request.method == "POST":
            post = {
                "post_title": request.form.get("post_title"),
                "post_category": request.form.get("post_category"),
                "post_content": request.form.get("post_content"),
                "post_image": request.form.get("post_image"),
                "post_date": datetime.today().strftime("%d %B, %Y"),
                "author": session["user"]
            }
            mongo.db.posts.insert_one(post)
            flash("You've successfully posted!")
            return redirect(url_for("homepage"))

        categories = mongo.db.categories.find().sort("post_category", 1)
        return render_template("add_post.html", categories=categories)
    else:
        flash("Please sign in to Post")
        return redirect(url_for("login"))


# -- Edit Post --- #
@app.route("/edit_post/<post_id>", methods=["GET", "POST"])
def edit_post(post_id):

    if request.method == "POST":
        submit = {
            "post_title": request.form.get("post_title"),
            "post_category": request.form.get("post_category"),
            "post_content": request.form.get("post_content"),
            "post_image": request.form.get("post_image"),
            "post_date": datetime.today().strftime("%d %B, %Y"),
            "author": session["user"].title()
        }
        mongo.db.posts.update({"_id": ObjectId(post_id)}, submit)
        flash("Post Successfully Updated")

    post = mongo.db.posts.find_one({"_id": ObjectId(post_id)})
    categories = mongo.db.categories.find().sort("post_category", 1)
    return render_template("edit_post.html", post=post, categories=categories)


# -- Delete Post --- #
@app.route("/delete_post/<post_id>")
def delete_post(post_id):

    mongo.db.posts.remove({"_id": ObjectId(post_id)})
    flash("Post Successfully Deleted")
    return redirect(url_for("homepage"))


# -- Categories --- #
@app.route("/get_categories")
def get_categories():

    if admin_user():
        categories = list(mongo.db.categories.find().sort("post_category", 1))
        
    else:
        flash('You are not authorized to perform this operation')
        return redirect(url_for("homepage"))
    
    return render_template("categories.html", categories=categories)


# -- Add Category --- #
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    #Allow admin user to add new categories
    if admin_user():
        if request.method == "POST":
            # Check if category already exists in db
            existing_category = mongo.db.categories.find_one(
            {"post_category": request.form.get("post_category")}
            )
            
            category = {
                "post_category": request.form.get("post_category")
            }
            if existing_category:
                flash("Category already exists")
                return render_template("add_category.html")
            else:
                mongo.db.categories.insert_one(category)
                flash("New Category Added")
                return redirect(url_for("dashboard"))
    else:
        flash('You are not authorized to perform this operation')
        return redirect(url_for("homepage"))

    return render_template("add_category.html")


# -- Delete Category --- #
@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    # Allow admin user to delete categories 
    if admin_user():
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category deleted")
     
    else:
        flash('You are not authorized to perform this operation')
        return redirect(url_for("homepage"))
    
    return redirect(url_for("dashboard"))


# -- Edit Category --- #
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # Allow admin user to edit categories
    if admin_user():
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

    if admin_user():
        categories = list(mongo.db.categories.find().sort("post_category", 1))
        total_categories = mongo.db.categories.count()
        users = list(mongo.db.users.find().sort("username", 1)) 
        total_users = mongo.db.users.count()
        posts = list(mongo.db.posts.find().sort("post", 1))
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

    if admin_user():
        mongo.db.users.remove({"_id": ObjectId(user_id)})
        flash("User Successfully Deleted")
    
    else:
        flash('You are not authorized to perform this operation')
        return redirect(url_for("homepage"))
    
    return redirect(url_for("dashboard"))


# -- Contact --- #
@app.route("/contact")
def contact():

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