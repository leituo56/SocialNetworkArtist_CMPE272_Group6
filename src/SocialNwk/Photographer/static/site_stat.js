/**
 * Created by Xiaoli on 4/26/14.
      add pie chart 05/03/14
 */

/**
* Loads data from the API.
*/
/**
* Xiumei: add errorFn
*/

//pie_arrays
var makes=[];
var make_pcts=[];

var models=[];
var models_pcts=[];


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
      loadMakePie();
      loadModelPie();
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
      console.log("key:"+key);
      switch(i){     
        case 0:
          if(key =="make"){
            makes.push(val);
            $("#fav_make_1").append(val);
          } else if(key =="pct") {
            make_pcts.push(val);
            $("#fav_make_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="make"){
            makes.push(val);
            $("#fav_make_2").append(val);
          } else if(key =="pct"){
            make_pcts.push(val);
            $("#fav_make_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="make"){
            makes.push(val);
            $("#fav_make_3").append(val);
          } else if(key =="pct"){
            make_pcts.push(val);
            $("#fav_make_3_pct").append(changeToPercent(val));
          }
          break;
        default:
          if(key =="make"){
            makes.push(val);
          } else if(key =="pct"){
            make_pcts.push(val);
          }
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
            models.push(val);
            $("#fav_model_1").append(val);
          } else if(key =="pct"){
            models_pcts.push(val);
            $("#fav_model_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="model"){
            models.push(val);
            $("#fav_model_2").append(val);
          } else if(key =="pct"){
            models_pcts.push(val);
            $("#fav_model_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="model"){
            models.push(val);
            $("#fav_model_3").append(val);
          } else if(key =="pct"){
            models_pcts.push(val);
            $("#fav_model_3_pct").append(changeToPercent(val));
          }
          break;
        default:
          if(key =="model"){
            models.push(val);
          } else if(key =="pct"){
            models_pcts.push(val);
          }
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
            //replace underscores with spaces
            var val1 = val.replace("_"," ");
            $("#fav_category_1").append(val1);
          } else {
            $("#fav_category_1_pct").append(changeToPercent(val));
          }
          break;
        case 1:
          if(key =="name"){
            //replace underscores with spaces
            var val1 = val.replace("_"," ");
            $("#fav_category_2").append(val1);
          } else {
            $("#fav_category_2_pct").append(changeToPercent(val));
          }
          break;
        case 2:
          if(key =="name"){
            //replace underscores with spaces
            var val1 = val.replace("_"," ");
            $("#fav_category_3").append(val1);
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

/************Pie chart for make*****************/

function loadMakePie(){

  console.log("in load pie");

  var svg = d3.select("div#make_pie")
    .append("svg")
    .append("g")

  svg.append("g")
    .attr("class", "slices");
  svg.append("g")
    .attr("class", "labels");
  svg.append("g")
    .attr("class", "lines");

  var width = 960,
      height = 450,
    radius = Math.min(width, height) / 2;

  var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) {
      return d.value;
    });

  var arc = d3.svg.arc()
    .outerRadius(radius * 0.8)
    .innerRadius(radius * 0.4);

  var outerArc = d3.svg.arc()
    .innerRadius(radius * 0.9)
    .outerRadius(radius * 0.9);

  svg.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  var key = function(d){ return d.data.label; };

  //make pie
  var make_color = d3.scale.ordinal()
    .domain(makes)
    .range(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

  function loadMakePieData(){
    var labels = make_color.domain();
    var i=0;
    return labels.map(function(label){
        return { label: label, value:make_pcts[i++] }
    });
  }

  change(loadMakePieData());

  d3.select(".randomize")
    .on("click", function(){
      change(randomData());
    });


  function change(data) {

    /* ------- PIE SLICES -------*/
    var slice = svg.select(".slices").selectAll("path.slice")
      .data(pie(data), key);

    slice.enter()
      .insert("path")
      .style("fill", function(d) { return make_color(d.data.label); })
      .attr("class", "slice");

    slice   
      .transition().duration(1000)
      .attrTween("d", function(d) {
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          return arc(interpolate(t));
        };
      })

    slice.exit()
      .remove();

    /* ------- TEXT LABELS -------*/

    var text = svg.select(".labels").selectAll("text")
      .data(pie(data), key);

    text.enter()
      .append("text")
      .attr("dy", ".35em")
      .text(function(d) {
        return d.data.label;
      });
    
    function midAngle(d){
      return d.startAngle + (d.endAngle - d.startAngle)/2;
    }

    text.transition().duration(1000)
      .attrTween("transform", function(d) {
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          var pos = outerArc.centroid(d2);
          pos[0] = radius * (midAngle(d2) < Math.PI ? 1 : -1);
          return "translate("+ pos +")";
        };
      })
      .styleTween("text-anchor", function(d){
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          return midAngle(d2) < Math.PI ? "start":"end";
        };
      });

    text.exit()
      .remove();

    /* ------- SLICE TO TEXT POLYLINES -------*/

    var polyline = svg.select(".lines").selectAll("polyline")
      .data(pie(data), key);
    
    polyline.enter()
      .append("polyline");

    polyline.transition().duration(1000)
      .attrTween("points", function(d){
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          var pos = outerArc.centroid(d2);
          pos[0] = radius * 0.95 * (midAngle(d2) < Math.PI ? 1 : -1);
          return [arc.centroid(d2), outerArc.centroid(d2), pos];
        };      
      });
    
    polyline.exit()
      .remove();
  };
}

