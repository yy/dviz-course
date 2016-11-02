# Before the class
Understand more about SVG paths and how D3 utilizes them: [https://www.dashingd3js.com/svg-paths-and-d3js](https://www.dashingd3js.com/svg-paths-and-d3js)

# Part 1
[https://github.com/yy/dviz-course/blob/master/w11-geo/w11_lab.ipynb](https://github.com/yy/dviz-course/blob/master/w11-geo/w11_lab.ipynb)

# Part 2: Maps I

## A basic map of the US
### topojson
To save time, let us start with the following HTML skeleton. Note that SVG elements have already been added. You can check this using the Inspector.

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>

    </style>
    </head>

    <body>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="http://d3js.org/topojson.v1.min.js"></script>
    <script>
    var width = 960, height = 500;

    var svg = d3.select("body").append("svg")
					 	 .attr("width", width)
					 	 .attr("height", height);
    </script>
    </body>
    </html>

We'll use `us.json` (on Canvas)to draw the US map. Its like any other JSON object that you may have seen but is more complex in structure. You can open the file in a text editor if you are curious. For more information on this format, see these links:

GeoJSON:

[http://en.wikipedia.org/wiki/GeoJSON](http://en.wikipedia.org/wiki/GeoJSON)

[https://github.com/mbostock/d3/wiki/Geo-Paths](https://github.com/mbostock/d3/wiki/Geo-Paths)

TopoJSON:

[http://en.wikipedia.org/wiki/Topojson](http://en.wikipedia.org/wiki/Topojson)

[https://github.com/mbostock/topojson](https://github.com/mbostock/topojson)

Frst we need to define a path generator. This is D3’s way of converting messy TopoJSON co-ordinates into `<path>` code in the SVG element. This function does all the math for you. We define a path generator as follows:

    var path = d3.geo.path();

Reading in JSON files is similar to reading in CSV and TSV files. It is as simple as adding the following to your code:

    d3.json("us.json", function(error, us) {
        //console.log(topojson.feature(us, us.objects.states));
	    // ALL CODE RELATING TO THE JSON FILE GOES HERE
    }

In this case, all the contents of the JSON file will be accessible through the variable `us`. The `console.log` command prints a part of the object to let you check if the file is loaded successfully (you can delete it once you know it's working). Just as in the case of CSV files, d3.json is asynchronous, i.e. subsequent lines of code are executed while the file is being read in, in the background. 

Now lets do some drawing! The JSON file contains co-ordinates for "arcs" to pass through. From the SVG lab, we know that drawing irregular shapes is all about creating paths that pass through a certain set of points on the SVG canvas. The following steps connect these two concepts together:

    svg.append("g")
  	   .attr("class", "counties")
  	   .selectAll("path")
  	   .data(topojson.feature(us, us.objects.counties).features)
  	   .enter().append("path")
  	   .attr("d", path);

You have seen most of these before. We will focus only on what’s new. The `data` function now takes in this input called `topojson.feature()`. This is a function that takes in a TopoJSON object and selects all the features we want at the given level of the data in the object. Here, we are accessing all co-ordinate information at the county level. For more information on this function see [here](https://github.com/mbostock/topojson/wiki/API-Reference#wiki-feature
).

The second new piece of code is the use of the path generator variable called `path` in the last line, that we created before. As mentioned earlier, `path` does the math and calculates the exact positions for all the arcs. The `d` attrbute then use these to make the shapes.

Finally, to make the county lines visible, we need to update some style elements in the CSS. So the overall code would look like this:

    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
    .counties {
 					fill: #000;
 					stroke: #fff;
					stroke-width: 0.5px;
     }
    </style>
    </head>
    <body>
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script src="http://d3js.org/topojson.v1.min.js"></script>
    <script>
    var width = 960, height = 500;

    var path = d3.geo.path();

    var svg = d3.select("body").append("svg")
						 .attr("width", width)
						 .attr("height", height);
	
	d3.json("us.json", function(error, us) {	
			console.log(topojson.feature(us, us.objects.states));
		    svg.append("g")
  		   	.attr("class", "counties")
  		   	.selectAll("path")
  		   	.data(topojson.feature(us, us.objects.counties).features)
  		   	.enter().append("path")
  		   	.attr("d", path);
    });

    </script>
    </body>
    </html>

Now you should be able to see the map.

### Formatting
We can also draw borders in different ways. For example, we may want to highlight the state borders. Add the following code after `svg.append("g")`:

    svg.append("path")
  	    .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
  	   .attr("class", "states")
  	   .attr("d", path);

The key difference between here and the previous situation is that we use `datum()` instead of `data()`. This accesses features in the data individually as opposed to as a whole with `data()`. We do this because we want to apply `topojson.mesh()` this time. This function enables the drawing of irregular shapes without “double-drawing“ in regions already rendered. That is essentially what the `function(a, b)` is doing - features are only sent for drawing if `a` and `b` are different. For more information see this link: [https://github.com/mbostock/topojson/wiki/API-Reference#wiki-mesh](https://github.com/mbostock/topojson/wiki/API-Reference#wiki-mesh
)

To format the states' display, add the following to the `<style>` tag:

    .states {
 					fill: none;
 					stroke: #fff;
 					stroke-linejoin: round;
    }

### Projections
As discussed in Monday’s class, there are different projections that can be used to represent 3D data on a 2D plane. We will use the Albers projection as it is a very popular projection for the United States. For more information on how this projection works:

[http://en.wikipedia.org/wiki/Albers_projection](http://en.wikipedia.org/wiki/Albers_projection
)

To apply a projection to our map, we need to add a statement to the path generator code:


	var projection = d3.geo.albersUsa()
				   			   .scale(1000)
				   			   .translate([width / 2, height / 2]);

    var path = d3.geo.path()
			 		  .projection(projection);

Here, `translate` is set to the mid-point of the canvas and therefore, the map is centered. Try changing the denominators to see how the map moves. `scale` adjusts the size of the map we draw (1000 is the default). 

Here is a link to different kinds of projections: [https://github.com/d3/d3-3.x-api-reference/blob/master/Geo-Projections.md](https://github.com/d3/d3-3.x-api-reference/blob/master/Geo-Projections.md)

TODO: Replace the Albers projection with any projection of your choice. Note that the scaling and the specific numbers may have to change for projections not specific to the US. **Submit this file to Canvas.**

    