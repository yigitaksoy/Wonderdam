<h2 align="center">
 Wonderdam Application Testing
</h2>

<div align="center">


<br><br>

[You can view the live project here](https://wonderdam.herokuapp.com/homepage)

</div>
<br>

Please refer to seperate [README.md](https://github.com/yigitaksoy/Wonderdam/blob/master/README.md) file for more information about the project.

<br>

## Contents Table

1. [**Testing User Stories from UX Design Section**](#user-stories)
    - [**First Time Visitor Goals**](#first-time-visitor-goals)
    - [**Registered Visitor Goals**](#registered-visitor-goals)
    - [**Admin User Goals**](#admin-user-goals)

2. [**Testing**](#testing)
    - [**W3C Markup Validator Results**](#html-validator-results)
    - [**W3C CSS Validator Results**](#html-validator-results)
    - [**JSHint Results**](#jshint-results)
    - [**PEP8 Online Validator Results**](#pep8-validator-results)
    - [**Debugging**](#debugging)

3. [**Further Manual Testing**](#further-manual-testing)





### Testing User Stories from UX Design Section

#### First Time Visitor Goals

* **I want to understand the main purpose of the website.**
    - When users enter the website a jumbotron text is presented for the visitors, which clearly states the main purpose of the website.
* **I want to easily navigate through the website.**
    - At the top of the page a sticky navigation bar is present, displaying all the links for new users to easily navigate through the website.
* **I want to find out how I can register to the website, and upload a post.**
    - On the navigation bar, right next to the Home link, Register link is presented for new users which leads them to the registration page. 
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/register.gif" width="700">
  </div>
  <br>
  
* **I want to find out how I can search for posts.**
    - On the navigation bar, at the right end side, there is a search bar present for users to easily search for posts.
 
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/search.gif" width="700">
  </div>
  <br>
  
* **I want to be able to find out how I contact the blog owner.**
    - On the navigation bar next to Login link, Contact link is present which takes users to the Contact form where users can easily contact the Blog Admin.

  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/contact.gif" width="700">
  </div>
  <br>


#### Registered Visitor Goals

* **I want to find out how I can login to my profile.**
    - On the navigation bar, right next to Register tab, Login link is presented for registered users, which takes them to Login page.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/login-to-site.gif" width="700">
  </div>
  <br>
  
* **I want to find out how I can add a new post.**
    - For registered users, Add new post link is presented on their profile page, as well on the Navigation bar.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/user-add-post.gif" width="700">
  </div>
  <br>
  
* **I want to find out how I can edit my posts.**
    - For post authors, Edit post links are present on their Profile page, on Homepage on top of their posts, as well as Blog post page.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/user-edit-post.gif" width="700">
  </div>
  <br>
  
* **I want to find out how I can delete my posts.**
    - For post authors, Delete post links are present on their Profile page, on Homepage on top of their posts, as well as Blog post page.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/user-delete-post.gif" width="700">
  </div>
  <br>
    
* **I want to find be able to see all my posts.**
    - On Registered user's Profile page, a section that shows users all the posts is present which makes it easy for users to easily see and manage their posts.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/profile.gif" width="700">
  </div>
  <br>
  
* **I want to find out how i can search through all the current posts, and categories.**
    - On the navigation bar, there is a search bar present, which lets users to easily search for current posts, and categories.
    
    <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/search-post--and-categories.gif" width="700">
  </div>
  <br>
  
* **I want to find out how to delete my blog account.**
    - On Registered users Profile page, at the bottom a Delete Account button is present for registered users to easily delete their account.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/user-delete-account.gif" width="700">
  </div>
  <br>

#### Admin User Goals

* **I want to be able to add new posts.**
    - On the Admin user Profile page and on Admin Dashboard a Add new post button, and on the navigation bar a New Post link is present, which helps Admin user to easily add new posts to the blog.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/admin-add-post.gif" width="700">
  </div>
  <br>
  
* **I want to be able to edit user posts.**
    - Admin user has exclusive rights therefore on Admin Dashboard and on top of every post an Edit button is present for Admin user to easily edit user posts.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/admin-edit-user-post.gif" width="700">
  </div>
  <br>
  
* **I want to be able to delete user posts.**
    - Admin user has exclusive rights therefore on Admin Dashboard and on top of every post a Delete button is present for Admin user to easily delete user posts.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/admin-delete-user-post.gif" width="700">
  </div>
  <br>
  
* **I want to be able to delete unwanted users from the blog.**
    - Admin user has exclusive rights therefore on Admin Dashboard a responsive registered users table is present, allowing admin user to delete unwanted users from the blog.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/admin-delete-user.gif" width="700">
  </div>
  <br>
  
* **I want to be able to manage add/edit/delete categories.**
    - On Admin dashboard there is a section listing all the current categories for Admin user, allowing Admin to easily Add/Edit/Delete catagories.
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/user-testing-videos/admin-manage-catagories.gif" width="700">
  </div>
  <br>
  
* **I want to be able to see real-time information about the blog, such as current number of posts, users, and categories**
    - On Admin dashboard, on top of the page, info cards are present allowing admin user to see real-time information of Blog post category and user data.
    
  <div align="center">
    <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/dashboard-info-cards.png">
  </div>
  <br>
### Testing

- The W3C Markup Validator and W3C CSS Validator Services were used to validate the HTML & CSS code in the project to ensure there were no syntax errors. JSHint was used to check the quality of the Javascript and PEP8 Online was used for checking the python code.

<details><summary><b>Click here for HTML Validator results</b></summary>

- __Homepage__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/homepage-validator-result.png" >
</p>

- __Login__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/login-validator-result.png" >
</p>

- __Register__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/register-validator-result.png" >
</p>

- __Contact__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/contact-validator-result.png" >
</p>

- __Profile__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/profile-validator-results.png" >
</p>

- __Add Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/add-post-validator-result.png" >
</p>

- Preview image is added dynamically with javascript, therefore issue was ignored.
<br>

- __Edit Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/edit-post-validator-result.png" >
</p>

- Preview image is added dynamically with javascript, therefore issue was ignored.
<br>

- __Blog Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/blog-post-validator-results.png" >
</p>

- __Admin Dashboard__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/dashboard-validator-result.png" >
</p>

- __Add Category__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/add-category-validator-results.png" >
</p>

- __Edit Category__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/edit-category-validator-results.png" >
</p>

- __Error 404__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/error-404-validator-result.png" >
</p>

- __Error 500__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/error-500-validator-result.png" >
</p>

</details>

<details><summary><b>Click here for CSS Validator results</b></summary>

- __CSS Validator Results__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/css-validator-results/css-validator-results.png" >
</p>
</details>

<details><summary><b>Click here for JSHint results</b></summary>

- __JSHint Results__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/jshint-results/jshint-results.png" >
</p>
</details>

<details><summary><b>PEP8 Online results</b></summary>

- __PEP8 Online Results__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/pep8-results/pep8-compliance.png" >
</p>
</details>

### Debugging

- During the early development stages of the project, Images that are requested from Cloudinary were highlighted in the console as `Mixed Content` on Homepage, as well as on Blog Post page. This issue was caused by Cloudinary images being served on an insecure HTTP connection. In order to fix this issue 
```console
<meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests"> 
```
meta tag was added into the base template, and issue was resolved. [Please see commit](https://github.com/yigitaksoy/Wonderdam/commit/c04907a47d7e6d2b60b26887046aa0ac16337b3f#diff-690b81fad8df2a1f1ce37c846641d9247e3472d244f17039d2910a5ed0c98d5e). For more information about what mixed content is, please refer to [Web.dev](https://web.dev/what-is-mixed-content/)

- During the testing stages of the project, Flask wasn't handling the 404 and 500 errors correctly, resulting in `key error: user` error. This issue was caused by Flask itself, and was also related to the if statement checking if user was in session. To resolve this issue, if statement was updated to:
```console
if session.get('user') is None:
```
### Further Manual Testing

#### Responsive Design - PASS

- All pages were tested locally, and on Heroku using Chrome, Firefox, IE, and Safari. 
- All pages tested for responsiveness in different device sizes using Google Chrome Developer Tools, and Google Chrome Responsive Viewer extension;
  - Desktop 
  - iPhone 5/6/7/8/X 
  - iPad 1/2/3/Pro 
  - Galaxy Android phones
- All the pages were also tested manually using;
  - iPhone 5s/6s/8/X/XS/11/
  - Samsung Galaxy S8/Note 10+
  - iPad Air 2 
  - iPad Pro 3
  
#### Functionality Testing
  
  #### Navbar - PASS
  
  - All links are working, and takes the user where they want to go.
  - Search bar is working, and lets user search through posts, users, and categories. If user input doesnt match any results, "No results found" message is shown"
  - Search results pagination works perfectly, and gives feedback depending on the search results. 
  
  #### Homepage - PASS
  
  - All posts and transitions work as expected.
  - All post images, titles, and read more links work as expected and takes the user to the post page.
  - All edit, and delete buttons on top of posts work as expected, enables post author or admin user to edit and delete posts.
  - Edit and Delete buttons are hidden if user isnt the author of the post or the admin user.
  - Pagination works as expected, and only shows 5 posts per page. 
  
  #### Register - PASS
  
  - Form inputs work as expected and stores the data in the database.
  - Form validations work as expected, and gives feedback upon unmatched format or existing username.
  - Password match validator works as expected and gives real-time information about matching data. 
  - Submit button works as expected and submits data successfully, and redirects new user to their profile page.
  
  #### Login - PASS
  
  - Form inputs works perfectly, and form validations work as expected and gives feedback upon unmatched format or incorrect username and password, or if user doesnt exist in the database.
  - Submit button works as expected and submits data successfully, and redirects user to their profile page upon successful entry.
  
  #### Logout - PASS
  
  - Logout functionality works perfectly, logs out user, and removes session cookies.
  
  #### Profile - PASS
  
  - All posts by the current user are displayed in post cards, and all post images fit perfectly inside the cards.
  - Add post button works as expected and redirects user to Add Post form.
  - If current user doesn't have any posts, "Would you like to add a post" text along with Add post button is shown.
  - All the edit delete buttons on post cards work perfectly and allows user to easily manage their posts. 
  - Delete User account button works as expected and deletes user from the database, logs out user, and removes them from the session cookies.
  
  #### Add Post - PASS
  
  - All form inputs work perfectly, and stores the required data into the database.
  - Character count function works perfectly, and gives real-time feed back upon typing in the text area, allowing users to match the requested charachter count for posts.
  - Post image preview section on the form works perfectly, and shows user their image before upload. Preview image function on the form is responsive and all images fit perfectly on all devices sizes.
  - File upload input on the form works as expected, restircts user to choose only allowed image extenstions, and uploads image to Cloudinary upon successful submission. 
  - Add post button works perfectly and submits data upon successfull submission.
  - Form validates if current Post title already exists. 
  
  #### Edit Post - PASS
  
  - All form inputs work perfectly, and updates the required data in the database.
  - All input fields are pre-filled with the information from the add post form, allowing users to easily edit their content.
  - Character count function works perfectly, and gives real-time feed back upon typing in the text area, allowing users to match the requested charachter count for posts.
  - Post image preview section on the form works perfectly, and shows user their image before upload. Preview image function on the form is responsive and all images fit perfectly on all devices sizes.
  - File upload input on the form works as expected, restircts user to choose only allowed image extenstions, and uploads image to Cloudinary upon successful submission. 
  - Add post button works perfectly and submits data upon successfull submission.
  - Form validates if current Post title already exists. 
  
  #### Post Page - PASS
  
  - Successfully renders all the data including the post image. 
  - Edit and Delete button on top of the post for the post author, and admin user works perfectly and allows them to delete or edit the data. 
  - Post website data renders perfectly as an external link underneath the post content, and opens the page in a new tab.
  
  #### Admin Dashboard - PASS
  
  - All post info cards show real-time data, and work as exptected.
  - Registered users table works as expected listing all the users and their data.
  - Delete user button on the Registered user table works as expected and deletes the user upon confirmation.
  - Categories section works as expected, and shows all the current categories along with their Edit and Delete buttons for Admin user to easily manage.
  - Edit Category button works as expected and redirects Admin user to Edit Category Form. 
  - Delete Category button works as expected and deletes the category upon confirmation.
  - Add category button works as expected and redirects Admin user to add category form. 
  - Recent Posts section works as expected and shows all the current posts on the blog, along with their post images, and Edit - Delete buttons. 
  - Edit buttons on recent posts cards works perfectly and allows admin user to edit any post they want.
  - Delete button on recent posts cards works perfectly and allows admin user to delete any post upon confirmation.
  - Add post button on Dashboard works perfectly and redirects admin user to Add post form to add new posts. 
  
  #### Add Category - PASS
  
  - All form inputs work perfectly, and gives feedback upon successful submission.
  - Form gives feedback if matching category already exists. 
  - Add Category button works as expected, and submits data upon successful submission. 
  
  #### Edit Category - PASS 
  
  - Form successfully requests current category data from database. 
  - All form inputs work perfectly, and gives feedback upon successful submission.
  - Form gives feedback if matching category already exists. 
  - Add Category button works as expected, and submits data upon successful submission. 
  
  #### Contact - PASS
  
  - All inputs work as expected and validates user information before submission. 
  - Send button works as expected and submits data as expected.
  - Form is fully functional and sends email to the Admin user upon successfull submission.
  
  #### Footer - PASS
  
  - Footer is present on all pages. 
  - Social links on the footer works as expected, and all the links open in a new tab. 
  
  #### Error 404 - PASS
  
  - Works as expected, successfuly captures and handles page not found error.
  - Go back button on error page works as expected and redirects user back to the homepage.
  
  #### Error 500 - PASS
  
  - Works as expected, successfuly captures and handles internal server error.
  - Go back button on error page works as expected and redirects user back to the homepage.
  
  
  ### Security Testing
  
  - Tested restrictions against users adding a post without signing in -  **Restricted Access / PASS**
  - Tested restrictions against users editing a post without signing in -  **Restricted Access / PASS**
  - Tested restrictions against users seeing other users Profiles without signing-in - **Restricted Access / PASS**
  - Tested restrictions against users seeing other users Profiles when signed-in - **Restricted Access / PASS**
  - Tested restrictions against users deleting other users' accounts - **Restricted Access / PASS**
  - Tested restrictions against users trying to delete Admin user - **Restricted Access / PASS**
  - Tested restrictions against users trying to add a Category - **Restricted Access / PASS**
  - Tested restrictions against users trying to edit a Category - **Restricted Access / PASS**
  - Tested restrictions against users trying to delete a Category - **Restricted Access / PASS**
  - Tested restrictions against users trying to access Admin Dashboard - **Restricted Access / PASS**
  
  #### Google Lighthouse Testing 
  
  - All pages were tested for web quality using Google's Lighthouse.
  
  <details><summary><b>Click here for Lighthouse results</b></summary>
  
  - __Homepage__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/homepage-lighthouse.png" >
</p>

  - __Register__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/register-lighthouse.png" >
</p>
  
  - __Login__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/login-lighthouse.png" >
</p>

  - __Contact__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/contact-lighthouse.png" >
</p>

  - __Profile__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/profile-lighthouse.png" >
</p>

  - __Add Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/add-post-lighthouse.png" >
</p>

  - __Edit Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/edit-post-lighthouse.png" >
</p>

  - __Blog Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/blog-post-lighthouse.png" >
</p>

  - __Admin Dashboard__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/dashboard-lighthouse.png" >
</p>

  - __Add Category__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/add-category-lighthouse.png" >
</p>

  - __Edit Category__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/lighthouse-scores/edit-category-lighthouse.png" >
</p>

  </details>