/************Pie chart for Model *****************/

function loadModelPie(){

  console.log("in load pie");

  var svg = d3.select("div#model_pie")
    .append("svg")
    .append("g")

  svg.append("g")
    .attr("class", "slices");
  svg.append("g")
    .attr("class", "labels");
  svg.append("g")
    .attr("class", "lines");

  var width = 960,
      height = 450,
    radius = Math.min(width, height) / 2;

  var pie = d3.layout.pie()
    .sort(null)
    .value(function(d) {
      return d.value;
    });

  var arc = d3.svg.arc()
    .outerRadius(radius * 0.8)
    .innerRadius(radius * 0.4);

  var outerArc = d3.svg.arc()
    .innerRadius(radius * 0.9)
    .outerRadius(radius * 0.9);

  svg.attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  var key = function(d){ return d.data.label; };

  //model pie
  var model_color = d3.scale.ordinal()
    .domain(models)
    .range(["#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

  //load model data
  function loadmodelPieData(){
      
    var labels = model_color.domain();
    var i=0;
    
    return labels.map(function(label){    
          return { label: label, value: models_pcts[i++]}
    });
  }



  change(loadmodelPieData());

  //apply data to pie
  function change(data) {

    /* ------- PIE SLICES -------*/
    var slice = svg.select(".slices").selectAll("path.slice")
      .data(pie(data), key);

    slice.enter()
      .insert("path")
      .style("fill", function(d) { return model_color(d.data.label); })
      .attr("class", "slice");

    slice   
      .transition().duration(1000)
      .attrTween("d", function(d) {
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          return arc(interpolate(t));
        };
      })

    slice.exit()
      .remove();

    /* ------- TEXT LABELS -------*/

    var text = svg.select(".labels").selectAll("text")
      .data(pie(data), key);

    text.enter()
      .append("text")
      .attr("dy", ".35em")
      .text(function(d) {
        return d.data.label;
      });
    
    function midAngle(d){
      return d.startAngle + (d.endAngle - d.startAngle)/2;
    }

    text.transition().duration(1000)
      .attrTween("transform", function(d) {
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          var pos = outerArc.centroid(d2);
          pos[0] = radius * (midAngle(d2) < Math.PI ? 1 : -1);
          return "translate("+ pos +")";
        };
      })
      .styleTween("text-anchor", function(d){
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          return midAngle(d2) < Math.PI ? "start":"end";
        };
      });

    text.exit()
      .remove();

    /* ------- SLICE TO TEXT POLYLINES -------*/

    var polyline = svg.select(".lines").selectAll("polyline")
      .data(pie(data), key);
    
    polyline.enter()
      .append("polyline");

    polyline.transition().duration(1000)
      .attrTween("points", function(d){
        this._current = this._current || d;
        var interpolate = d3.interpolate(this._current, d);
        this._current = interpolate(0);
        return function(t) {
          var d2 = interpolate(t);
          var pos = outerArc.centroid(d2);
          pos[0] = radius * 0.95 * (midAngle(d2) < Math.PI ? 1 : -1);
          return [arc.centroid(d2), outerArc.centroid(d2), pos];
        };      
      });
    
    polyline.exit()
      .remove();
  };
}


