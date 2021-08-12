<h2 align="center">
 Wonderdam City Guide for Amsterdam
</h2>

<h3 align="center">
<img src="https://github.com/yigitaksoy/Wonderdam/blob/master/static/images/wonderdam-responsive.png" alt="Wonderdam Preview">
</h3>


<div align="center">


<br><br>

[You can view the live project here](https://wonderdam.herokuapp.com/homepage)

</div>

# Wonderdam

## Overview

This is the main website for Wonderdam, a local guide for hidden gems, popular restaurants, cafes, terraces, and bars located in Amsterdam. The website aims to target tourists who are looking for suggestions, or locals who are looking for news places to discover in the great city of Amsterdam. The website's main focus is to inform people about what or where to eat, or make suggestions for people who just want hangout with their friends and family and wants to try somewhere new in the city.

The website is fully interactive, built with mobile-first design in mind, and accessible on a wide range of mobile devices, and tablets.


## Contents Table

1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Media**](#media)
    - [**Codes**](#codes)
    - [**Acknowledgements**](#acknowledgements)

7. [**Disclaimer**](#disclaimer)



## UX
- The Blog features a modern, interactive, and easy-to-use design for visitors to easily navigate and enjoy their time during their visit.

### User stories

#### First Time Visitor Goals

- I want to understand the main purpose of the website.
- I want to easily navigate through the website.
- I want to find out how I can register to the website, and upload a post.
- I want to find out how I can search for posts.
- I want to be able to find out how I contact the blog owner.


#### Registered Visitor Goals

- I want to find out how I can login to my profile.
- I want to find out how I can add a new post.
- I want to find out how I can edit my posts.
- I want to find out how I can delete my posts.
- I want to find be able to see all my posts.
- I want to find out how i can search through all the current posts, and categories.
- I want to find out how to delete my blog account.

#### Admin User Goals

- I want to be able to add new posts.
- I want to be able to edit user posts.
- I want to be able to delete user posts.
- I want to be able to delete unwanted users from the blog.
- I want to be able to manage add/edit/delete categories.
- I want to find out how many posts are currently on the blog.
- I want to find out how many categories are currently on the blog.
- I want to find out how many users are currently registered on the blog.


## Strategy

- The goal of the website is to inform local residents, tourists how are visiting, or looking to visit Amsterdam about all the new local cafes, restaurants and bars. The blog aims to attract more visitors by presenting up to date information about these places, aims create a community around the blog, and to be the go-to place as a local Amsterdam guide.

## Design


### Color Scheme

- The colors used throughout the website are:

<img src="https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/images/color-palette.png"  alt="color-palette">


### Typography

There are three Adobe fonts used throught the website. [P22 Pooper Black](https://fonts.adobe.com/fonts/p22-pooper-black) is used for logo, [Antique Olive Nord](https://fonts.adobe.com/fonts/antique-olive) used for all titles and post "Read More" links. [Paralucent](https://fonts.adobe.com/fonts/paralucent) was used on all the texts to give the website a modern and minimalistic feel.



### Imagery



### Wireframes

- [Homepage](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Homepage.png)
- [Blog Post Page](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Blog%20Post%20Page.png)
- [Register](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Register.png)
- [Login](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Login.png)
- [Contact](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Contact.png)
- [Profile Page for New User](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20New%20User.png)
- [Profile Page without Posts](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20user%20without%20posts.png)
- [Profile Page with Posts](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Profile%20with%20posts.png)
- [Admin Profile Page](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Admin%20Profile%20Page.png)
- [Add Post](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Add%20Post.png)
- [Edit Post](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Edit%20Post.png)
- [Add Category](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Add%20Category.png)
- [Edit Category](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Edit%20Category.png)
- [Admin Dashboard](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Admin%20Dashboard.png)
- [Error 404](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Error%20404.png)
- [Error 500](https://github.com/yigitaksoy/Wonderdam/blob/master/documentation/wireframes/Error%20500.png)


## Features

### Existing Features

- Responsive on all device sizes.
- Navbar and Footer is visible on all pages.

 **Homepage**
- Features an interactive, and modern design.
- Using Javascript animations, Post images, and Titles are seamlessly presented to the user in an orderly fashion as user scrolls through the page, providing a unique experience.
- Features Pagination to show only 5 posts per page for a clean UX.
- Each post on homepage displays Author, Post date, and Category information, and each Category color is given a unique color using Jquery.
- For post authors, a Delete and Edit button is displayed on their post for users to easily manage their posts from Homepage.
- For Admin user all the posts feature a Delete and Edit button, allowing Admin user to easily Edit or Delete Unwanted user posts directly from the Homepage.

 **Register Page**
- Features a clean registration for user to signup for the blog.
- Each section of form input area features a placeholder text.
- Underneath the form inputs, there is a placeholder text explaining the required data for input, helping users to easily match the requested format.

 **Login Page**
- Features a clean form for users to login to their blog.
- Each section of form input area features a placeholder text.
- Underneath the form inputs, there is a placeholder text explaining the required data for input, helping users to easily match the requested format.
- Upon succcessful submission, user is redirected to their own profile page.

 **Profile Page**
- Features a clean layout.
- Shows a greeting message to the User upon successful login.
- Features a section showing all the posts by the user, allowing them to edit or delete their posts.
- If user has no posts, then a message is presented to the user, asking them if they would like to add a new post.
- At the bottom of the page there is a "Delete Account" button featuring a modal for user confirmation.

 **Add Post Page**
- Stricted only for registered users.
- Page features a clean form for users to use, outlining all the required information in the form.
- Form features an image preview section allowing users to see their post images before uploading.
- Using file upload, and Cloudinary service, form allows users to easily upload their image to the cloud, and eliminates the hassle of looking for image urls.
- File upload function allows user to only upload image files such as jpeg, jpg, and png. Any other file extensions are restricted.
- After submission, form checks if the current Post title exits in the database, restricting users from adding duplicate posts.
- Upon successful post, user get redirected to the homepage and greeted with a success message.

**Edit Post Page**
- Stricted only for post authors.
- Page features the same form and features as the Add Post page.
- Each section of the form is pre-filled with the data they provided when they submited the form, allowing users to easily edit the post information.
- After submission, form checks if the current Post title exits in the database, restricting users from adding duplicate posts.
- Upon successful post, user get redirected to the homepage and greeted with a success message.

**Contact Page**
- Allowed for all visitors and users of the blog.
- Using Flask Mail, users are able to contact the Blog Admin via the form.
- Upon successfull submission users are greeted with a success message, and email is sent for Admin user to see.

**Admin Dashboard**
- Stricted for Admin use only, and features a variety options for the Admin user to easily manage and be in total control.
- On top of the page, info cards are presented for the admin user. Each card shows a real-time information about total number of users, total number of posts, and total number of categories.
- Underneath the blog info cards, a responsive table of registered user list is presented along with all the information users provided. Next to each user there is a call to action button for user deletion, allowing admin user to delete any unwanted users. Admin user deletion is restricted from the table.
- Underneath the Registered users table, All the categories are listed for Admin user to manage. Along with a Add Category button for Admin user to easily add new categories if needed.
- Underneath the Categories section, Recent posts section is presented to the Admin user showing all the current posts on the page showing their titles and images. Each post card features a Edit and Delete button, allowing Admin user to easily manage current posts on the blog.

**Add Category**
- Stricted for Admin use only.
- Page features a single line form allowing Admin user to add new categories.
- After submission Add category function checks if Category already exits, if it does, it shows a message to Admin user that category already exits.

**Edit Category**
- Stricted for Admin use only.
- Page features a single line form allowing Admin user to edit the selected category.
- After submission Edit Category function checks if Category already exits, if it does, it shows a message to Admin user that category already exits.

**404 Error Page**
- Page features custom error message with a button that takes user back to the homepage

**500 Error Page**
- Page features custom error message with a button that takes user back to the homepage


### Features Left to Implement



## Technologies Used

### Languages Used

- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries, and Programs Used

- [Visiual Studio Code ](https://code.visualstudio.com)
    - **Vscode** Is the code editor used to develop, commit & push this project to Github.
- [GitHub](https://github.com/)
    - **Github** is used for:
    1. Tracking the project, and for version control.
    2. As a repository for other users to see the code used in the project.
    3. Deploying the final version of the project for live view. The deployed version can be viewed [here](https://wonderdam.herokuapp.com/homepage).
- [Bootstrap](https://www.bootstrapcdn.com/)
    - **Bootstrap**  to structure the website, and to achieve responsive layout across various mobile devices.
- [JQuery](https://jquery.com)
    - **JQuery**  used with Bootstrap.
- [MongoDB](https://www.mongodb.com/)
     - **MongoDB**  Source-available cross-platform document-oriented database program.
- [WOW.js](https://wowjs.uk)
    - **WOW.js**  a JavaScript plugin that reveals animations when you scroll.
- [Animate.css](https://animate.style)
    - **Animate.css**  a cross-browser library of CSS animations.
- [Adobe Fonts](https://fonts.adobe.com/)
    - **Adobe Fonts**  for importing typography.
- [Font Awesome](https://fontawesome.com/)
   - **Font Awesome** for adding a icons.
- [W3C Markup Validator](https://validator.w3.org/)
   - **W3C Markup Validator** to check validity of HTML code.
- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
   - **W3C CSS Validator** to check validity of CSS code.
- [JSHint Javascript Code Quality Tool](https://jshint.com/)
   - **JSHint Javascript Code Quality Tool** to check the quality of the Javascript code.
- [Balsamiq:](https://balsamiq.com/)
    - **Balsamiq** was used for creating [wireframes]() during the design process.




## Testing



### Testing User Stories from UX Design Section

#### First Time Visitor Goals



#### Returning Visitor Goals



#### Frequent User Goals



### Further Manual Testing



#### Google Lighthouse scores:

- Desktop:

<img src="" alt="lighthouse-desktop" width="500" height="170">

- Mobile:

<img src="" alt="lighthouse-mobile" width="500" height="180">

### Debugging



## Deployment

- To view the deployed version of [Wonderdam](..) I took the following steps:
    - Logged on to [GitHub](https://github.com/).
    - Selected **yigitaksoy/Wonderdam** from the list of repositories.
    - Selected **Settings** within the repository.
    - Scrolled down to **Github Pages**, and changed **source** to **master branch**.
    - The page automatically deployed.

- To add this repository to your local workspace:
    - Click on the [Wonderdam repository on GitHub](https://github.com/yigitaksoy/Wonderdam) link.
    - Click on the **Code** button, and copy the URL.
    - Go into your local workspace, and open up a new terminal.
    - Type `git clone ` and paste the URL you copied from GitHub, and press enter. It should look like this:
```console
git clone https://github.com/*username*/*repository*
```
The process of cloning is now completed. For further information on cloning,
 visit [How to clone from GitHub](https://help.github.com/en/articles/cloning-a-repository).



## Credits

### Content



### Media


### Codes

 - Code to fix mixed content issue was taken from [Stackoverflow](https://stackoverflow.com/questions/35178135/how-to-fix-insecure-content-was-loaded-over-https-but-requested-an-insecure-re/35178323)
 - Code for line-clamp was taken from [CSS Tricks](https://css-tricks.com/almanac/properties/l/line-clamp/)
 - Code to show image previews on Add/Edit Posts are taken from [Learn Code Web](https://learncodeweb.com/snippets/browse-button-in-bootstrap-4-with-select-image-preview/)
 - Code for user password input validation on Register form was taken from [Stackoverflow](https://stackoverflow.com/questions/21727317/how-to-check-confirm-password-field-in-form-without-reloading-page)
 - Code for HTML email input pattern attribute was taken from [Stackoverflow](https://stackoverflow.com/questions/5601647/html5-email-input-pattern-attribute)
 - Code for Setting up Flask Mail was taken from Karina's Flask Mail setup instructions on [Slack](https://slack-files.com/T0L30B202-F01KX8QUEJF-6a89867a18).
 - Code for styling and structuring the forms were taken from [Colorlib](https://colorlib.com/etc/regform/colorlib-regform-8/)
 - Code for fitting bootstrap card images evenly was taken from [Stackoverflow](https://stackoverflow.com/questions/37287153/how-to-get-images-in-bootstraps-card-to-be-the-same-height-width/53252725)
 - Code for live character count on Add/Edit Post forms were taken from [Codexworld](https://www.codexworld.com/live-character-counter-javascript/)


## Acknowledgements


## Disclaimer
- All content on the website, including images and text, are used for educational purposes only.

## Miscellaneous
- During the early development stages of the project, delete modal title was updated on User Profile page, but due to long hours of coding this commit was mis-stated as "Update delete modal title on post page" which was meant for Profile Page. [See commit](https://github.com/yigitaksoy/Wonderdam/commit/a0547907ea744e8d0e4447f9a7611a32a2c425dd)