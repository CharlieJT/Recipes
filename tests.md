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