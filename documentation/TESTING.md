<h2 align="center">
 Wonderdam Application Testing
</h2>

<div align="center">


<br><br>

[You can view the live project here](https://wonderdam.herokuapp.com/homepage)

</div>


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

3. [**Further Manual Testing**](#further-manual-testing)





### Testing User Stories from UX Design Section

#### First Time Visitor Goals

* I want to understand the main purpose of the website.
    - When users enter the website a jumbotron text is presented for the visitors, which clearly states the main purpose of the website.
* I want to easily navigate through the website.
    - At the top of the page a sticky navigation bar is present, displaying all the links for new users to easily navigate through the website.
* I want to find out how I can register to the website, and upload a post.
    - On the navigation bar, right next to the Home link, Register link is presented for new users which leads them to the registration page. 
* I want to find out how I can search for posts.
    - On the navigation bar, at the right end side, there is a search bar present for users to easily search for posts.
* I want to be able to find out how I contact the blog owner.
    - On the navigation bar next to Login link, Contact link is present which takes users to the Contact form where users can easily contact the Blog Admin.



#### Registered Visitor Goals

* I want to find out how I can login to my profile.
    - On the navigation bar, right next to Register tab, Login link is presented for registered users, which takes them to Login page.
* I want to find out how I can add a new post.
    - For registered users, Add new post link is presented on their profile page, as well on the Navigation bar.
* I want to find out how I can edit my posts.
    - For post authors, Edit post links are present on their Profile page, on Homepage on top of their posts, as well as Blog post page.
* I want to find out how I can delete my posts.
    - For post authors, Delete post links are present on their Profile page, on Homepage on top of their posts, as well as Blog post page.
* I want to find be able to see all my posts.
    - On Registered user's Profile page, a section that shows users all the posts is present which makes it easy for users to easily see and manage their posts.
* I want to find out how i can search through all the current posts, and categories.
    - On the navigation bar, there is a search bar present, which lets users to easily search for current posts, and categories.
* I want to find out how to delete my blog account.
    - On Registered users Profile page, at the bottom a Delete Account button is present for registered users to easily delete their account.

#### Admin User Goals

* I want to be able to add new posts.
    - On the Admin user Profile page and on Admin Dashboard a Add new post button, and on the navigation bar a New Post link is present, which helps Admin user to easily add new posts to the blog.
* I want to be able to edit user posts.
    - Admin user has exclusive rights therefore on Admin Dashboard and on top of every post an Edit button is present for Admin user to easily edit user posts.
* I want to be able to delete user posts.
    - Admin user has exclusive rights therefore on Admin Dashboard and on top of every post a Delete button is present for Admin user to easily delete user posts.
* I want to be able to delete unwanted users from the blog.
    - Admin user has exclusive rights therefore on Admin Dashboard a responsive registered users table is present, allowing admin user to delete unwanted users from the blog.
* I want to be able to manage add/edit/delete categories.
    - On Admin dashboard there is a section listing all the current categories for Admin user, allowing Admin to easily Add/Edit/Delete catagories.
* I want to find out how many posts are currently on the blog.
    - On Admin dashboard, on top of the page info cards are present allowing admin user to see real-time information of Blog post data.
* I want to find out how many categories are currently on the blog.
    - On Admin dashboard, on top of the page info cards are present allowing admin user to see real-time information of Blog category data.
* I want to find out how many users are currently registered on the blog.
    - On Admin dashboard, right underneath blog info cards, a responsive registered users table is present allowing Admin user to get detailed information about all the registered users on the blog.

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

- __Blog Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/blog-post-validator-results.png" >
</p>

- __Edit Post__
<p align="center">
  <img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/html-validator-results/edit-post-validator-result.png" >
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

### Further Manual Testing