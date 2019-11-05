/* 
Whatever code is written inside the JQuery ready method will run once the page Document Object Modal (DOM)
is ready to execute JavaScript code.
*/

$(document).ready(() => {
    // This is the jquery that gives the mobile burger icon the ability to toggle the mobile sidedrawer
    $('.button-collapse').sideNav();

    // Will check to see if the window has been scrolled 50px from the top
    $(window).scroll(() => {
        const joinedBlueLighen = ['blue', 'lighten-1'].join(' ');
        const joinedNATransparent = ['N/A', 'transparent'].join(' ');
        if ($(document).scrollTop() > 50) {
            $(".navbar-container").removeClass(joinedNATransparent).addClass(joinedBlueLighen).css('box-shadow', 'rgb(70, 70, 70) 1px 1px 5px');
        }
        else {
            $(".navbar-container").removeClass(joinedBlueLighen).addClass(joinedNATransparent).css('box-shadow', 'none');
        }
    });
});
