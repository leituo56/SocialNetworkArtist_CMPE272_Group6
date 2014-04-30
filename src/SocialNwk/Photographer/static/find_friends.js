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

  console.log("data.results:" + data.results);

  $.each(data.results, function(i, item) {
    
    console.log("key i:" + i);
    console.log("value item:" + item);

    $.each(item, function(key, val) {
      console.log("key key:" + key);
      console.log("value val:" + val);

    });


    var html = '';
    html += '<li>';
    html += '<a href='+ photo_page_url+item.id+ '><img src="'+ item.file +'" width="190"></a>';
    html += '<p><a href='+ photo_page_url+item.id+ '> Title:'+item.title+'</a></p>';
    html += '<p><a href='+ user_url+item.author+ '> Title:'+item.authorName+'</p>';
    html += '</li>';

    console.log("html:" + html);

    // Add user HTML to the page.
    $("#firends").append(html);

    //Apply layout.
    applyLayout();
  });

  if(data.next){
    photo_list_url = data.next;
    //page++; // Increment page index for future calls.
  }else{
    //finishLoad = true;
    //$('#loadMore a').off('click');
    //$('#loadMore').html('No more photos')
  }

    
};


function applyLayout() {
  options.container.imagesLoaded(function() {
    // Create a new layout handler when images have loaded.
    handler = $('#firends li');
    handler.wookmark(options);
  });
};
