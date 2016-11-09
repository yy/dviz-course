# W12 Lab Assignment

# Part 1:
See the ipynb file.

# Part 2: Maps II

## Bubble maps

We'll display the 10 fastest growing cities in the US, with bubble sizes representing their populations. This is mostly putting things we've already covered together. 

Start from this skeleton from the last lab :

    <!DOCTYPE html>
    <meta charset="utf-8">
    <style>

    .counties {
 		fill: #000;
 			stroke: #fff;
 			stroke-width: 0.25px;
    }

    .states {
 			fill: none;
 			stroke: #fff;
 			stroke-linejoin: round;
    }
    </style>

    <body>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="http://d3js.org/topojson.v1.min.js"></script>
    <script>

    var width = 960,
   			height = 500;

    var projection = d3.geo.albersUsa()
				  		   	  .scale(1000)
				  		       .translate([width / 2, height / 2]);

    var path = d3.geo.path()
        		 		  .projection(projection);

    var svg = d3.select("body").append("svg")
					 .attr("width", width)
					 .attr("height", height);

    d3.json("us.json", function(error, us) {

				svg.append("g")
  	   			   .attr("class", "counties")
  	   			   .selectAll("path")
  	   			   .data(topojson.feature(us, us.objects.counties).features)
  	   			   .enter().append("path")
  	   			   .attr("d", path);

				svg.append("path")
   	   			   .datum(topojson.mesh(us, us.objects.states, function(a, b) { return                a !== b; }))
   	   			   .attr("class", "states")
   	   			   .attr("d", path);

    });
    </script>
    </body>
    
We can make it a little more nice-looking. 

**TODO**: Change the color of the map from black to #fcfa86 and color the state and county boundaries in orange.

The data we'll use is `city_growth.csv` (on Canvas). To read in the data:

    d3.csv("growth.csv", function(error, data) {
		// Drawing of map already done before
		// Now we will draw the points here
    });

#### Drawing circles

Recall that drawing a circle requires two parameters - the center (`cx`, `cy`) and the radius (`r`). Add the following within the d3.csv() function.

    svg.selectAll("circle")
  	   .data(data)
  	   .enter()
  	   .append("circle")
  	   .attr("cx", function(d) {return projection([d.lon, d.lat])[0];})
  	   .attr("cy", function(d) {return projection([d.lon, d.lat])[1];})
  	   .attr("r", 5)
 	   .style("opacity", 0.5)
  	   .style("fill", "red");

The main trick here is that we are applying the Albers projection to the longitudinal and latitudinal information in the CSV file. The output of this application serves as the center for each point.

Changing the size and transparency of the circles:

For the radius, we can use a hardcoded scaling function. Change the correspoding code as the following:

    svg.selectAll("circle")
  	   .data(data)
  	   .enter()
  	   .append("circle")
  	   .attr("cx", function(d) {return projection([d.lon, d.lat])[0];})
  	   .attr("cy", function(d) {return projection([d.lon, d.lat])[1];})
  	   .attr("r", function(d) {return Math.sqrt(d.pop * 0.00004);})
  	   .style("fill", "red");

For the opacity, we can just set a number between 0 and 1.

**TODO**: Set the transparency of the circles.

### Adding text labels

Finally, we want to place the text labels such that there are placed close enough to the points that we have drawn.

We could keep them right at the center of each circle, i.e. the x and y co-ordinates of the text would correspond to the cx and cy values of the circles. But that would not be clean enough.

We could move them to the right by a bit. But by how much? If we need to prevent them from overlapping with the circles, we need to move by a distance equal to the radius at the least. Now, the x-value will be:
			                 
cx + radius + some offset

**TODO**: Add the labels. Update the CSS style in the header to make all the labels colored red, with font-family sans-serif and font-size 10px. 

**Submit this file on Canvas.**

## Using Leaflet to draw geographical heatmaps

### Mapbox

[Mapbox](https://www.mapbox.com) is a mapping platform. You can use it for developing mobile or web apps, or use it to create geo-visualizations. Create an account, create a project, and play with it. You can display maps in different styles, in different locations, and in different zoom levels. When you click "save", it saves the current view (style, location, zoom level) as the default for your app. For heatmaps, black map works well. 

In "Project" tap, you can see your `map ID`. Copy the code in the `Embed` section somewhere, you can see the following code:

    share.html?access_token=.....'></iframe>

Copy the .... part (the `access token`). 

### Leaflet

Now you can use the mapbox tiles with the [Leaflet, which is an open-source JavaScript library for mobile-friendly interactive maps](http://leafletjs.com). By using the following pages, draw a heatmap of Walmart stores. 

- [Wal-Mart Stores](https://www.google.com/fusiontables/DataSource?docid=1ag3Z3Uwp_hWiHeiBRqGrS_HzEtwUjeVh4d4ZAnI#rows:id=1): `File` -> `Download`
- [Leaflet Quick start guide](http://leafletjs.com/examples/quick-start.html)
- [A tiny, simple and fast heatmap plugin for Leaflet.](https://github.com/Leaflet/Leaflet.heat) - you don't need to download from the page. Use the following template. 

Here is an HTML template:

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
    <script src="http://leaflet.github.io/Leaflet.heat/dist/leaflet-heat.js">
    </script>
    <script src="walmart.js"></script>  <!-- put your data into data.js -->

    <script>

    //  put your code here. 

    </script>

    </body>
    </html>


You can get something like this: 

![Walmart heatmap](https://raw.githubusercontent.com/yy/dviz-course/master/w12-geo-2/walmart.png)
