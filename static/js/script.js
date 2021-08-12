// Hamburger menu button trigger
$(document).ready(function(){
	$('#nav-icon1').click(function(){
		$(this).toggleClass('open');
	});
});

// Menu Open
$('.hamburger-menu, .link').click(function () {
	$('body').hasClass('menu-open') ? ($('body').removeClass('menu-open')) : ($('body').addClass('menu-open'));
});


// Hide Header on on scroll down
var didScroll;
var lastScrollTop = 0;
var delta = 5;
var navbarHeight = $('header').outerHeight();
var bannerHeight = $('.banner').outerHeight();

$(window).scroll(function(event){
    didScroll = true;
});

setInterval(function() {
    if (didScroll) {
        hasScrolled();
        didScroll = false;
    }
}, 250);

function hasScrolled() {
    var st = $(this).scrollTop();

    // Make sure they scroll more than delta
    if(Math.abs(lastScrollTop - st) <= delta)
        return;

    // If they scrolled down and are past the navbar, add class .nav-up.
    // This is necessary so you never see what is "behind" the navbar.
    if (st > lastScrollTop && st > navbarHeight){
        // Scroll Down
        $('header').removeClass('nav-down').addClass('nav-up');
        $('.titles-collapse').removeClass('nav-down').addClass('titles-nav-up');
    } else {
        // Scroll Up
        if(st + $(window).height() < $(document).height()) {
            $('header').removeClass('nav-up').addClass('nav-down');
            $('.titles-collapse').removeClass('titles-nav-up').addClass('nav-down');
        }
    }

    lastScrollTop = st;
}