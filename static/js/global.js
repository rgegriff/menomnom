function printDay() {
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var now = new Date();
    var dayOfWeek = days[now.getDay()];

    document.write(dayOfWeek);
} // Prints day of week on the home-specials tab

function fromToday(numberOfDay) { // Prints correct days of week starting from today
    var days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    var now = new Date();
    var dayOfWeek = days[now.getDay()];
    var newList = [];
    var current = now.getDay();

    for (var i = 0; i < days.length; i++) {
        newList.push(current);
        current++;
        if (current > days.length - 1) {
            current = 0;
        }
    }

    var newListDays = [];

    for (var i = 0; i < days.length; i++) {
        if (i <= 4) {
            var twoDaysOut = i + 2;
            var dayName = days[newList[twoDaysOut]];
            newListDays.push(dayName);
        } else {
            var twoDaysOut = i - 5;
            var dayName = days[newList[twoDaysOut]];
            newListDays.push(dayName);
        }
    }

    document.write(newListDays[numberOfDay]);

}

function weekDates(whichDay) { // Retrieves month and date for upcoming week

    var now = new Date(); // today
    var nowMS = now.getTime(); // get # milliseconds for today
    var DayMS = 1000 * 60 * 60 * 24; // milliseconds in a day
    var months = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'];
    var sevenDays = [];
    var monthDates = [];
    var monthNames = [];
    var MonthAndDate = [];

    for (var i = 0; i <= 6; i++) {
        var day = DayMS * (i);
        sevenDays.push(new Date(nowMS + day));

        var monthDate = sevenDays[i].getDate();
        var monthName = months[sevenDays[i].getMonth()];
        monthNames.push(monthName);

        MonthAndDate.push(monthName + " " + monthDate);
    }

    document.write(MonthAndDate[whichDay]);

}

function weeksAway(whichWeek) { // Retrieves month and date for upcoming week

    var now = new Date(); // today
    var nowMS = now.getTime(); // get # milliseconds for today
    var DayMS = 1000 * 60 * 60 * 24; // milliseconds in a day
    var WeekMS = DayMS * 7;
    var months = ['Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.'];
    var weekThree = new Date(nowMS + (WeekMS * 2));
    var weekThreeLast = new Date(nowMS + (WeekMS * 3) - DayMS);
    var weekFour = new Date(nowMS + (WeekMS * 3));
    var weekFourLast = new Date(nowMS + (WeekMS * 4) - DayMS);
    var ThreeWeeksOut = [weekThree.getDate()];
    var ThreeWeeksLast = [weekThreeLast.getDate()];
    var FourWeeksOut = [weekFour.getDate()];
    var FourWeeksLast = [weekFourLast.getDate()];
    var MonthOut = [

        months[weekThree.getMonth()] + " " + ThreeWeeksOut,
        months[weekThreeLast.getMonth()] + " " + ThreeWeeksLast,
        months[weekFour.getMonth()] + " " + FourWeeksOut,
        months[weekFourLast.getMonth()] + " " + FourWeeksLast

    ];

    document.write(MonthOut[whichWeek]);

}

