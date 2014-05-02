/**
 * Created by Xiaoli on 4/26/14.
 */
//define load handler
var handler = null,
    //page = 1,
    isLoading = false,
    finishLoad = false;
    countshow = false;

$(document).bind('scroll', onScroll);

function onScroll(event) {
  // Only check when we're not still waiting for data.
  if(!isLoading && !finishLoad) {
    // Check if we're within 100 pixels of the bottom edge of the broser window.
    var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
    if(closeToBottom) {
      LoadUserList();
    }
  }
};

/**
* Loads data from the API.
*/
function LoadUserList() {
  isLoading = true;
  $.ajax({
    type: 'GET',
    url: userlist_url, // Page parameter to make sure we load new data
    dataType: 'json',
    success: onLoadUserList //pass get data to onLoadData function
  });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadUserList(data) {
  isLoading = false;

  if(data.count != 0){
    
    finishLoad = false;

    if(countshow ==false){
      $("#list_title").append("( Count: " + data.count+ ")");
      countshow=true;
    };

    $.each(data.results, function(i, item) {

      var html = '';
      html += '<li id="find_friend" >';
      html += '<img id="find_head" src="'+ item.head+'"/>';
      html += '<a href='+ user_url+item.id+ '>'+item.username+'</a>';
      html += '<p> Fav_make: <span id="find_fav"> '+item.fav_make+'</span></p>';
      html += '<p> Fav_Model: <span id="find_fav">'+item.fav_model +'</span></p>';
      html += '<p> Fav_Category: <span id="find_fav"> '+item.fav_category+'</span></p>';
      html += '</li>';

      console.log("html:" + html);

      // Add user HTML to the page.
      $("#firends").append(html);

    });

    if(data.next){
      console.log("in next");
      userlist_url = data.next;
    }else{
      console.log("in no more else");
      finishLoad = true;
      countshow = false;
      $('#loadMore').html('No more users');
    };

  } else {
    console.log("in no data else");
    finishLoad = true;
    countshow = false;
    $('#loadMore').html('No Match User');
  }
};

function clearUsers(){
    console.log("in clear");
    $('#firends').empty();
    $('#list_title').empty();
};

