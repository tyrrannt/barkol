"use strict";

$(window).load(function() {
   $("#rq-circle-loader-wrapper").fadeOut(500);
});

$(document).ready(function(){

    // Mobile MaxHeight Issue Fixing
    $(".navbar-collapse").css({ maxHeight: $(window).height() - $(".navbar-header").height() + "px" });

    // Owl Carousal
    $(".rq-owl-carousel-content .owl-carousel").owlCarousel({
        autoplay: true,
        loop: true,
        autoplayTimeout: 4000,
        // nav: true,
        items : 1,
        itemsDesktop : [1199,1],
        itemsDesktopSmall : [979,1]
    });

    $(".rq-testimonial-owl-carousel .owl-carousel").owlCarousel({
        autoplay: true,
        loop: true,
        // autoplayTimeout: 1000,
        // nav: true,
        iresponsiveClass:true,
        responsive:{
            0:{
                items:1,
                nav:false,
                loop:true
            },
            480:{
                items:2,
                nav:false,
                loop:true
            },
            600:{
                items:3,
                nav:false,
                loop:true
            },
            1000:{
                items:5,
                nav:false,
                loop:true
            }
        }
    });

    //language select2
    function languageFlag (language) {
        if (!language.id) { return language.text; }
        var $language = $(
            '<span>' + language.text + '<span class="rq-flag-wrapper"><img src="img/flags/' + language.element.value.toLowerCase() + '.png" class="img-flag" /></span></span>'
        );
        return $language;
    };

    $(".rq-language .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        dropdownCssClass: "rq-lang-dropdown",
        templateResult: languageFlag,
        templateSelection: languageFlag,
    });

    // $(".rq-select-single .js-example-placeholder-single").select2({
    //     minimumResultsForSearch: Infinity,
    //     placeholder: "Select a state",
    // });

    $(".rq-room-type .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Room Type",
    });

    $(".rq-adult-person .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Adult",
    });

    $(".rq-children-num .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Children",
    });

    // Parallax
    $('.rq-slider-area.parallax-window').parallax(); 

    $(".rq-checkout-country .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Select Your Country",
    });

    $(".rq-checkout-district .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Select Your State",
    });

    $(".rq-total .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Number of Room",
    });

    $(".rq-adult .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Number"
    });


    $(".rq-children .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Number"
    });


    $(".singleRoom-grid-upper-right-date .js-example-placeholder-single").select2({
        minimumResultsForSearch: Infinity,
        placeholder: "Date"
    });

    // Coming Soon Count down
    $('.rq-countdown #example').countdown({
        date: '07/24/2016 23:59:59'
    });

    // Jquery UI Slider
    $( ".rq-ui-slider #slider-range" ).slider({
        range: true,
        min: 0,
        max: 2000,
        values: [ 50, 2000 ],
        slide: function( event, ui ) {
        $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
        }
        });
        $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) +
        " - $" + $( "#slider-range" ).slider( "values", 1 ) );

        // Grid & List View
        $('.rq-grid-list-view-option').on('click', 'a', function (e) {
            e.preventDefault();
            const item = $(this);
            const dataClass = item.data('class');
            item.siblings().removeClass('active');
            const row = $('.rq-listing-choose');

            if (dataClass === 'singleRoom-list-main') {
                row.removeClass('singleRoom-grid-main').addClass(dataClass);
            } else {
                row.removeClass('singleRoom-list-main').addClass(dataClass);
            }
            item.addClass('active');
        });

        // Raty Js
        $('.rq-service-rating').raty({
            // readOnly:  true,
            cancel: false,
            starType: 'i',
            half:  true,
            start:     0
        });

        $('input').iCheck({
            checkboxClass: 'icheckbox_square-red',
            radioClass: 'iradio_square-red',
            increaseArea: '20%' // optional
        });


/* ****************************************
        Isotope
**************************************** */
// ISOTOPE
var $packageLayout = $('.rq-room-package-wrapper');

$packageLayout.imagesLoaded(function(){
  $packageLayout.isotope({
    itemSelector: '.rq-room-package',
    percentPosition: true,
    masonry: {
      // use outer width of grid-sizer for columnWidth
      columnWidth: 1
    }
  });
});

/* ****************************************
        Magnific Popup
**************************************** */
$('.popup-vimeo').magnificPopup({
    // disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 300,
    preloader: false,

    fixedContentPos: false
});

/* ********************************************
Date
******************************************** */
// Date Picker
var $rqCheckIn = $('#rq-check-in'),
      $rqCheckInSingle = $('#rq-check-in-single'),
      $rqCheckInTime = $('#rq-check-in-time'),
      $rqCheckInFilter = $(' #rq-check-in-filter'),
      $rqCheckOut = $('#rq-check-out'),
      $rqCheckOutSingle = $('#rq-check-out-single'),
      $rqCheckOutTime = $('#rq-check-out-time'),
      $rqCheckOutFilter = $('#rq-check-out-filter'),
      monthName = [
        "January",
        "February",
        "March",
         "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
      ];

// Current Date
(function() {
    var cDate = new Date();
    $rqCheckIn.find(".rq-single-date").html(cDate.getDate());
    $rqCheckIn.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));
    $rqCheckIn.find(".rq-single-year").html(cDate.getFullYear().toString().substr(2,2));

    $rqCheckInSingle.find(".rq-single-date").html(cDate.getDate());
    $rqCheckInSingle.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));

    $rqCheckInFilter.find(".rq-single-date").html(cDate.getDate());
    $rqCheckInFilter.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));
    $rqCheckInFilter.find(".rq-single-year").html(cDate.getFullYear().toString().substr(2,2));
})();

