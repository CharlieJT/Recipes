/* 
Whatever code is written inside the JQuery ready method will run once the page Document Object Modal (DOM)
is ready to execute JavaScript code.
*/

$(document).ready(() => {
    // This is the jquery that gives the mobile burger icon the ability to toggle the mobile sidedrawer
    $('.button-collapse').sideNav();

    // Will check to see if the window has been scrolled 50px from the top
    $(window).scroll(() => {
        const joinedNATransparent = ['N/A', 'transparent'].join(' ');
        if ($(document).scrollTop() > 50) {
            $(".navbar-container").removeClass(joinedNATransparent).css('background-color', '#000000a3');
            $(".recipe-logo-image").css('width', '55px');
        }
        else {
            $(".navbar-container").addClass(joinedNATransparent);
            $(".recipe-logo-image").css('width', '80px');
        }
    });
});
