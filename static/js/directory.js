function msgSend(){
    var data = JSON.stringify({
        message:$("form[name='mistake']").children("textarea").val()
    });
    $.ajax({
        url: '/api/mistakes/mistake/',
        type : "POST",
        data : data,
        success : function(){
            $("form[name='mistake']").hide();
            $("#msg_send_confirm").show();
            setTimeout(function(){
                $(".skinny_contact").fadeOut();
                $("#mistake_button").fadeOut();},
                3000);
        }(),
        dataType: "application/json",
        processData:  false,
        contentType: "application/json"
    });
    return false;
}

function hideAll(){
    $('.directory_outter_box').hide();
}

function shutterAll(){
    $(".directory_lower").hide();
}

function swapCats(){
    shutterAll();
    hideAll();
    var category = $(this).attr("for");
    category = '.' + category;
    $(category).show();
}

function resetCats(){
    $(".directory_outter_box").show();
}

$(function() {
    shutterAll();
    $("#directory_radio > label[name='Radio']").not(":last").click(swapCats);
    $("#directory_radio > label[name='Radio']:last").click(resetCats);
    $("form[name='mistake'] > input[name='submit']").click(msgSend);

})