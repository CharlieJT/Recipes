<h1 align="center">
Data Centric - Milestone Project 3 - Recipe Nest - Charlie Tipton
</h1>

<div align="center">
    <img src="https://i.ibb.co/L9tFSwY/recipe-nest-home-page.png" href="https://listing-of-recipes.herokuapp.com" target="_blank" alt="Responsive displays of Recipe Nest" border="0">
</div>
<br>

[Recipe Nest](https://listing-of-recipes.herokuapp.com) is a website created to give users access & full control over recipes.
It's a platform that has been designed to allow the user to be able to easily browse for different recipes,
allowing users to create their own recipes, make any amendments to recipes & gives the user the option
to be able to delete their recipes. In addition to friendly colours, designs & animations, it makes a great
recipe platform!

<br><br>
[**View Recipe Nest website here in Heroku!**](https://listing-of-recipes.herokuapp.com)

</div>

## Contents Table

1. [**UX**](#ux)
    - [**Project Purpose**](#project-purpose)
    - [**User Experience**](#user-experience)
    - [**User Stories**](#user-stories)
    - [**Design Ideas**](#design-ideas)
    - [**Wireframes**](#wireframes)
    - [**Developer and Business Purpose**](#developer-and-business-purpose)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Database**](#database)
    - [**Data types**](#data-types)
    - [**Recipes Database**](#recipes-database)

4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)

6. [**Deployement**](#deployment)
    - [**To run on your local IDE**](#to-run-on-your-local-ide)
    - [**Deploy to Heroku**](#deploy-to-heroku)

7. [**Credits**](#credits)
    - [**Contents**](#contents)
    - [**Media**](#media)
    - [**Help with code**](#help-with-code)
    - [**Acknowledgements**](#acknowledgements)

8. [**Disclaimer**](#disclaimer)

## UX

### Project Purpose

The goal of Recipe Nest is to give users full access & control over all recipes. This
means they are able to create recipes, view all recipes, update any recipe & delete any recipe.

### User Experience

- Users get a great sense of usability from the get-go. They are presented with a burger icon at the top of
the screen for mobile & tablet display & a navigation bar on desktop display for Home, List of recipes &
Create recipe. A logo has been included in the top right on mobile and tablet & top left on desktop to help
easily navigate back to the homepage at any given time.

- An introductory heading has been included to welcome the user to the website.

- A search bar has been included on all displays so they can search for a recipe they would like to find
right away along with a down chevron (arrow), which has been placed as an indicator to the user that
there is more information below should the user be confused. The arrow is also clickable & will smoothly scroll
down the page when it's clicked.

- All cards on the website have a clickable image, title & 'view recipe' button which will navigate the
user to that particular recipe page. Should they want a quick look at the description of the recipe,
ellipses (3 vertical dots) have been put on each card as an indicator to view the description before
they click to view the whole recipe.

- Bread crumbs have been included at the top of specific pages to help easily navigate back to pages
they have previously come from.

- When a user has mistakenly inputted a wrong path in the URL, a 404 page will show with a link back to the
home page.

- Asterisks (Star symbols) have been included in each form fields to indicate which fields are required to be
filled in before submission. If a user has submitted a form without filling in a required field, validation
has been included & will prompt the user to input any particular input field that is required. Also, placeholders have been
given to instruct the users on how the information they give should be sectioned out.

- Edit recipe fields are filled out automatically so that the user does not need to input all of the previous values back in
before they submit an update.

- When the delete button is clicked on the recipe page, the user is presented with a modal to ensure they want to
delete their recipe permanently.

- The player does not need to click a back button or to reload the page. Easy and informative buttons have been provided
at all times to ensure the user has an easy way around the website.

### Design Ideas

- #### As a user, I'd like to see:
    - A professional and strong looking website to draw the user into using the website.
    - Navigations which are simple & informative which don't leave the user unsure of how to get to the page they want to get to.
    - Buttons which are simple but informative & give a good indication of their purpose.
    - Subtle animations to not overcomplicate the website, but to give a strong professional look & feel.
    - Good separation between each instruction.
    - I have full control over all recipes on the website.
    
### Design Ideas

The design of the website was to give a clean & intuitive look & feel ensuring the user gets the best experience.

- #### Fonts

    - The font **'Open Sans'** was chosen as the primary font to ensure it had a professional look.

- #### Colours

    - **Main Heading and Footer -** A white font was selected for the heading to contrast nicely with the dark background
    of the main image of the home page &  was also selected for the footer to contrast nicely with the blue background.
    
    - **Cards -** A white background for each card was kept as a nice indicator of a 'card' & a box-shadow was kept
    to give a nice separation between the background of the outer card & the inner card. This was contrasted nicely with
    black text.
    
    - **To Top Arrow -** A white 'up' chevron was contrasted nicely with a darkened background & a white border
    & when hovered over, the white chevron & border transformed to blue, this was to give a nice live look & feel to
    the chevron.
    
    - **Edit & Delete Buttons -** An blue colour for the edit button was chosen to conform with the buttons of the website
    & the delete button was styled with red to indicate a 'danger' or (be aware) feel. This was contrasted nicely with white text.
    
    - **Forms -** A white background was chosen to conform to the website & a red asterisk was added to indicate that
    the field 'must' be populated before submission. Also, red text was added to validation test when a user submitted
    a form that had not been completed as it gave off a 'must' feel.
    
    - **Active Input fields -** When an input field is active, the test & bottom border transforms to blue, this
    is to conform with the colours used on the website.
    
    
- #### Styling

    Styles have been made to give a professional, strong look. With the help of the CSS framework
    [Materialize!](https://materializecss.com/), I was able to implement a nice looking & well animated
    website without going over the top.
    
    **Special styles include:**
    
    - **Input fields -** Input fields were produced with the help of materialize to give a nice
    subtle animation when the user clicks on a field, the placeholder will bounce to the top of the field,
    change the bottom border & text to blue & allow the user to input text.
    
    - **Buttons & images** With the help of materialize, when all buttons or images on cards are clicked,
    a nice waves effect is triggered giving it a nice subtle animation.
    
    - **Down chevron** A downwards chevron was included underneath the homepage search bar to give an
    indication that the user will have more information to scroll down to, this was animated specifically for
    it to look as if it is flicking down. When clicked, it will scroll the user down in a smooth fashion.
    
    - **Up chevron -** When a user scrolls 50 pixels down from the top of any page, an 'up' chevron will appear
    in the bottom left-hand corner of the screen. When hovered over on desktop, it will rotate 360° &
    border & chevron colour will change to blue. When clicked on mobile & tablet, it will perform the animation
    as the page is scrolling back to the top. When clicked it will smooth scroll back to the top & the icon will
    disappear. The logic behind it can be found [here!](https://freefrontend.com/css-arrows/).
    
    - **Navbar shrinking -** When a user scrolls 50 pixels down from the top of any page, the user will notice that
    the logo will shrink in size and the background of the navbar be sticky and have a dark background, this is to make sure
    it doesn't take up too much space & so it can still be seen by the user.
    
    - **Active pages -** When either the Home, List of Recipes or Create Page is active, depending on whichever it is,
    The navbar on desktop displays a white underline underneath the corrisponding page. On mobile, it colours the background
    of the corresponding page to grey & in the footer, the corresponding text will be grey, which will only work if
    one of those pages is active.
    
- #### Main background

    The main background image has been requested by the developer and been granted permission to use them for educational purposes.
 
    - The main background of the website has been styled with a dark background with different ingredients. This is to contrast
    nicely with the white text on the navbar, the search bar & the main logo.
    
### Wireframes

Wireframes were made using [Balsamiq](https://balsamiq.com/) for a clean looking design layout.

- #### Desktop Wireframes

    - [Home Page 1 - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-home-page-1.png)
    - [Home Page 2 - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-home-page-2.png)
    - [Home Page 3 - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-home-page-3.png)
    - [Recipe Listing Page 1 - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-recipe-listing-page-1.png)
    - [Recipe Listing Page 2 - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-recipe-listing-page-2.png)
    - [Recipe Page - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-recipe-page-1.png)
    - [Create Recipe Page - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-create-recipe-page-1.png)
    - [Edit Recipe Page - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-edit-recipe-page-1.png)
    - [Search Recipe Page - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-search-page-1.png)
    - [404 Error Page - Desktop Display](static/images/wireframes/desktop-wireframes/recipe-nest-404-error-page-1.png)

- #### Tablet Wireframes

    - [Home Page 1 - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-home-page-1.png)
    - [Home Page 2 - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-home-page-2.png)
    - [Home Page 3 - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-home-page-3.png)
    - [Recipe Listing Page 1 - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-recipe-listing-page-1.png)
    - [Recipe Page - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-recipe-page-1.png)
    - [Create Recipe Page - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-create-recipe-page-1.png)
    - [Edit Recipe Page - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-edit-recipe-page-1.png)
    - [Search Recipe Page - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-search-page-1.png)
    - [404 Error Page - Tablet Display](static/images/wireframes/tablet-wireframes/recipe-nest-404-error-page-1.png)
 
 
- #### Mobile Wireframes

    - [Home Page 1 - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-home-page-1.png)
    - [Home Page 2 - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-home-page-2.png)
    - [Home Page 3 - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-home-page-3.png)
    - [Recipe Listing Page 1 - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-recipe-listing-page-1.png)
    - [Recipe Page - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-recipe-page-1.png)
    - [Create Recipe Page - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-create-recipe-page-1.png)
    - [Edit Recipe Page - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-edit-recipe-page-1.png)
    - [Search Recipe Page - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-search-page-1.png)
    - [404 Error Page - Mobile Display](static/images/wireframes/mobile-wireframes/recipe-nest-404-error-page-1.png)
 

### Developer and Business Purpose

- Should be prepared for any double click, fast clicking or clicking different parts of the website.
Every feature must react to it's intended purpose.

- Must show clear & professional examples of HTML, CSS, JavaScript, jQuery & Python.

- A great example project to put as part of a portfolio.


## Features

### Existing Features

1. #### Home Page

    <div align="center">
        <img src="https://i.ibb.co/L9tFSwY/recipe-nest-home-page.png" width=400 href="https://listing-of-recipes.herokuapp.com" target="_blank" alt="Responsive displays of Recipe Nest Home" border="0">
    </div>
    <br>
    
    - When you arrive at the page for the very first time, you will be presented with a dark recipe background,
    an input search box in the centre of the screen where you can search for a recipe right from the get-go
    & a logo in the top corner along with navigation in the opposite corner. 
    
    - A down chevron will be displayed underneath the search box as an indication for the user to scroll down. When clicked,
    it will smooth scroll you down to the next section of the home page.
    
    - The navbar will also shrink when a user has scrolled down, this is to ensure that it doesn't take up too much space &
    the background is darkened to ensure it can be seen at all times.
    
    - When you've scrolled down to the next section, you'll be presented with the top 3 viewed recipes on the website
    which is dependant on how many times each particular recipe has been viewed on its specific recipe page.
    
    - With each most viewed recipe cards, you can click the ellipses (3 vertical dots) to see that particular description &
    by clicking on the image, name or 'view recipe' button, it will navigate you to view the recipe.
    
    - The footer positioned at the bottom of the screen shows links to the Home, Recipe listing & Create recipe pages,
    a brief description of the main purpose of the website, a link to the developers github repository & copyright text at the bottom.
    
    
2. #### Recipe Listing Page

    <div align="center">
        <img src="https://i.ibb.co/QKf3CWB/recipe-nest-recipe-listing-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/recipe_listing" target="_blank" alt="Responsive displays of Recipe Nest Recipe Listing" border="0">
    </div>
    <br>
    
    - When you arrive at the recipe listing page, you will be presented with a breadcrumb which will navigate you back to the
    homepage & will show you you're currently on the recipe listing page. You also have the option to search
    for a particular recipe from there too. 
    
    - You are also presented with all of the recipes that are on the website with the option to click the ellipses (3 vertical dots)
    to see that particular description & by clicking on the image, name or 'view recipe' button, it will navigate you to view the recipe.
    
3. #### Recipe Page 

    <div align="center">
        <img src="https://i.ibb.co/NL4t2PD/recipe-nest-recipe-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/recipe" target="_blank" alt="Responsive displays of Recipe Nest Recipe" border="0">
    </div>
    <br>
    
    - When you arrive at the recipe page, you are presented with the entire recipe, this will show the recipe name,
    recipe image, recipe description, recipe ingredients & recipe instructions.
    
    - An edit button has been included in this page so you can navigate to edit the recipe if the user would like to add
    additional information, adjust information or delete information.
    
    - A delete button has also been included so that the user has the option to delete the recipe, a modal will be presented
    upon clicking the modal to ensure that the user is notified with the outcome of deleting a recipe before they permanantly
    delete it.
    
    - List items of ingredients are shown of each ingredient.
    
    - A step by step guide of instruction will be shown.
    
    - You will be presented with a breadcrumb which will navigate you back to the homepage or back to the recipe listings page
    and will show that you're currently on the recipe page.
    
4. #### Create Recipe Page 

    <div align="center">
        <img src="https://i.ibb.co/x5vdYD6/recipe-nest-create-recipe-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/create_recipe" target="_blank" alt="Responsive displays of Recipe Nest Create" border="0">
    </div>
    <br>
    
    - When you arrive at the create recipe page, you are presented with a form which will show the following fields.
        - Recipe Name
        - Recipe Description
        - Recipe Ingredients
        - Recipe Instructions
        - Recipe Keywords
        - Recipe Image URL
        - Create Recipe 'button'
    
    - You will be presented with a breadcrumb which will navigate you back to the homepage & will show that
    you're currently on the create recipe page.
    
    - Each field except for the 'Recipe Keywords' field is a required field and has a red asterisk next to each of them
    to indicate that you 'must' fill that field. If not done & the user clicks submit, the user will be prompted to input
    all of the required fields with red text under each of them.
    
5. #### Edit Recipe Page

    <div align="center">
        <img src="https://i.ibb.co/m5qGmXr/recipe-nest-edit-recipe-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/edit_recipe" target="_blank" alt="Responsive displays of Recipe Nest Edit" border="0">
    </div>
    <br>
    
    - When you arrive at the edit recipe page, you are presented with a form which will show the following fields
    (these fields will have inputs with the original recipe that is going to be editing).
        - Recipe Name
        - Recipe Description
        - Recipe Ingredients
        - Recipe Instructions
        - Recipe Keywords
        - Recipe Image URL
        - Update Recipe 'button'
    
    - You will be presented with a breadcrumb which will navigate you back to the homepage, back to the recipe listing,
    back to the recipe & will show that you're currently on the create recipe page.
    
    - Each field except for the 'Recipe Keywords' field is a required field and has a red asterisk next to each of them
    to indicate that you 'must' fill that field. If not done & the user clicks submit, the user will be prompted to input
    all of the required fields with red text under each of them.

6. #### Search Recipe Page

    <div align="center">
        <img src="https://i.ibb.co/cFkTbvL/recipe-nest-search-recipe-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/search?query=burger&action=" target="_blank" alt="Responsive displays of Recipe Nest Search" border="0">
    </div>
    <br>
    
    - When you have inputted something into any of the search fields throughout the website, you will
    be taken to the search recipe page. Here, you will be presented with a title showing how many search items
    have been found of whatever query was inputted into the search field.
    
    - You are then given the option to search for another item.
    
    - If no results have been found for your query, you will be notified with text informing you
    that no results have been found with a sad face.
    
    - You will be presented with a breadcrumb which will navigate you back to the homepage or back to the recipe listings page
    and will show that you're currently on the search page with the number of results found & the
    query that has been inputted.

7. #### Error 404 Page

    <div align="center">
        <img src="https://i.ibb.co/GkZBvy9/recipe-nest-404-error-page.png" width=400 href="https://listing-of-recipes.herokuapp.com/anything" target="_blank" alt="Responsive displays of Recipe Nest 404 Error" border="0">
    </div>
    <br>
    
    - If at anytime the user has inputted a value in the URL that has not been found, a 404
    page will be presented.
    
    - The page will show the user a message explaining that they've gotten lost & will have a button
    which will lead them back to the home page.

### Features Left to Implement

1. #### Pagination

    - Pagination on recipe listing page & search page. This will help with keeping everything
    more organised & help with loading time.

2. #### Logging in

    - A logging in feature should be implemented so that you can have control over your own recipes
    & only your own. This will prevent people being able to tamper or delete your recipes.
    
## Database

### MongoDB

- The database used for this project was a NoSQL database called MongoDB which is a requirement
for this particular project & to gain experience using a NoSQL database.

### Data types

- For this project, the types of data that are used are:
    - ObjectId
    - String
    - Int32(Integer)
    
### Recipes Database

- A database was created called 'myRecipes' which contains a collection called recipes which is where
- each piece of data for each 'recipe' is stored. The data structure are as follows:

| Name of field | field key | field value | type |
--- | --- | --- | --- 
Recipe ID | _id | `<Creates ID automatically>` | ObjectId 
Recipe Name | recipe_name | `<Name of your Recipe>` | string
Recipe Description | recipe_description | `<Describe your recipe in a paragraph>` | string
Recipe Ingredients | recipe_ingredients | `<Each ingredient in recipe>` | string
Recipe Instructions | recipe_instructions | `<Each instruction in recipe>` | string
Recipe Image URL | recipe_image_url | `<Full image path of recipe>` | string
Amount of views | views | `<Amount of viewings of recipe>` | int32

#### Views

- A view will begin at 1 when the recipe has been created & will then increment by 1 everytime that a
partilcar recipe is used on the website with the corresponding ID.

## Technologies Used

- This project uses HTML, CSS, JavaScript, Python, Flask, MongoDB and various different technologies to work as helpers to the languages.
- #### [Cloud9](https://c9.io)
    - **Cloud9** is an IDE used to develop the website.
- #### [MongoDB](https://www.mongodb.com/)
    - **MongoDB** short for (Humongous database) is a database platform used to store all of the
    data for each recipe that is used on the website.
- #### [Materialize](https://materializecss.com/)
    - **Materialize** is s modern responsive front-end framework based on Material Design
    -  It's used to create professional looking cards, search boxes & overall style of the website.
    - It also allows for responsive design of the website. 
- #### [JQuery](https://jquery.com)
    - **JQuery** has been used to simplify DOM manipulation.
- #### [GitHub](https://github.com/)
    - **Github** is used: 
    1. As a remote backup of code used in the project.
- #### [AutoPrefixer](https://autoprefixer.github.io/)
    - **AutoPrefixer** is used to ensure all css prefixes are running with the most up to date versions.
- #### [Heroku](https://www.heroku.com)
    - **Heroku** is used as a platform for the project to be deployed to.
    - For users to view the deployed version of the website. The deployed version can be viewed [here!](https://listing-of-recipes.herokuapp.com).

## Testing

A full testing process can be found in a separate [tests.md](tests.md) file.

## Deployment

### To run on your local IDE

The project was built using [Cloud9](https://c9.io), through a built-in function called 'Git', I could commit

- You must ensure that the following are installed on your machine before you can work with it in your IDE.
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
    - You must have an account in [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or have it running locally
    on your machine (You can find instructions of setting it up [here](https://docs.atlas.mongodb.com/).

#### Instructions
1. Go to https://github.com/CharlieJT/Recipes and click the 'Clone or download' button and then click 'Download ZIP'
& extract to a folder of your choice. Ensuring you have Git installed on your system, you can clone the project into
your IDE through running the following command in the terminal
```console
git clone https://github.com/*username*/*repository*
```

2. Ensure you have open a terminal (Some IDE's such as Cloud9 & VSCode have a built in terminal but if not, you may need
3. to open one up on your desktop), cd to the correct location to where you have your ZIP file.
4. if running in Cloud9, you won't need to do this step as it comes with a built in virtual environment but if it doesn't,
you need to run the following command to build a virtual environment:
```
python -m .venv venv
```  

5. Use the following command to run a DNS toolkit for Python
```
sudo pip3 install dnspython
```

6. Use the following command to allow your project to run along side mongodb in python
```
sudo pip3 install pymongo
```

_Your Python can vary, i.e. python3, py._

7. If your IDE requires a virtual environment, run the following command to activate it:
```
.venv\Scripts\activate 
```
_This may vary so be sure to check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) to make sure you're sure._

8. Install a requirements.txt file with of the correct packages that you need for the project with: 
```
pip -r requirements.txt
```
_Check to ensure that you have all of the required packages you need for the project._

9.  Should you need to the latest version of pip, you can get it by running the following command.
```
pip install --upgrade pip
```

10. Go into your .flaskenv file & create a MONGO_URI which is a link to your database in MongoDB it should look something like this

```
mongodb+srv://<username>:<password in mongo db>@<cluster_name>-qtxun.mongodb.net/<database name>?retryWrites=true&w=majority
```

11. With the following command, run your app.py file using the following command

```
python3 app.py
```

12. Then click on `http://127.0.0.1:5000` which will display in the termimal to view the project.

### Deploy to Heroku

- The following steps to deploy to Heroku in the terminal

1. You need to run the command `echo web: python app.py > Procfile` which will create a Procfile.

2. You need to add a requirements.txt file by using the command `sudo pip3 freeze —local > requirements.txt`
which will add all of the package that you need to use for the project.

3. Use `git add .` to stage all of your files `git commit -m "<message here>"` to commit the changes ready to push to github

4. You must then create a repository in github & follow the instructions in order to push your work up to github.

5. Using `git push` & inputting your email & password when instructed, this will push all of the files
that have been committed up to github.
_Note that the password field will not change when you are inserting text_

6. Go to heroku [here](https://dashboard.heroku.com/) & ensure you are signed up.

7. Go to your Heroku dashboard & click "New" & click "Create New App".

8. Give any name you like & set the region to "Europe".

9. Ensure you link the heroku application to the correct Github repository.

10. Click inside of your app that you've just created and go to "Settings" then to "Reveal Config Vars".
They should all read as follows:

| Key | Value |
--- | ---
IP | 0.0.0.0 
MONGO_ URI | <string at section 10 in instructions ^>
PORT | 5000


then click add after each one to insert.

10. Go back to the top & go to "Deploy" and scroll down to the list of instructions given to deploy your project to heroku,
this should be done in the terminal.

11. After these step are done correctly, you can scroll to the very top of the page in Heroku & click
"Open App". You will now be able to view the project in Heroku.

## Credits

### Contents

- All Content has been thought of and written by the Developer. 


### Media

- #### Images
    - The Main background image for the website was found [here](https://www.pinterest.nz/pin/346566133817029961/)
    - The Recipe Nest logo was created [here](https://www.brandcrowd.com/maker/tag/name)
    - The Favicon was create [here](ttps://favicon.io/favicon-converter/)

### Help with code

- Ideas on how to write out the code for the Up Arrow: [Up Arrow](https://freefrontend.com/css-arrows).
- Ideas on how to apply the functionality for an action taking place when scrolled down from top:
[How TO - Scroll Back To Top Button](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp).
- Ideas on how to add a sticky footer, ensuring it will stay at the bottom of the page at all times:
[Sticky Footer, Five Ways](https://css-tricks.com/couple-takes-sticky-footer/)
    
The code learned from the snippet was not copied into the project, they were used as help and guidance to be interpreted in a different and unique way.

### Acknowledgements

A huge thank you to:

- Spencer Barriball (spence_mentor) - For helping me with planning & preperation as well as providing me with
useful tips & tricks to use in my project, also helping me with issues along the way.

- Martin (Code Institute) - For hepling me with a requirement.txt file that wasn't allowing me to deploy my project properly
to Heroku.

- Tim (Code Institute) - For a minor fix with an image file path which would not allow me to view my images with jinja in heroku. 

## Disclaimer

All content on the website, including images, are used for educational purposes only.