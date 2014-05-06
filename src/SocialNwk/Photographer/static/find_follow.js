/**
 * Created by Xiaoli on 05/02/14.
 */
//define load handler
/*var handler = null,
    //page = 1,
    isLoading = false,
    finishLoad = false;
    countshow = false;*/

//$(document).bind('scroll', onScroll);

/*function onScroll(event) {
  // Only check when we're not still waiting for data.
  if(!isLoading && !finishLoad) {
    // Check if we're within 100 pixels of the bottom edge of the broser window.
    var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
    if(closeToBottom) {
      LoadFollowList();
    }
  }
};*/

/**
* Loads data from the API.
*/
function LoadFollowList() {
  //isLoading = true;
  $.ajax({
    type: 'GET',
    url: current_user_url, // Page parameter to make sure we load new data
    dataType: 'json',
    success: onLoadFollowList //pass get data to onLoadData function
  });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadFollowList(data) {
  //isLoading = false;

  //if(data.count != 0){
    
    //finishLoad = false;

    /*if(countshow ==false){
      $("#list_title").append("(Count: " + data.count+ ")");
      countshow=true;
    };*/

  /*
  read follows list
  */
  if(data.follows != null){

    $.each(data.follows, function(i, item) {

      var html = '';
      html += '<li id="follow_result" >';
      html += '<img id="" src="/media/'+ item.head+'"/><br/>';
      html += '<a href='+ user_url+item.user_id+ '>'+item.name+'</a>';
      html += '<h4>Favs</h4>';
      html += '<p>Make: <span id=""> '+item.fav_make+'</span></p>';
      html += '<p>Model: <span id="">'+item.fav_model +'</span></p>';
      var cat = item.fav_category;
      cat = cat.replace("_"," ");
      html += '<p>Category: <span id=""> '+cat+'</span></p>';
      html += '</li>';

      console.log("html following:" + html);

      // Add user HTML to the page.
      $("#following").append(html);

    });
  } else {
    var html = '<p> No Follows </p>';
    $("#following").append(html);
  }

  /*
  read followers list
  */
  if(data.followers != null){

    $.each(data.followers, function(i, item) {

      var html = '';
      html += '<li id="follow_result" >';
      html += '<img id="" src="/media/'+ item.head+'"/><br/>';
      html += '<a href='+ user_url+item.user_id+ '>'+item.name+'</a>';
      html += '<h4>Favs</h4>';
      html += '<p>Make: <span id=""> '+item.fav_make+'</span></p>';
      html += '<p>Model: <span id="">'+item.fav_model +'</span></p>';
      var cat = item.fav_category;
      cat = cat.replace("_"," ");
      html += '<p>Category: <span id=""> '+cat+'</span></p>';
      html += '</li>';

      console.log("html followers:" + html);

      // Add user HTML to the page.
      $("#followers").append(html);

    });
  } else {
    var html = '<p> No Followers </p>';
    $("#followers").append(html);
  }



    /*if(data.next){
      console.log("in next");
      current_user_url = data.next;
    }else{
      console.log("in no more else");
      finishLoad = true;
      countshow = false;
      $('#loadMore').html('No more users');
    };*/

  /*} else {
    console.log("in no data else");
    //finishLoad = true;
   // countshow = false;
    //$('#loadMore').html('No users like ME');
  }*/
};

function clearUsers(){
    console.log("in clear");
    $('#firends').empty();
    $('#list_title').empty();
};

