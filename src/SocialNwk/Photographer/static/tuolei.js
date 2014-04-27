/**
 * Created by leituo56 on 4/24/14.
 */
var photo_list_url = "/api/photos/"
var photo_page_url = "/photo/"
var user_url = "/user/"

var photo_lite = $("<div><a><img /></a><a /><a /></div>")
function loadPhotos(){
    $.ajax({
        type: "GET",
        url: photo_list_url,
        dataType: "json"
    }).success(function(data, textStatus, jqXHR){
        $.each(data.results, function(i, item) {
            var elem = photo_lite.clone()
            elem.find('img').attr('src', item.file);
            elem.children('a').eq(0).attr('href', photo_page_url+item.id);
            elem.children('a').eq(1).attr('href', photo_page_url+item.id).html('Title:'+item.title);
            elem.children('a').eq(2).attr('href', user_url+item.author).html('Authors:'+item.authorName);
            $("#container").append(elem);
        });
        if(data.next){
            photo_list_url = data.next;
            $('#loadMore a').off('click');
            $('#loadMore a').click(loadPhotos);
        }else{
            $('#loadMore a').off('click');
            $('#loadMore').html('No more photos')
        }
    }).fail(function( jqXHR, textStatus ) {
        alert('Request Failed');
    });
}
function clearPhotos(){
    $('#container').empty()
}
