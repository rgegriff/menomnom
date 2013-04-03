function loadevents(){
    var url = $(this).attr('href');

    $('#event_containment_field').load(url, complete=function(){
        $(".daily_event_button").click(attend);
        $('.event_more_info').hide();

        $('.expand a').toggle(
            function () {
                $(this).parent().parent().children('.event_more_info').slideDown(350);
                $(this).text("Hide details...");
            },
            function () {
                $(this).parent().parent().children('.event_more_info').slideUp(350);
                $(this).text("Show details...");
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

    });

    return false;
}
function attend(){
    if(user_info.authenticated){
        var id = $(this).parent().parent().find(".id_holder").text()
        $.getJSON(
            '/events/attend/',
            {'id':id}
        );

        console.log(($(this).filter('.DEB_bg_inactive')));

        if($(this).is('.DEB_bg_inactive')){
            $(this).css(
                {
                    'border-color':'#aaa',
                    'color':'#333'
                });
            $(this).removeClass('DEB_bg_inactive');
            $(this).addClass('DEB_bg_active');
            $(this).text('Attending');
            $(this).siblings().find(".count")[0].innerHTML = parseInt( $(this).siblings().find(".count")[0].innerHTML ) + 1

        }else{
            $(this).css(
                {
                    'border-color':'#ccc',
                    'color':'#666'
                });
            $(this).removeClass('DEB_bg_active');
            $(this).addClass('DEB_bg_inactive');
            $(this).text('Attend This Event');
            $(this).siblings().find(".count")[0].innerHTML = parseInt( $(this).siblings().find(".count")[0].innerHTML ) - 1

        }
    }else{
        $("#entire_canvas").fadeIn(300);
    }
    return $(this);
}

$(function(){
    $('.event_tab').click(function () {
        var $this = $(this);
        $('.event_tab').removeClass('active_event');
        $this.addClass('active_event').blur();
        $('.event_tab > .event_date_box').removeClass('datebox_bg');
        $this.children().addClass('datebox_bg');
        return false;
    });

    $('.weekly_event_tab').click(function () {
        var $this = $(this);
        $('.weekly_event_tab').removeClass('weekly_active_event');
        $this.addClass('weekly_active_event').blur();
        return false;
    });

    $('.weekly_event_tab').click
    $(".main_header > a").click(loadevents);
    $(".main_header > a:first").click();
    $(".daily_event_button").click(attend)
    $('.event_more_info').hide();

    $('.expand a').toggle(
        function () {
            $(this).parent().parent().children('.event_more_info').slideDown(350);
            $(this).text("Hide details...");
        },
        function () {
            $(this).parent().parent().children('.event_more_info').slideUp(350);
            $(this).text("Show details...");
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
});