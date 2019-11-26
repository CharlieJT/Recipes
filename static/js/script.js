// Constants used to target specific class names needed for jQuery

const goBackOnePage = document.getElementsByClassName("go-back-one-page");
const buttonCollapse = document.getElementsByClassName("button-collapse");
const navbarContainer = document.getElementsByClassName("navbar-container");
const recipeLogoImage = document.getElementsByClassName("recipe-logo-image");
const toTop = document.getElementsByClassName("to-top");
const createRecipeSubmitButton = document.getElementsByClassName("create-recipe-submit-button");

/* 
Whatever code is written inside the JQuery ready method will run once the page Document Object Modal (DOM)
is ready to execute JavaScript code.
*/

$(document).ready(() => {
    // Will check to see if the window has been scrolled 50px from the top.
    $(window).scroll(() => {
        const joinedNATransparent = ['N/A', 'transparent'].join(' ');
        if ($(document).scrollTop() > 50) {
            $(navbarContainer).removeClass(joinedNATransparent).css('background-color', '#000000a3');
            $(recipeLogoImage).css({ 'width': '66px', 'margin-top': '0px' });
            $(toTop).css('opacity', '1');
        }
        else {
            $(navbarContainer).addClass(joinedNATransparent);
            $(recipeLogoImage).css({ 'width': '95px', 'margin-top': '5px' });
            $(toTop).css('opacity', '0');
        }
    });
    // Will remove active class and add new active class depending on which is matched with the pathname.
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');

    // Will take the user back to the previous page on click.
    $(goBackOnePage).on('click', () => {
        window.history.back(1);
    });
    
    $('.button-collapse').sideNav();
    
    $('.modal').modal();

    /*
    Will be resonsible for form validation, depending on which field is empty, it will throw a message at the bottom
    of the field.
    */

    $('.insert-recipe-name').on('change', () => {
        $('.insert-recipe-name-validation').removeClass('insert-recipe-name-validation-flag');
    }).on('keypress', () => {
        $('.insert-recipe-name-validation').removeClass('insert-recipe-name-validation-flag');
    });
    $('.insert-recipe-description').on('change', () => {
        $('.insert-recipe-description-validation').removeClass('insert-recipe-description-validation-flag');
    }).on('keypress', () => {
        $('.insert-recipe-description-validation').removeClass('insert-recipe-description-validation-flag');
    });
    $('.insert-recipe-ingredients').on('change', () => {
        $('.insert-recipe-ingredients-validation').removeClass('insert-recipe-ingredients-validation-flag');
    }).on('keypress', () => {
        $('.insert-recipe-ingredients-validation').removeClass('insert-recipe-ingredients-validation-flag');
    });
    $('.insert-recipe-instructions').on('change', () => {
        $('.insert-recipe-instructions-validation').removeClass('insert-recipe-instructions-validation-flag');
    }).on('keypress', () => {
        $('.insert-recipe-instructions-validation').removeClass('insert-recipe-instructions-validation-flag');
    });
    $('.insert-recipe-image-url').on('change', () => {
        $('.insert-recipe-image-url-validation').removeClass('insert-recipe-image-url-validation-flag');
    }).on('keypress', () => {
        $('.insert-recipe-image-url-validation').removeClass('insert-recipe-image-url-validation-flag');
    });

    $(createRecipeSubmitButton).on('click', () => {
        // Constants used to target each form field's value on create recipe page
        const inputRecipeName = $("input[type=text][name=recipe_name]").val();
        const inputRecipeDescription = $("input[type=text][name=recipe_description]").val();
        const inputRecipeIngredients = $("textarea[type=text][name=recipe_ingredients]").val();
        const inputRecipeInstructions = $("textarea[type=text][name=recipe_instructions]").val();
        const inputRecipeImageUrl = $("input[type=text][name=recipe_image_url]").val();


        if (inputRecipeName.length === 0) {
            $('.insert-recipe-name-validation').addClass('insert-recipe-name-validation-flag');
        }
        else {
            $('.insert-recipe-name-validation').removeClass('insert-recipe-name-validation-flag');
        }

        if (inputRecipeDescription.length === 0) {
            $('.insert-recipe-description-validation').addClass('insert-recipe-description-validation-flag');
        }
        else {
            $('.insert-recipe-description-validation').removeClass('insert-recipe-description-validation-flag');
        }

        if (inputRecipeIngredients.length === 0) {
            $('.insert-recipe-ingredients-validation').addClass('insert-recipe-ingredients-validation-flag');
        }
        else {
            $('.insert-recipe-ingredients-validation').removeClass('insert-recipe-ingredients-validation-flag');
        }

        if (inputRecipeInstructions.length === 0) {
            $('.insert-recipe-instructions-validation').addClass('insert-recipe-instructions-validation-flag');
        }
        else {
            $('.insert-recipe-instructions-validation').removeClass('insert-recipe-instructions-validation-flag');
        }

        if (inputRecipeImageUrl.length === 0) {
            $('.insert-recipe-image-url-validation').addClass('insert-recipe-image-url-validation-flag');
        }
        else {
            $('.insert-recipe-image-url-validation').removeClass('insert-recipe-image-url-validation-flag');
        }
    });
});
