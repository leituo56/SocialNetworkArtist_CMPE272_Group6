/*
load current user info
*/

function loadUser() {

  $.ajax({
    type: 'GET',
    url: current_user_url, 
    dataType: 'json',
    success: onLoadUser //pass get data to onLoadData function
  });
};

function loadPct() {

  console.log("in pct");

  $.ajax({
    type: 'GET',
    url: current_user_url+"/stat", 
    dataType: 'json',
    success: onLoadPct //pass get data to onLoadData function
  });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadUser(data) {
  //console.log("in onloaduser");
  //console.log("data.make:" + data.fav_make);

  $("#fav_make").append("<span id='fav_tag' >" + data.fav_make+"</span>");
  $("#fav_model").append("<span id='fav_tag' >" +data.fav_model+"</span>");
  var fav = data.fav_category;
  fav = fav.replace('_',' ');
  $("#fav_category").append("<span id='fav_tag' >" +fav+"</span>");
  $("img#userhead").attr("src",data.head);
  $("#name").append("<span id='user_info_text' >" +data.name+"</span>");
  $("#gender").append("<span id='user_info_text' >" +data.gender+"</span>");
  $("#career").append("<span id='user_info_text' >" +data.career+"</span>");
  $("#about").append("<span id='user_info_text' >" +data.about+"</span>");
  $("#home_page").append("<span id='user_info_text' >" +data.home_page+"</span>");

};

function onLoadPct(data) {
  console.log("in onloadPct");
  //console.log("data.make:" + data.fav_make);

  $.each(data.make_stat, function(i, item) {
    if(i==0){
      var pct= Math.floor(item.pct*100).toFixed(1);
      $("#fav_make_pct").append(pct+ "%");
    }
  });


  $.each(data.model_stat, function(i, item) {
    if(i==0){
      var pct= Math.floor(item.pct*100).toFixed(1);
      $("#fav_model_pct").append(pct + "%");
    }
  });
  
  $.each(data.category_stat, function(i, item) {
    if(i==0){
      var pct= Math.floor(item.pct*100).toFixed(1);
      $("#fav_catagory_pct").append( pct + "%");
    }
  });




};