$(document).ready(function () {

    // NAVIGATION BOXES

    $('.global_link').css(
        {
            height:'85px'
        });

    $('.global_link').hover(function () {

            var $this = $(this);

            $this.children('img').animate(
                {
                    opacity:'.6'
                },
                150
            );

        },
        function () {

            var $this = $(this);

            $this.children('img').animate(
                {
                    opacity:'.25'
                },
                110
            );

        });

    $('.global_link h4').each(function () {
        var $this = $(this);
        var globalH4width = ($this.parent().width() - $this.width()) / 2;

        $this.css(
            {
                'left':globalH4width
            });
    });

    // Homepage Buttons (not logged-in)

    $('.home_page_buttons').hover(function () {

            var $this = $(this);

            $this.children('img').animate(
                {
                    opacity:'.45'
                },
                150
            );

        },
        function () {

            var $this = $(this);

            $this.children('img').animate(
                {
                    opacity:'.2'
                },
                110
            );

        });

    // Login box positioning

    function loginBox() {
        var loginWidth = ($(document).width() - $('#login_popup').width()) / 2;
        $('#login_popup').css(
            {
                'left':loginWidth
            });

        var winHeight = $(document).height();
        var winWidth = $(document).width();

        $('#entire_canvas').css(
            {
                width:winWidth,
                height:winHeight
            });
    }

    loginBox();

    $(window).resize(function () {
        loginBox();
    });

    var loginBorder = $('#login_popup').height();
    $('.border_between').css('height', loginBorder);

    $('.login_open').click(function () {
        $('#entire_canvas').fadeIn(300);
        return false;
    });

    $('.x_login').click(function () {
        $('#entire_canvas').fadeOut(300);
    });

    $('#entire_canvas').click(function () {
        if (!$('#login_popup').is(':hover')) {
            $(this).fadeOut(300);
        }
    });


    // SOCIALIZE PAGE

    $('textarea').elastic(); //Makes the textarea stretch

    $('textarea')
        .focus(function () {
            if (this.value === this.defaultValue) {
                this.value = '';
                $(this).addClass('text_black').removeClass('text_gray');
            } // End focus
        })
        .blur(function () {
            if (this.value === '') {
                this.value = this.defaultValue;
                $(this).addClass('text_gray').removeClass('text_black');
            } // End blur
        });

    $('#charsLeft').text('150'); // Sets charsLeft initially to 150

    $('#post_message').hide();

    messageBox();
    if (!window.user_info.authenticated) {
        $("#toggle_message").click(function(){
                $('#entire_canvas').fadeIn(300);
        });
    } else {
        $('#toggle_message').toggle(
            function () {
                $('#post_message').slideDown(500);
                $(this).text('Cancel message');

                $('#message_board_container').animate(
                    {
                        height:310
                    },
                    500
                ); // End animation in
            },
            function () {
                $('#post_message').slideUp(500);
                $(this).text('Post a message');
                var totalHeight = $('#community_chatter').height() - 54; // Height: Community Box - (standard header + blue bottom)

                $('#message_board_container').animate(
                    {
                        height:totalHeight
                    },
                    500
                ); // End animation in
            });
    }
    function messageBox() {

        var messageHeight = $('#post_message').height();
        var totalHeight = $('#community_chatter').height() - 54; // Height: Community Box - (standard header + blue bottom)

        var MBCheight = totalHeight - messageHeight;

        if ($('#post_message').is(':visible')) {

            $('#message_board_container').css('height', MBCheight);

        } else {

            $('#message_board_container').css('height', totalHeight);

        }

    }

    $(document).mousemove(
        function () {
            messageBox();
        });


    // HOMEPAGE

    $('.main_page_tab').click(function () {
        var $this = $(this);
        $('.main_event_panel').hide();
        $('.main_page_tab').removeClass('main_page_tab_active');
        $this.addClass('main_page_tab_active').blur();
        var panel = $this.attr('href');
        $(panel).fadeIn(200);

        if (panel == '#mainPanel2') {
            $('.specials_day_of_week').show();
        } else {
            $('.specials_day_of_week').hide();
        }

        return false;
    });

    $('.sidebar_container img').click(function () {
        $('.specials_day_of_week').hide();
        var $this = $(this);
        $('.main_event_panel').hide();
        var panel = $this.attr('href');
        $(panel).fadeIn(200);
        var titleText = $(panel).attr('title');
        $('.main_header').children('.main_sidebar_event').html(titleText + '<img src="images/x.png" />');
        $('.main_header').children('.main_sidebar_event').slideDown(150);
    });

    $('.sidebar_container').children('.sidebar_title').click(function () {
        $('.specials_day_of_week').hide();
        var $this = $(this);
        $('.main_event_panel').hide();
        var panel = $this.prev('img').attr('href');
        $(panel).fadeIn(200);
        var titleText = $(panel).attr('title');
        $('.main_header').children('.main_sidebar_event').html(titleText + '<img src="images/x.png" />');
        $('.main_header').children('.main_sidebar_event').slideDown(150);
    });

    $('.main_page_tab:first').click();

    $('.main_img_holder a').text('Remove this event');

    $('.main_img_holder a').click(
        function () {
            $(this).parent().parent().slideUp(150).parent().css('border', 'none');
            return false;
        });

    $('.main_sidebar_event').hide();

    $('.main_sidebar_event').click(function () {
        $(this).slideUp(100);
        $('.main_page_tab:first').click();
    });


    // EVENTS: Daily View
    $('.expand a').toggle(
        function () {
            $(this).parent().parent().children('.event_more_info').slideDown(350);
            $(this).text("Hide details...");
        },
        function () {
            $(this).parent().parent().children('.event_more_info').slideUp(350);
            $(this).text("Show details...");
        });

    $('.event_tab:first').click();
    $('.event_more_info').hide();
/*
    $('.event_tab').click(function () {
        var $this = $(this);
        $('.eventPanel').hide();
        $('.event_tab').removeClass('active_event');
        $this.addClass('active_event').blur();
        $('.event_tab > .event_date_box').removeClass('datebox_bg');
        $this.children().addClass('datebox_bg');
        return false;
    });





    $('.eventPanel img').click(
        function () {
            $(this).siblings('.expand').children().click();
            $(this).parent().siblings('.expand').children().click();
        });

    $('.main_event_panel img').click(
        function () {
            $(this).parent().siblings('.expand').children().click();
        });

    $('.daily_event_button').addClass('DEB_bg_inactive');

    $('.daily_event_button').toggle(
        function () {
            var $this = $(this);
            $this.css(
                {
                    'border-color':'#aaa',
                    'color':'#333'
                });
            $this.removeClass('DEB_bg_inactive');
            $this.addClass('DEB_bg_active');
            $this.text('Attending');
        },
        function () {
            var $this = $(this);
            $this.css(
                {
                    'border-color':'#ccc',
                    'color':'#666'
                });
            $this.removeClass('DEB_bg_active');
            $this.addClass('DEB_bg_inactive');
            $this.text('Attend This Event');
        });
*/
    // Directory
/*
    $('.directory_lower').hide();
*/
    $('#events_box').children().children('.directory_upper').click(

        function () {

            if ($('#events_box').children().children('.directory_upper').next('.directory_lower').is(':visible')) {
                $('#events_box').children().children('.directory_upper').next('.directory_lower').slideUp(100);
                $('#events_box').children().children('.directory_upper').removeClass('tint');
            } // Resests panels if there are any visible

            if ($(this).next('.directory_lower').is(':hidden')) {
                $(this).next('.directory_lower').slideDown(250);
                $(this).addClass('tint');
            } else {
                $(this).removeClass('tint');
                $(this).next('.directory_lower').sideUp(250);
            } // Changes current panel depending on visibility

        });

    function radioSelector(button) {


        $(button).click(function () {
            $(this).parent().children('label').css(
                {
                    backgroundColor:'#F7F7F7',
                    borderColor:'#F3F3F3'
                });
            if ($(button).is(':checked')) {
                $(this).next('label').css(
                    {
                        backgroundColor:'#cae1ea',
                        borderColor:'#adccda'
                    });
            }
        });
    } // Checks whether a button is active or not and styles accordingly

    $('#directory_radio').children().attr('name', 'Radio').each(
        function () {
            var IDname = $(this).attr('ID');
            radioSelector('#' + IDname);
        }); // Loops through all of the buttons and applies the function to each


    // Specials Page

    $('.specials_inner_box li').click(function () {
        $(this).toggleClass('specials_li_active');
    });

    // Skinny Contact

    $('.skinny_contact').hide();

    $('.standard_footer a').toggle(
        function () {
            $('.skinny_contact').slideDown(250);
            $(this).text('Cancel');
        },
        function () {
            $('.skinny_contact').slideUp(250);
            $(this).text('Notice a mistake?');
        });


    // Login Page Transitions

    $('#register').hide();

    $('.switch').toggle(function () {
            $('#login').hide()
            $('#register').slideDown(500);
            $(this).text("Click here to sign in");
        },
        function () {
            $('#register').hide();
            $('#login').slideDown(500);
            $(this).text("Click here to register");
        });

    // Submit an Event

    $('input[type="time"]').timepicker({
        timeFormat:'hh:mm TT',
        ampm:true
    });

    $('input[name="date"]').datepicker({

    });

});