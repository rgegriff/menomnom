function star(id){
    if(user_info.authenticated){
        $.getJSON(
            '/specials/star/',
            {'id':id}
        );
    }else{
        $("#entire_canvas").fadeIn(300);
    }
}

function setday(daycode){
    var days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday'];
    var day_class = ".day_" + days[daycode];
    $("[class^='day_']").hide();
    $(".specials_outter_box").hide();
    $('.special_header').hide();
    console.log(day_class);
    $(day_class).show();
    return false;
}

$(function(){
    $('.event_tab').click(function () {
        var $this = $(this);
        $('.event_tab').removeClass('active_event');
        $this.addClass('active_event').blur();
        return false;
    });

   // $('.event_tab:first').click();
    var id = "#day_" + extra_info.curday;
    alert(id);
    $(id).click();
})