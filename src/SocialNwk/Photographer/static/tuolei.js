/**
 * Created by leituo56 on 4/24/14.
 */
 //for loading photo on feed page

var photo_list_url = "/api/photos/"
var photo_page_url = "/photo/"
var user_url = "/user/"

var photo_lite = $("<div id='feed_photo'><a><img /></a><a /><a /></div>")
function loadPhotos(){
    $.ajax({
        type: "GET",
        url: photo_list_url,
        dataType: "json"
    }).success(function(data, textStatus, jqXHR){
        $.each(data.results, function(i, item) {
            var elem = photo_lite.clone();
            elem.find('img').attr('src', item.file);
            elem.children('a').eq(0).attr('href', photo_page_url+item.id);
            elem.children('a').eq(1).attr('href', photo_page_url+item.id).html('Title: '+item.title);
            elem.children('a').eq(2).attr('href', user_url+item.author).html('Author: '+item.authorName);
            var timestamp = new Date(item.upload_time);
            var d = timestamp.getDate();
            var m = timestamp.getMonth();
            var y = timestamp.getFullYear();
            var h = timestamp.getHours();
            var min = timestamp.getMinutes();
            //var s = timestamp.getSeconds();
            var m_names = new Array("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December");
            timestamp = m_names[m]+' '+d+', '+y+' @ '+h+':'+min;

            var html = '<br/><p>Uploaded: '+timestamp+'</p>';
            if (item.portrait) {
                html+='<img id="categories" src="/static/images/portrait_yellow.png"/>';
              }
              if (item.landscape) {
                html+='<img id="categories" src="/static/images/landscape_yellow.png"/>'; 
              }
              if (item.telephoto) {
                html+='<img id="categories" src="/static/images/telephoto_yellow.png"/>'; 
              }
              if (item.low_light) {
                html+='<img id="categories" src="/static/images/lowlight_yellow.png"/>'; 
              }
              if (item.high_speed) {
                html+='<img id="categories" src="/static/images/highspeed_yellow.png"/>'; 
              }
              if (item.long_exposure) {
                html+='<img id="categories" src="/static/images/longexposure_yellow.png"/>'; 
              }
            elem.append(html);
            //elem = elem.replace('</div>',html3);
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
