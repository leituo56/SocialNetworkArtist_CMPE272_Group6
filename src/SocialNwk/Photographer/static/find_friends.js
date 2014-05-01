/**
 * Created by Xiaoli on 4/26/14.
 */




/**
* Loads data from the API.
*/
function LoadUserList() {
  isLoading = true;

  console.log("in LoadUserList");
  console.log("url:"+userlist_url);

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

  console.log("data.count:" + data.count);

  if(data.count != 0){

    $.each(data.results, function(i, item) {

      var html = '';
      html += '<li>';
      html += '<a href='+ user_url+item.id+ '>'+item.username+'</a>';
      html += '<p>Fav_make: '+item.fav_make+ '   Fav_Model: '+item.fav_model+ '  Fav_Cate: '+item.fav_category+'</p>';
      html += '</li>';

      console.log("html:" + html);

      // Add user HTML to the page.
      $("#firends").append(html);

    });

    if(data.next){
      userlist_url = data.next;
      //page++; // Increment page index for future calls.
    }else{
      finishLoad = true;
      //$('#loadMore a').off('click');
      $('#loadMore').html('No more users')
    }
  } else {
    console.log("in else");
    finishLoad = true;
    $('#loadMore').html('No Match User')
  }

    
};

function clearUsers(){
    $('#friends').empty()
};

