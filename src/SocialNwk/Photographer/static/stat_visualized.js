/**
 * Created by Sammie on 5/01/14.
 * To visualized the trend statistic data with bar chart
 *<!-- Bar chart reference: http://bl.ocks.org/Caged/6476579-
 *<!-- Bar chart reference: 
 *http://jsfiddle.net/gh/get/jquery/1.9.1/highslide-software/highcharts.com/tree/master/samples/highcharts/demo/column-basic/
 */

// This function is just for testing
function statVisualize(){
  console.log("in loadStat");
  console.log("url:"+site_stat_url);
  
  $.ajax({
    type: 'GET',
    url: site_stat_url, // Page parameter to make sure we load new data
    dataType: 'json',
    success: showStatData,
     //pass get data to onLoadData function
    error: errorFn,
    complete: function (xhr, status){
      console.log("The request is complete");
    }
  });
}

// present data with bar chart
function showStatData(arg1, arg2,arg3) {
  //$(function () {
        var barData={};
        barData.chart={type: 'column'};
        
        barData.title={text: 'Camera Make Trending Rate'};
        barData.subtitle={text: ' '};
        //barData.xAxis={categories: ['Nikon', 'Canon', 'Olympas']};
        barData.xAxis={categories: arg1};
        barData.yAxis={min: 0, title:{text: 'Percent(%)'}};
        barData.tooltip={headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                        '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
                        footerFormat: '</table>',
                        shared: true,
                         useHTML: true
                       };
        barData.plotOptions={column: {pointPadding: 0.2, borderWidth: 0}};
        barData.legend={enabled: false};


        if( arg3 == "cameraMake"){
            barData.title={text: 'Top Camera Makes'};
            //barData.series=[{name: 'Camera Make', data: [41.7, 29.2, 29.2]}];
            barData.series=[{name: 'Camera Make', color: '#fbc100', data: arg2}];
            $('#visual_container1').highcharts(barData);
         } 
         else if (arg3 =="cameraModel") {
            barData.title={text: 'Top Camera Models'};
            barData.series=[{name: 'Camera Model',color: '#5bc0de', data: arg2}];
            $('#visual_container2').highcharts(barData);
         } 
         else if (arg3 == "categoryTrends"){
            barData.title={text: 'Top Photo Categories'};
            barData.series=[{name: 'Category', color: '#5bc85c', data: arg2}];
            $('#visual_container3').highcharts(barData);
         }
}
