String.prototype.format = String.prototype.f = function() {
    var s = this,
        i = arguments.length;

    while (i--) {
        s = s.replace(new RegExp('\\{' + i + '\\}', 'gm'), arguments[i]);
    }
    return s;
};
var tmpl = "<div class=\"message\">" +
    "<span class='message_id' style='visibility: hidden;'>{0}</span>"+
    "<div class='top_message'>" +
    "<h1>{1}</h1>" +
    "<p>{2}</p>" +
    "</div>" +
    "<div class='bottom_message'>{3}</div>"+
    "</div>";


function getNewPosts(){
    var target = "#topofmsgs";
    var data_returned;
    var top = $(".message").find(".message_id");
    if(top.length > 0){
        var _id = parseInt(top[0].innerHTML);
    }else{
        var _id = 0;
    }
    $.getJSON('/api/message/message/', {id__gt:_id}, function(d){
        data_returned = d;
        for(var i = 0; i < d.objects.length; i++){
            var thing = d.objects[i];
            var posted = thing.posted;
            posted = new Date(posted)
            posted = posted.toString("h:mm tt")
            var que = tmpl.f(thing.id, thing.username, posted,thing.message);
            $(que).insertAfter(target).hide().fadeIn(1000)
        }
    });
}

function postMsg(){
    var msg = $('#social_post_text')[0].value;
    if (msg === "" || msg === "Type your message here... "){
        return false;
    }
    var data = JSON.stringify({
        message: $('#social_post_text')[0].value
    });

    $.ajax({
        url: '/api/message/message/',
        type: 'POST',
        contentType: 'application/json',
        data: data,
        success : function(){
            getNewPosts();
            $('#social_post_text')[0].value = "";
            $('#toggle_message')[0].click();},
        dataType: 'json',
        processData: false
    });
}
$(function(){
    window.setInterval(getNewPosts, 5000);
})