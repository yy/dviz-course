# W13 Lab Assignment

Word cloud and tree map.


## Word Cloud

We will use a Python library called [word_cloud](https://github.com/amueller/word_cloud) to generate word cloud.

To install it:

	pip install wordcloud

**TODO**:

Follow the example [here](https://github.com/amueller/word_cloud/blob/master/examples/simple.py) to generate a word cloud of movie titles in the IMDb dataset. Submit the generated image file to Canvas.

## Setup

Create a folder named `W13Lab` on the Desktop and set it as the root for the server:

`python -m SimpleHTTPServer`

or

`python -m http.server`

The defualt port number is 8000.

Note:

* If you see `file://…` in your browser's address bar, the file is **not** served through the web server. Instead, type in `localhost:8000/…` and choose the html file;
* To reload a webpage, you can press CTRL + R (Windows) or Command + R (Mac).

Then create a skeleton html file called `W13Lab.html`.

```html
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

<hr>

<h3>Tier 2</h3>

<hr>

</body>
</html>
```

## Tree Maps

Let's visualize the hierarchical structure of the packages in the [Flare visualization toolkit](http://flare.prefuse.org/).

### Tier 1

First, let's focus on the tier 1: 

```javascript
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

var color = d3.scale.category20c();

var treemap = d3.layout.treemap()
    .size([910, 450])
    .sticky(true)
    .value(function(d) { return d.size; });

var div = d3.select("body").append("div")
    .style("position", "relative")
    .style("width", "910px")
    .style("height", "450px");

var node = div.datum(tier_1).selectAll(".node")
    .data(treemap.nodes).enter()
    .append("div")
    .attr("class", "node")
    .call(position)
    .style("background", function(d) { return color(d.name); })
    .style("font-size", function(d) { return Math.max(21, Math.log(d.area))+'px'; })
    .text(function(d) { return d.children ? null : d.name; });

function position() {
  this.style("left", function(d) { return d.x + "px"; })
      .style("top", function(d) { return d.y + "px"; })
      .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
      .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; });
}
</script>
```

And set the style for the `node` class (put this in the html file under the  `<head>` tag)

```css
<style>
.node {
  border: solid 1px white;
  overflow: hidden;
  position: absolute;
}
</style>
```

`tier_1` is the data we want to visualize. [**`d3.scale.category20c()`**](https://github.com/mbostock/d3/wiki/Ordinal-Scales#category20c) returns one of 20 categorical color based on input data. [**`d3.layout.treemap()`**](https://github.com/mbostock/d3/wiki/Treemap-Layout#treemap) creates a new layout for treemap. For other types of layout, see [d3.layout](https://github.com/mbostock/d3/wiki/Layouts).

### Tier 2

Smilarly, we can also visualize the first two layers:

```javascript
<script type="text/javascript">
var color = d3.scale.category20c();

var treemap = d3.layout.treemap()
    .size([910, 450])
    .sticky(true)
    .value(function(d) { return d.size; });

var div = d3.select("body").append("div")
    .style("position", "relative")
    .style("width", "910px")
    .style("height", "450px");

d3.json("tier_2.json", function(error, root) {
var node = div.datum(root).selectAll(".node")
    .data(treemap.nodes)
    .enter().append("div")
    .attr("class", "node")
    .call(position)
    .style("background", function(d) { return d.children ? color(d.name) : null; })
    .style("font-size", function(d) { return Math.max(10, 0.1*Math.log(d.area))+'px'; })
    .text(function(d) { return d.children ? null : d.name; });
});

function position() {
  this.style("left", function(d) { return d.x + "px"; })
      .style("top", function(d) { return d.y + "px"; })
      .style("width", function(d) { return Math.max(0, d.dx - 1) + "px"; })
      .style("height", function(d) { return Math.max(0, d.dy - 1) + "px"; });
}
</script>
```

For the whole tree, see [here](http://bl.ocks.org/mbostock/4063582). You can get the data [here](https://gist.github.com/mbostock/1093025#file-flare-json).
