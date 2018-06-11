# W13 Lab Assignment

## Part 1
See the Jupyter notebook.

## Part 2: Tree Maps

Tree maps are good at visualizing hierarchical data. We'll visualize the hierarchical structure of the packages in the [Flare visualization toolkit](http://flare.prefuse.org/) . The data for the second level packages is available on Canvas (`tier_2.json`), you can also download the complete data [here](https://gist.github.com/mbostock/1093025#file-flare-json). The plot would look like [this](http://bl.ocks.org/mbostock/4063582): the size of rectangles represent data values, and the colors encode different categories. 


Start with a skeleton html file:

    <!DOCTYPE html>
    <html>
    <head>
    <title>W13 Lab</title>
    </head>

    <body>
    <script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>

    <h1 align="center">W13 Lab Assignment</h1>

    <h2>Tree Map</h2>

    <h3>Tier 1</h3>
    
    </body>
    </html>




### Tier 1

First, let's focus on tier 1. The data is relatively small, so we can hardcode it in the script.

    <script type="text/javascript">
    var tier_1 = {
      "name": "flare", 
      "children": [
    {"name": "analytics", "size": 48716}, 
    {"name": "animate", "size": 100024}, 
    {"name": "data", "size": 30284}, 
    {"name": "display", "size": 24254}, 
    {"name": "flex", "size": 4116}, 
    {"name": "physics", "size": 29934}, 
    {"name": "query", "size": 89721}, 
    {"name": "scale", "size": 31294}, 
    {"name": "util", "size": 165157}, 
    {"name": "vis", "size": 432629}
     ]
    };

Let's choose some colors. D3 provides some [categorical colors](https://github.com/d3/d3-3.x-api-reference/blob/master/Ordinal-Scales.md#categorical-colors). The following line returns a scale of 20 colors:

    var color = d3.scale.category20c();

`D3.layout.treemap()` creates a treemap layout.

    var treemap = d3.layout.treemap()
    .size([910, 450])
    .sticky(true)
    .value(function(d) { return d.size; });

`sticky` means that treemap layout will preserve the relative arrangement of nodes across transitions.

Instead of creating an SVG element, this time we'll create a fixed `div`:

    var div = d3.select("body").append("div")
    .style("position", "relative")
    .style("width", "910px")
    .style("height", "450px");

Next create the nodes by reference our data, `tier_1`. D3 will make a rectangle for each node and put its name up there.

    var node = div.datum(tier_1).selectAll(".node")
    .data(treemap.nodes).enter()
    .append("div")
    .attr("class", "node")
    .style("background", function(d) { return color(d.name); })
    .style("font-size", function(d) { return Math.max(21, Math.log(d.area))+'px'; })
    .text(function(d) { return d.name; });

Open this page through a local server:

![image](https://github.com/yy/dviz-course/blob/master/w13-text-graph/tree_map_halfdone.png)

The rectangles are crammed together. What's going wrong?

We haven't specified the positions for each rectangle. We can do so by creating a function:

    function position() {
      this.style("left", function(d) { return d.x + "px"; })
      .style("top", function(d) { return d.y + "px"; })
      .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
      .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; });
    }
    </script>

and call this function by adding a line to the `var node` code, so the previous code will be like:

     var node = div.datum(tier_1).selectAll(".node")
    .data(treemap.nodes).enter()
    .append("div")
    .attr("class", "node")
    .call(position)
    .style("background", function(d) { return color(d.name); })
    .style("font-size", function(d) { return Math.max(21, Math.log(d.area))+'px'; })
    .text(function(d) { return d.name; });

`this` is a special keyword in Javascript. When the function `position` is called, `this` is given a value from the data. It takes the x and y coordinates of the rectangle (given by D3) and use them to set the positions of the rectangles.

Finally, set the style for the `node` class (put this in the html file under the  `<head>` tag).

    <style>
    .node {
    border: solid 1px white;
      overflow: hidden;
      position: absolute;
    }
    </style>


### Tier 2

Smilarly, we can also visualize the first two layers. But the tier 2 data is larger, so you would want to read in it as an external file (`tier_2.json`) using `d3.json`.

**TODO: make another plot visualizing tier 2. You can just add a `div` to the previous code, so the overall plot will look like the following. Submit this file to Canvas. **

![image](https://github.com/yy/dviz-course/blob/master/w13-text-graph/tree_map_2.png)
