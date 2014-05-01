/*
load current user info
*/

function loadUser() {

  //console.log("in loaduser");
  //console.log("url:"+current_user_url);

  $.ajax({
    type: 'GET',
    url: current_user_url, 
    dataType: 'json',
    success: onLoadUser //pass get data to onLoadData function
  });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadUser(data) {
  //console.log("in onloaduser");
  //console.log("data.make:" + data.fav_make);

  $("#fav_make").append(data.fav_make);
  $("#fav_model").append(data.fav_model);
  $("#fav_category").append(data.fav_category);


};