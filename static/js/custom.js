/* ===========================================
                    wow
============================================*/
$(document).ready(function() {
    new WOW().init();
});


/* ==============================================================
              magnific-popup
http://dimsemenov.com/plugins/magnific-popup/documentation.html
================================================================*/
$('#work').magnificPopup({
  delegate: 'a', // child items selector, by clicking on it popup will open
  type: 'image',
      gallery:{
        enabled:true       //갤러리처럼 만들어라는 의미
      }
      // other options
});


/* ===========================================
                owl-carousel
============================================*/
$(document).ready(function() {
  $('#team-members').owlCarousel({
       items:3,
       autoplay:true,          /*자동으로 돌게 하는 것*/
       smartSpeed:700,         /*돌아가는 속도*/
       loop:true,               /*무한으로 계속 도는 것*/
       autoplayHoverPause:true
   });
});

$(document).ready(function() {
   $('#customers-testimonials').owlCarousel({
        items:1,
        autoplay:true,          /*자동으로 돌게 하는 것*/
        smartSpeed:700,         /*돌아가는 속도*/
        loop:true,               /*무한으로 계속 도는 것*/
        autoplayHoverPause:true
   });
});

$(document).ready(function() {
  $('#clients-list').owlCarousel({
       items:4,
       autoplay:true,          /*자동으로 돌게 하는 것*/
       smartSpeed:400,         /*돌아가는 속도*/
       loop:true,               /*무한으로 계속 도는 것*/
       autoplayHoverPause:true
   });
});


/* ===========================================
               counterUp
============================================*/

$(document).ready(function(){
    $('.counter').counterUp({
        delay: 10,
        time: 2000
    });
});

/*
//a링크를 클릭하면 팝업창에서 보여준다?
$('.gallery').each(function(){
    $(this).magnificPopup({
        delegate : 'a',
        type: 'image',
        gallery:{
            enabled:true
        }
    });
});
*/