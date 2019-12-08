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
ellipses (3 horizontal dots) have been put on each card as an indicator to view the description before
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
    
    - **Up Chevron -** When a user scrolls 50 pixels down from the top of any page. An 'up' chevron will appear
    in the bottom left-hand corner of the screen. When hovered over on desktop, it will rotate 360° &
    border & chevron colour will change to blue. When clicked on mobile & tablet, it will perform the animation
    as the page is scrolling back to the top. When clicked it will smooth scroll back to the top & the icon will
    disappear.
    
    - **Active Pages -** When either the Home, List of Recipes or Create Page is active, depending on whichever it is,
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

- #### Mobile Wireframes

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