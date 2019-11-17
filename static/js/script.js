const goBack = document.getElementsByClassName("go-back");
const buttonCollapse = document.getElementsByClassName("button-collapse");
const navbarContainer = document.getElementsByClassName("navbar-container");
const recipeLogoImage = document.getElementsByClassName("recipe-logo-image");
const toTop = document.getElementsByClassName("to-top");

/* 
Whatever code is written inside the JQuery ready method will run once the page Document Object Modal (DOM)
is ready to execute JavaScript code.
*/

$(document).ready(() => {
    // This is the jquery that gives the mobile burger icon the ability to toggle the mobile sidedrawer
    $(buttonCollapse).sideNav();
    $('input#input_text, textarea#textarea2').characterCounter();
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
    $(goBack).on("click", () => {
        window.history.back();
    });
});


