/**
 * Created by Xiaoli on 4/26/14.
 */

/**
* Loads data from the API.
*/
/**
* Xiumei: add errorFn
*/
function errorFn(xhr){
  console.log("There was an error!" + str(xhr));
};

function loadStat() {
  //isLoading = true;

  console.log("in loadStat");
  console.log("url:" + site_stat_url);

  $.ajax({
    type: 'GET',
    url: site_stat_url, // Page parameter to make sure we load new data
    dataType: 'json',
    success: onLoadStat, //pass get data to onLoadData function
    error: errorFn,
    complete: function () {
      console.log("The request is complete");
    }
  });
} ;

/**
* convert the "val" string into percentage 
*/
function changeToPercent(val){
    var num = parseFloat(val);
    var percent = num*100;
    var showPct = percent.toFixed(1) + "%";
    return showPct;
  }

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadStat(data) {

  console.log("data.category_stat:" + data.category_stat);

  //data.make_stat - first layer of JSON key i, value item
  $.each(data.make_stat, function(i, item) {
    //second layer of JSON key key, value val 
    $.each(item, function(key, val) {
      switch(i){     
        case 0:
          if(key =="make"){
            $("#fav_make_1").append(val);
          } else if(key =="pct") {
            $("#fav_make_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="make"){
            $("#fav_make_2").append(val);
          } else if(key =="pct"){
            $("#fav_make_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="make"){
            $("#fav_make_3").append(val);
          } else if(key =="pct"){
            $("#fav_make_3_pct").append(changeToPercent(val));
          }
          break;
      }
    });
  });

  //data.model_stat - first layer of JSON key i, value item
  $.each(data.model_stat, function(i, item) {
    //second layer of JSON key key, value val 
    $.each(item, function(key, val) {      
      switch(i){     
        case 0:
          if(key =="model"){
            $("#fav_model_1").append(val);
          } else if(key =="pct"){
            $("#fav_model_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="model"){
            $("#fav_model_2").append(val);
          } else if(key =="pct"){
            $("#fav_model_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="model"){
            $("#fav_model_3").append(val);
          } else if(key =="pct"){
            $("#fav_model_3_pct").append(changeToPercent(val));
          }
          break;
      }
    });
  });

  //data.category_stat - first layer of JSON key i, value item
  $.each(data.category_stat, function(i, item) {
    //second layer of JSON key key, value val 
    $.each(item, function(key, val) {      
      switch(i){     
        case 0:
          if(key =="name"){
            $("#fav_category_1").append(val);
          } else {
            $("#fav_category_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="name"){
            $("#fav_category_2").append(val);
          } else {
            $("#fav_category_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="name"){
            $("#fav_category_3").append(val);
          } else {
            $("#fav_category_3_pct").append(changeToPercent(val));
          }
          break;
      }
    });
  }); 
}


function applyLayout() {
  options.container.imagesLoaded(function() {
    // Create a new layout handler when images have loaded.
    handler = $('#container li');
    handler.wookmark(options);
  });
};
