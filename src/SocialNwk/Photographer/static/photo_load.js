/**
 * Created by Xiaoli on 4/26/14.
 */


//define load handler
  var handler = null,
      //page = 1,
      isLoading = false,
      finishLoad = false;

  // Prepare layout options.
  var options = {
    autoResize: true, // This will auto-update the layout when the browser window is resized.
    container: $('#tiles'), // Optional, used for some extra CSS styling
    offset: 2, // Optional, the distance between grid items
    itemWidth: 210 // Optional, the width of a grid item
  };

  $(document).bind('scroll', onScroll);

  /**
  * When scrolled all the way to the bottom, add more tiles.
  */
  function onScroll(event) {
    // Only check when we're not still waiting for data.
    if(!isLoading && !finishLoad) {
      // Check if we're within 100 pixels of the bottom edge of the broser window.
      var closeToBottom = ($(window).scrollTop() + $(window).height() > $(document).height() - 100);
      if(closeToBottom) {
        loadData();
      }
    }
  };


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
      url: photo_list_url, // Page parameter to make sure we load new data
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

    //console.log("page:"+ page);

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
      photo_list_url = data.next;
      //page++; // Increment page index for future calls.
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