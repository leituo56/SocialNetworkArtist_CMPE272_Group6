/**
 * Created by Xiaoli on 4/26/14.
 */

/**
* Loads data from the API.
*/
function loadStat() {
  //isLoading = true;

  console.log("in loadStat");
  console.log("url:"+site_stat_url);

  $.ajax({
    type: 'GET',
    url: site_stat_url, // Page parameter to make sure we load new data
    dataType: 'json',
    success: onLoadStat //pass get data to onLoadData function
  });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadStat(data) {

  console.log("data.category_stat:" + data.category_stat);

  //data.category_stat - first layer of JSON key i, value item
  $.each(data.category_stat, function(i, item) {

    console.log("key i:" + i);

    //second layer of JSON key key, value val 
    $.each(item, function(key, val) {

      console.log("key in i:" + i);

      console.log("key key:" + key);
      console.log("value val:" + val);
      
      switch(i){

        //console.log("in switch:" + i);
        case 1:
          $("#fav_category_1").text = val;
          break;
        case 2:
          $("#fav_category_2").text = val;
          break;
        case 3:
          $("#fav_category_3").text = val;
          break;
      }


    });


    /*var html = '';
    html += '<li>';
    html += '<a href='+ photo_page_url+item.id+ '><img src="'+ item.file +'" width="190"></a>';
    html += '<p><a href='+ photo_page_url+item.id+ '> Title:'+item.title+'</a></p>';
    html += '<p><a href='+ user_url+item.author+ '> Title:'+item.authorName+'</p>';
    html += '</li>';

    console.log("html:" + html);*/

    // Add image HTML to the page.
    //$("#container").append(html);

    //Apply layout.
    //applyLayout();
  });


    
};


function applyLayout() {
  options.container.imagesLoaded(function() {
    // Create a new layout handler when images have loaded.
    handler = $('#container li');
    handler.wookmark(options);
  });
};
