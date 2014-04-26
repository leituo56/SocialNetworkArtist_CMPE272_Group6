/**
 * Created by Xiaoli on 4/26/14.
 */


/**
* Refreshes the layout.
*/
function applyLayout() {
	options.container.imagesLoaded(function() {
		// Create a new layout handler when images have loaded.
		handler = $('#tiles li');
		handler.wookmark(options);
	});
};

/**
* Loads data from the API.
*/
function loadData() {
    isLoading = true;

    console.log("in loadData");

    $.ajax({
      type: 'GET',
      url: photo_list_url+'?page='+page, // Page parameter to make sure we load new data
      dataType: 'json',
      success: onLoadData //pass get data to onLoadData function
    });
};

/**
* Receives data from the API, creates HTML for images and updates the layout
*/
function onLoadData(data) {

    isLoading = false;
    //$('#loaderCircle').hide();

    console.log("page:"+ page);

    $.each(data.results, function(i, item) {
        var html = '';
        html += '<li>';
        html += '<a href='+ photo_page_url+item.id+ '><img src="'+ item.file +'" width="200"></a>';
        html += '<p><a href='+ photo_page_url+item.id+ '> Title:'+item.title+'</a></p>';
        html += '<p><a href='+ user_url+item.author+ '> Title:'+item.authorName+'</p>';
        html += '</li>';

        console.log("html:" + html);

        // Add image HTML to the page.
        $("#tiles").append(html);

        //Apply layout.
        applyLayout();
    });

    if(data.next){
        page++; // Increment page index for future calls.
    }else{
      finishLoad = true;
      //$('#loadMore a').off('click');
      $('#loadMore').html('No more photos')
    }
    
};

function clearPhotos(){
    $('#container').empty()
};

  // Capture scroll event.
  //$(document).bind('scroll', onScroll);

  // Load first data from the API.
  //loadData();
//})(jQuery);