// Next Day
(function() {
    var cDate = new Date();
    // $rqCheckOut.find(".rq-single-date").html(cDate.getDate()+1);
    $rqCheckOut.find(".rq-single-date").html(cDate.getDate());
    $rqCheckOut.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));
    $rqCheckOut.find(".rq-single-year").html(cDate.getFullYear().toString().substr(2,2));

    // $rqCheckOutSingle.find(".rq-single-date").html(cDate.getDate()+1);
    $rqCheckOutSingle.find(".rq-single-date").html(cDate.getDate());
    $rqCheckOutSingle.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));

    // $rqCheckOutFilter.find(".rq-single-date").html(cDate.getDate()+1);
    $rqCheckOutFilter.find(".rq-single-date").html(cDate.getDate());
    $rqCheckOutFilter.find(".rq-single-month").html(monthName[cDate.getMonth()].toString().substr(0,3));
    $rqCheckOutFilter.find(".rq-single-year").html(cDate.getFullYear().toString().substr(2,2));
})();

// Check In Date
$rqCheckIn.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           maxDate: $('#rq-check-out').val()?$('#rq-check-out').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckIn.datetimepicker('getValue');
        $rqCheckIn.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckIn.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckIn.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});

// Check In Single Date
$rqCheckInSingle.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           maxDate: $('#rq-check-out-single').val()?$('#rq-check-out-single').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckInSingle.datetimepicker('getValue');

        $rqCheckInSingle.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckInSingle.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckInSingle.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});

// Check In Filter
$rqCheckInFilter.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           maxDate: $('#rq-check-out-filter').val()?$('#rq-check-out-filter').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckInFilter.datetimepicker('getValue');
        $rqCheckInFilter.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckInFilter.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckInFilter.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});

// Check Out Date
$rqCheckOut.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           minDate: $('#rq-check-in').val()?$('#rq-check-in').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckOut.datetimepicker('getValue');
        $rqCheckOut.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckOut.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckOut.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});

// Check Out Single
$rqCheckOutSingle.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           minDate: $('#rq-check-in-single').val()?$('#rq-check-in-single').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckOutSingle.datetimepicker('getValue');

        $rqCheckOutSingle.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckOutSingle.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckOutSingle.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});

// Check Out Filter
$rqCheckOutFilter.datetimepicker({
    timepicker:false,
    minDate:0,
    scrollMonth: false,
    onShow:function( ct ){
       this.setOptions({
           minDate: $('#rq-check-in-filter').val()?$('#rq-check-in-filter').val():false
       })
    },
    onChangeDateTime:function(){
        var datePickerDate = $rqCheckOutFilter.datetimepicker('getValue');
        $rqCheckOutFilter.find(".rq-single-date").html(datePickerDate.getDate());
        $rqCheckOutFilter.find(".rq-single-month").html(monthName[datePickerDate.getMonth()].toString().substr(0,3));
        $rqCheckOutFilter.find(".rq-single-year").html(datePickerDate.getFullYear().toString().substr(2,2));
    }
});



/* ********************************************
Time
******************************************** */
// Check In Time
$rqCheckOutTime.datetimepicker({
    timepicker:true,
    datepicker:false,
    format:'H:i',

    onChangeDateTime:function(){
        var datePickerTime = $rqCheckOutTime.datetimepicker('getValue'),
              getHours = ('0'+datePickerTime.getHours()).slice(-2),
              getMins = ('0'+datePickerTime.getMinutes()).slice(-2);

        $rqCheckOutTime.find(".rq-checkout-time").html(getHours + ":" + getMins);
    }
});

// Check In Time
$rqCheckInTime.datetimepicker({
    timepicker:true,
    datepicker:false,
    format:'H:i',

    onChangeDateTime:function(){
        var datePickerTime = $rqCheckInTime.datetimepicker('getValue'),
              getHours = ('0'+datePickerTime.getHours()).slice(-2),
              getMins = ('0'+datePickerTime.getMinutes()).slice(-2);

        $rqCheckInTime.find(".rq-checkin-time").html(getHours + ":" + getMins);
    }
});



// $('button.somebutton').on('click', function () {
//     var d = $('#input').datetimepicker('getValue');
//     console.log(d.getFullYear());
// });
        

});

    // Flex Slider
    $(window).load(function() {
        // The slider being synced must be initialized first
        $('.rq-flex-slider #carousel').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            // itemWidth: 210,
            itemWidth: 125,
            itemMargin: 6,
            asNavFor: '#slider'
        });

        $('.rq-flex-slider #slider').flexslider({
            animation: "slide",
            controlNav: false,
            animationLoop: false,
            slideshow: false,
            sync: "#carousel"
        });
    });


// RIght side menu
(function() {

    var bodyEl = document.body,
        content = document.querySelector( 'body' ),
        openbtn = document.getElementById( 'rq-side-menu-btn' ),
        closebtn = document.getElementById( 'rq-side-menu-close-button' ),
        isOpen = false;

    function init() {
        initEvents();
    }

    function initEvents() {
        openbtn.addEventListener( 'click', toggleMenu );
        if( closebtn ) {
            closebtn.addEventListener( 'click', toggleMenu );
        }

        // close the menu element if the target it´s not the menu element or one of its descendants..
        // content.addEventListener( 'click', function(ev) {
        //     var target = ev.target;
        //     if( isOpen && target !== openbtn ) {
        //         toggleMenu();
        //     }
        // } );
    }

    function toggleMenu() {
        if( isOpen ) {
            classie.remove( bodyEl, 'rq-show-menu' );
        }
        else {
            classie.add( bodyEl, 'rq-show-menu' );
        }
        isOpen = !isOpen;
    }

    init();

})();