
(function ($) {

  "use strict";

  // HERO SLIDE
  $('.hero-slide').backstretch([
    "https://images.pexels.com/photos/3965543/pexels-photo-3965543.jpeg?cs=srgb&dl=pexels-kseniachernaya-3965543.jpg&fm=jpg",
    "https://img.freepik.com/premium-photo/modern-automatic-high-technology-embroidery-machine-textile-clothing-apparel_620624-155.jpg",
    "https://cdn.pixabay.com/photo/2016/07/12/11/45/towels-1511875_640.jpg"
  ],  {duration: 2000, fade: 750});

  // REVIEWS CAROUSEL
  $('.reviews-carousel').owlCarousel({
    items:3,
    loop:true,
    dots: false,
    nav: true,
    autoplay: true,
    margin:30,
    responsive:{
      0:{
        items:1
      },
      600:{
        items:2
      },
      1000:{
        items:3
      }
    }
  })

  // CUSTOM LINK
  $('.smoothscroll').click(function(){
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height();

    scrollToDiv(elWrapped,header_height);
    return false;

    function scrollToDiv(element,navheight){
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop-navheight;

      $('body,html').animate({
        scrollTop: totalScroll
      }, 300);
    }
  });

})(window.jQuery);


