<h1 align="center">
Recipe Nest - Testing
</h1>

<div align="center">

[**Main README.md file**](README.md)

[Recipe Nest](https://listing-of-recipes.herokuapp.com)
</div>

## Contents Table

1. [**Automated Testing**](#automated-testing)
    - [**Validating Code**](#validating-code)

2. [**User Stories Testing**](#user-stories-testing)

3. [**Manual Testing**](#manual-testing)
    - [**Testing on Desktop**](#testing-on-desktop)
    - [**Testing on tablet and mobile devices**](#testing-on-tablet-and-mobile-devices)

<br>

## Automated Testing

### Validating Code

Validation services were used to ensure that code was valid code used to develop the website.

- [W3C Markup Validation Service](https://validator.w3.org/) was used to test HTML code to ensure it was valid code.
I needed to remove jinja to ensure this first.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) was used to test CSS code to ensure it was valid code.
- [Code Beautify JavaScript Validator](https://codebeautify.org/jsvalidate) was used to test JavaScript code to ensure it was valid code.


## User Stories Testing

This follows on from each of the **'User Stories'** items from the **'UX'** section in [README.md](README.md).

- ### As a user, I'd like to see:
    - ### A professional and strong looking website to draw the user into using the website.
        - A colour scheme of black, white & blue were used to help with a friendly looking design.
        - The Materialize library was used in order to give it a strong & professional look.
        - Everything was sectioned out nicely & carefully thought off to give the best presentation to the user.
        - A dark image was used as the main image to contrast nicely with the rest of the website.
        - Button colours were carefully selected to ensure they were coloured corrected to their primary prupose.
    - ### Navigations which are simple & informative which don't leave the user unsure of how to get to the page they want to get to.
        - You will find a navigation on every page of website.
        - The Recipe Logo will navigate you back to the home page.
        - Breadcrumbs have been added to all pages which are necessary to jump back to specific pages with
        the name of the page that is linked this helps alot with the website navigation.
        - If you hit the 404 error page at any point. There is a button which allows you to go back to the home page.
    - ### Buttons which are simple but informative & give a good indication of their purpose.
        - Button have been labelled correctly with their accordance.
        - They have been given the appropriate colour for either purpose.
    - ### Subtle animations to not overcomplicate the website, but to give a strong professional look & feel.
        - Buttons & images throughout the website have a nice waves effect when clicked.
        - Input fields are been given a nice animation when the field is active. The placeholder will jump to the top
        & the underline & placeholder will trasnform to blue.
        - A back to top chevron has a nice animation when you hover over it, it will transform to blue from white &
        rotate.
        - A downwards chevron has been animated to give an indication that there is more information below.
    - ### Good separation between each instruction.
        - When inputting the information for each instruction, It instructs you to input each piece of instructions,
        seperated by a full stop. When it reaches the front-end. It will list each item in a 'step' for each
        instruction.
    - ### I have full control over all recipes on the website.
        - You are able to view all of the recipes on the website.
        - You can search for any recipe on the website.
        - Any user can edit any of the recipes.
        - Any user can create a recipe.
        - Any user can delete any of the recipes.

## Manual Testing

A number of manual tests were done to ensure the website was working with it's intended purpose and use.

### Testing on Desktop

The website was tested numerous times in Browsers: Chrome, Safari, FireFox and Internet Explorer
on a Laptop, Macbook & Desktop PC.

#### 1. Dashboard

I checked that:

- The main image is loading properly, is 100 view height & there are no issues with the height or width.
- There is an animation on the search bar when the page is loaded for the first time, it should blur into vision.
- The animation for the downwards chevron is working & that it's clickable.
- There is no upwards chevron in the bottom right-hand corner until the page has been scrolled down.
- My Github repo in the footer links correctly to my github repo for the project & that it opens up in a new tab.
- The Favicon is loading correctly.
- The upwards chevron is appearing when scrolled down the page & that it's animating correctly when hovered over
& when it's clicked.
- The navbar is correctly animating so the main logo is decreasing in size & that is has a darkened background
when scrolled down.
- The footer was properly sitting at the bottom of the page as I added a sticky footer to the bottom.

#### 2. Home Page

I checked that:

- All images were loaded properly.
- It was showing the top 3 most viewed recipes on the home page, I confirmed this in MongoDB.
- All information on each card was loading correctly.
- The search bar was correctly animating when the input field is active & that it's changing colour.
- The link 'Home' is slightly lighter in colour than the rest of the links in the footer.
- That the link for the search bar is working correctly by testing numerous inputs.
- Each card on the home page links correctly to the recipe page when clicking the image, the title &
the button, also that is linking to the correct recipe.
- Each of the ellipses on each of the card will show the description of the recipe when clicked.
- On all displays from 992 pixels & upwards that everything is sitting correctly on the page &
that nothing is out of place.
- All images dimensions are accounted for.

#### 3. Recipe Listing

I checked that:

- All images were loaded properly.
- It was showing all of the available recipes, I confirmed this in MongoDB.
- All information on each card was loading correctly.
- The search bar was correctly animating when the input field is active & that it's changing colour.
- The link 'List Of Recipes' is slightly lighter in colour than the rest of the links in the footer.
- Each card on the home page links correctly to the recipe page when clicking the image, the title &
the button, also that is linking to the correct recipe.
- That the link for the search bar is working correctly by testing numerous inputs.
- Each of the ellipses on each of the card will show the description of the recipe when clicked.
- Checked on all displays from 992 pixels & upwards that everything is sitting correctly on the page &
that nothing is out of place.
- The breadcrumb was sitting correctly with the correct links & linking to their respective page.
- Ensure that all images dimensions are accounted for.

#### 4. Recipe

I checked that:

- All images were loaded properly on all recipes.
- It was showing the correct recipe along with all of the information coming through.
- Each of the steps of the ingredients which were separated with a full stop & coming through as a list.
- Each of the steps of the instructions which were separated with a full stop & coming as steps.
- When the page is reloaded, the view count incremented by 1.
- The breadcrumb was sitting correctly with the correct links & linking to their respective page.
- Checked on all displays from 992 pixels & upwards that everything is sitting correctly on the page &
that nothing is out of place.
- Edit button was correctly linking to the edit page & the delete button was displaying a modal with buttons
that were linking to their appropriate action.

#### 5. Create Recipe

I checked that:

- The form is sitting correctly on the page.
- Each required input field in the form has a red asterisk next to it.
- Each input field has a placeholder with the appropriate name & action if necessary.
- The breadcrumb was sitting correctly with the correct links & linking to their respective page.
- Each input field was correctly animating when the input field is active & that it's changing colour.
- Validation is implemented correctly and if the 'Create Recipe' button is clicked
with a required field being empty, it will flag up with red text underneath all of the fields
that need to be filled.
- When all of the required fields are filled in, & the 'Create Recipe' button is clicked,
it will fire off the 'insert_recipe' function in app.py & redirect to the recipe listing page
with the new recipe being implemented.
- A recipe can still be created if an 'optional' field is not filled out.
- The recipe had been successfully created by viewing the recipe on the recipe page & checked
to ensure it is visible in MongoDB with the viewing count set to '1'.
- The link 'Create Recipe' is slightly lighter in colour than the rest of the links in the footer.


#### 6. Edit Recipe

I checked that:

- The form is sitting correctly on the page.
- Each required input field in the form has a red asterisk next to it.
- Each input field has been auto-filled with the correct information stored in MongoDB.
- The breadcrumb was sitting correctly with the correct links & linking to their respective page.
- Each input field was correctly animating when the input field is active & that it's changing colour.
- Validation is implemented correctly and if the 'Update Recipe' button is clicked
with a required field being empty, it will flag up with red text underneath all of the fields
that need to be filled.
- When all of the required fields are filled in, & the 'Update Recipe' button is clicked,
it will fire off the 'update_recipe' function in app.py & redirect to the recipe listing page
with the recipe being updated with the correct information.
- A recipe can still be editted if an 'optional' field is not filled out.
- The recipe had been successfully updated by viewing the recipe on the recipe page & checked
to ensure it is visible in MongoDB with the viewing count set to '1'.


#### 7. Search Recipe

I checked that:

- When anytime are the search function is triggered by making a search, you will be linked to the search page.
- The input of any of the search bar will do a find through the recipe name, recipe description,
recipe instructions & any recipe keywords that are found in the database.
- If no matches are found in the database, it will display 'No results have been found' with 
a sad face image.
- The search bar still works inside of the search page.
- Both enter & the button works when doing a search.
- The breadcrumb was sitting correctly with the correct links & linking to their respective page.
- It was displaying the amount of recipes that had been found as well as displaying the query
that had been inputted into the search bar.

#### 8. 404 Error

I checked that:

- When a url has been inserted wrong or doesn't match with any of the functions that has
been set up in app.py, the error 404 function will fire off & will display the 404 error page.
- A title, image of an empty plate & a brief description of what has happened is displayed along
with a button to the 'Home Page'.
- The button to the Home Page is correctly firing off & will link you back to the home page.
