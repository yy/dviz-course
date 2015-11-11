# W12 Lab Assignment

Data binding and maps.

Submit `W12Lab.html` to Canvas.

## Setup

Create a folder named `W12Lab` on the Desktop and set it as the root for the server:

`python -m SimpleHTTPServer`

or

`python -m http.server`

The defualt port number is 8000.

Then create a skeleton html file called `W12Lab.html`.
```html
<!DOCTYPE html>
<html>
<head>
<title>W12 Lab</title>
</head>

<body>
<script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>

<h1 align="center">W12 Lab Assignment</h1>

<h2>Data Binding</h2>

<div id="data_binding">
</div>

<hr>

<h2>Maps</h2>

<h3>US Land</h3>

<div id="us_land">
</div>

<hr>

<h3>US States</h3>

<div id="us_states">
</div>

<hr>

<h3>US Counties</h3>

<div id="us_counties">
</div>

<hr>

<h3>US States with Names</h3>

<div id="us_states_names">
</div>

<hr>

<h3>Choropleths</h3>

<div id="choropleths">
</div>

<hr>

</body>
</html>
```

## Data Binding

In the previous lab, we manually created a horizontal bar chart by hardcoding the width of each bar proportional to each value in the `data` variable. Or you may have used a `for` loop to make it a bit easier. But there is a more "D3-style" way to do this, using D3' `enter()` selection. Recommend to read [this](http://bost.ocks.org/mike/join/).

For example, to create a bar chart:

```javascript
<script type="text/javascript">
var data = [43, 27, 18, 9, 2];

var svg = d3.select("#data_binding")
    .append("svg")
    .attr("width", 500)
    .attr("height",150);

svg.selectAll("rect")
    .data(data).enter()
    .append("rect")
    .attr("height", 23)
    .attr("width", function(d) {return 10*d;})
    .attr("x", 0)
    .attr("y", function(d, i) {return 25*i;})
    .attr("fill", "DarkGray");
</script>
```

The variable `svg` is the canvas on which we want to draw the bar chart. `svg.selectAll("rect")` returns an empty selection. Nothing will happen at this time because there is no `rect` elements, but this will tell D3 that we want to draw some rectangles. `svg.selectAll("rect").data(data)` is to bind the empty selection with the `data` variable. Then, calling the `.enter()` function will create a placeholder for each new datum. But there is no actual shape there. So we call `.append("rect")` to append a actual rectangle. Finally, we need to specify where to start to draw the rectangle (`x` and `y`) and the width and height of the rectangle. The height of each rectangle is a constant `23`. For the width, the `attr()` function pass the data that is bound to the rectangle to the function `function(d) {return 10*d;}`. The returned value of this function is then used to set the width of the rectangle. D3 will also magically set the value of `i` as the i-th rectangle, so that we can easily set the `y` attributes (there is a (25-23)px gap between bars).

We can put these code into console (in the skeleton webpage `W12Lab.html`, right click and select "Inspect Element" and choose "Console") to see what is happening.

**TODO**:

- Can you label the width of each bar using in the data binding way?

## Maps

