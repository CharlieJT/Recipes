/* 
Whatever code is written inside the JQuery ready method will run once the page Document Object Modal (DOM)
is ready to execute JavaScript code.
*/

$(document).ready(() => {
    // This is the jquery that gives the mobile burger icon the ability to toggle the mobile sidedrawer
    $('.button-collapse').sideNav();
    $('input#input_text, textarea#textarea2').characterCounter();
    // Will check to see if the window has been scrolled 50px from the top
    $(window).scroll(() => {
        const joinedNATransparent = ['N/A', 'transparent'].join(' ');
        if ($(document).scrollTop() > 50) {
            $(".navbar-container").removeClass(joinedNATransparent).css('background-color', '#000000a3');
            $(".recipe-logo-image").css({ 'width': '66px', 'margin-top': '0px' });
            $('.to-top').css('opacity', '1');
        }
        else {
            $(".navbar-container").addClass(joinedNATransparent);
            $(".recipe-logo-image").css({ 'width': '95px', 'margin-top': '5px' });
            $('.to-top').css('opacity', '0');
        }
    });
    // Will remove active class and add new active class depending on which is matched with the pathname
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
});