Since we will create several maps, we can put all the code for each map in a function. [JavaScript Closures](http://www.w3schools.com/js/js_function_closures.asp).

```javascript
<script type="text/javascript">
(function() {
  // put the code here for each map 
})();
</script>
```

## US Land

Let's first create a map for the US land. Go to <http://bl.ocks.org/mbostock/raw/4090846/us.json> to see what a [TopoJSON](https://github.com/mbostock/topojson/wiki) format for the US map looks like, and save the file to the `W12Lab` folder.

To reference TopoJSON:

```javascript
<script src="//d3js.org/topojson.v1.min.js"></script>
```

To draw this:

```javascript
var path = d3.geo.path();

var svg = d3.select("#us_land").append("svg")
    .attr("width", 900)
    .attr("height", 600);

d3.json("us.json", function(error, us) {
  if (error) return console.error(error);
  console.log(us);

  svg.append("path")
      .datum(topojson.feature(us, us.objects.land))
      .attr("d", path)
      .attr("fill", "LightGray")
      .attr("stroke", "White");
});
```

First, [**`d3.json()`**](https://github.com/mbostock/d3/wiki/Requests) is a _callback_ function, which means that while the file `us.json` is being loaded, the rest of the webpage can still be displayed, so that we don't have to wait for a long time to display the whole webpage. This is the _asynchronous_ way of loading data. When the file is ready, the function `function(error, us)` will be called, and we can put the visualization code inside the function. `console.log(us)` will print the obejct `us`, and all the contents of the `us.json` file can be accessed through this variable.

`var path = d3.geo.path()` is used to define a new geographic path generator. See [Geo Paths](https://github.com/mbostock/d3/wiki/Geo-Paths). [**`topojson.feature()`**](https://github.com/mbostock/topojson/wiki/API-Reference#feature) is a function that returns all the features for the specified object (`us.objects.land`) in the given TopoJSON object (`us`). The [**`d`**](https://developer.mozilla.org/en-US/docs/Web/SVG/Attribute/d) attribute is a string that contains a series of path descriptions, which will be generated by the `path` generator. `datum()` is used to bind data to a single element.

Go to the Console and see what other objects under `us.objects`.

## US States

There are also information for states, so let's display them:

```javascript
var projection = d3.geo.albersUsa()
    .scale(1000)
    .translate([900/2, 600/2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("#us_states").append("svg")
    .attr("width", 900)
    .attr("height", 600);

d3.json("us.json", function(error, us) {
  if (error) return console.error(error);
  console.log(us);

  svg.selectAll("path")
      .data(topojson.feature(us, us.objects.states).features)
      .enter()
      .append("path")
      .attr("d", path)
      .attr("fill", "LightGray")
      .attr("stroke", "White");
});
```

One important change is adding projections. [**`.projection()`**](https://github.com/mbostock/d3/wiki/Geo-Paths#path_projection) specifies the projection function used by the path generator. We use the [**`albersUsa`**](https://github.com/mbostock/d3/wiki/Geo-Projections#albersUsa) projection. For other projections, see [here](https://github.com/mbostock/d3/wiki/Geo-Projections). Change the values for [**`scale()`**](https://github.com/mbostock/d3/wiki/Geo-Projections#scale) and [**`translate()`**](https://github.com/mbostock/d3/wiki/Geo-Projections#translate) and think about what they mean.

## US Counties

**TODO**

- Since there are county information in the `us.json` file, can you also make a county level map?
- Try to add some interactive features to the map. For instance, change the color of a county when mouse hovers this county.

## US States with Names

In the `us.json` file, we have ID for each state. Luckily we can also get the state name and code information from [here](https://gist.github.com/mbostock/4090846#file-us-state-names-tsv). Download the file to the `W12Lab` folder. 

Let's show the state code on the US states map:

```javascript
var projection = d3.geo.albersUsa()
    .scale(1000)
    .translate([900/2, 600/2]);

var path = d3.geo.path()
    .projection(projection);

var svg = d3.select("#us_states_names").append("svg")
    .attr("width", 900)
    .attr("height", 600);

var names = {};

queue()
  .defer(d3.json, "us.json")
  .defer(d3.tsv, "us-state-names.tsv", function(d) {names[d.id] = d.code;})
  .await(ready);

function ready(error, us) {
  if (error) return console.error(error);
  console.log(us);
  console.log(names);

  svg.selectAll("path")
      .data(topojson.feature(us, us.objects.states).features)
      .enter()
      .append("path")
      .attr("d", path)
      .attr("fill", "LightGray")
      .attr("stroke", "White");

  svg.selectAll("text")
      .data(topojson.feature(us, us.objects.states).features)
      .enter()
      .append("text")
      .text(function(d) {return names[d.id];})
      .attr("x", function(d) {return path.centroid(d)[0];})
      .attr("y", function(d) {return path.centroid(d)[1];})
      .attr("text-anchor","middle")
      .attr('fill', 'Black');
}
```

Everything looks very familiar. The biggest change is now we don't use the callback function `d3.json()`. Instead, we use [queue.js](http://bl.ocks.org/mbostock/1696080) to load multiple files. And we use a map (`names`) to store state ID and state code (`names[d.id] = d.code`). So we can get the code of a state and then display it when we have its ID (`.text(function(d) {return names[d.id];})`).

**TODO** (optional)

- Some state codes in the northeastern part are not clearly showed. Can you change them by labeling the code text in other places, like [this](https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations#Postal_codes)?

## Choropleths

See the example [here](http://bl.ocks.org/mbostock/4060606). The code there should also look very familiar. You can also use other color schemes provided by [Color Brewer](http://colorbrewer2.org/).

### Direct SVG manipulation

It is possible to create choropleth by directly editing the SVG file of maps. 

- [Flowing Data: How to Make a US County Thematic Map Using Free Tools](http://flowingdata.com/2009/11/12/how-to-make-a-us-county-thematic-map-using-free-tools/)

Finally, recommend to read [Let’s Make a Map](http://bost.ocks.org/mike/map/).

# Using Leaflet to draw geographical heatmaps

## Mapbox

[Mapbox](https://www.mapbox.com) is a mapping platform. You can use it for developing mobile or web apps, or use it to create geo-visualizations. Create an account, create a project, and play with it. You can display maps in different styles, in different locations, and in different zoom levels. When you click "save", it saves the current view (style, location, zoom level) as the default for your app. For heatmaps, black map works well. 

In "Project" tap, you can see your `map ID`. Copy the code in the `Embed` section somewhere, you can see the following code:

    share.html?access_token=.....'></iframe>

Copy the .... part (the `access token`). 

## Leaflet

Now you can use the mapbox tiles with the [Leaflet, which is an open-source JavaScript library for mobile-friendly interactive maps](http://leafletjs.com). By using the following pages, draw a heatmap of Walmart stores. 

- [Wal-Mart Stores](https://www.google.com/fusiontables/DataSource?docid=1ag3Z3Uwp_hWiHeiBRqGrS_HzEtwUjeVh4d4ZAnI#rows:id=1): `File` -> `Download`
- [Leaflet Quick start guide](http://leafletjs.com/examples/quick-start.html)
- [A tiny, simple and fast heatmap plugin for Leaflet.](https://github.com/Leaflet/Leaflet.heat) - you don't need to download from this page. Use the following template. 

Here is an HTML template:

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width">
<title>Walmart Heatmap</title>

<link rel="stylesheet" href="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.css" />

<style type="text/css" media="screen">
#map { height: 800px; }  
</style>

</head>

<body>

<div id="map"></div>

<script src="http://cdn.leafletjs.com/leaflet/v0.7.7/leaflet.js"></script>
<script src="http://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js"></script>
<script src="walmart.js"></script>  <!-- put your data into data.js -->

<script>

//  put your code here. 

</script>

</body>
</html>

```

You can get something like this: 

![Walmart heatmap](https://raw.githubusercontent.com/yy/dviz-course/master/w12-geo-2/walmart.png)
