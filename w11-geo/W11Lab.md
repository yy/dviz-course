# W11 Lab Assignment

We will introduce SVG, Javascript, and D3.js.

During this lab, we will be creating a html file named `W11Lab.html`. Submit this file to Canvas.

## Setup

Create a folder named `W11Lab` on the Desktop. This will be our [working directory](https://en.wikipedia.org/wiki/Working_directory) in this lab.

1. Open the Command Prompt in Windows or Terminal in Mac;
2. Change the working directory to `W11Lab`; in Command Prompt type `cd C:\Users\YOUR_USERNAME\Desktop\W11Lab` or in Terminal type `cd ~/Desktop/W11Lab`;
3. Start a web-server provided by Python by typing `python -m SimpleHTTPServer`

We will see:

`Serving HTTP on 0.0.0.0 port 8000 ...`

Then, open your favorite web browser and type `0.0.0.0:8000` or `localhost:8000` in the address bar.

## html

1. Under the `W11Lab` folder, create a blank file with name `W11Lab.html`;
2. Put the following code to `W11Lab.html`

```html
<!DOCTYPE html>
<html>
<head>
<title>W11 Lab Assignment</title>
</head>
<body>

<h1>W11 Lab Assignment</h1>

<p>We will introduce SVG, JavaScript, and D3.</p>

<h2>html</h2>

<h2>SVG</h2>

<h2>JavaScript</h2>

<h2>D3</h2>

</body>
</html>
```

Then, reload the web page localhost:8000 and open `W11Lab.html` or directly open it by typing `http://localhost:8000/W11Lab.html`

You can learn more from [here](http://www.w3schools.com/html/html_intro.asp).

**TODO**:

1. Center the h1 text [here](http://www.w3schools.com/tags/att_hn_align.asp);
2. Change the font color of h1 text;
3. Create more paragraphs using `<p>` tag under each `h2` tag.

## SVG

[SVG](http://www.w3schools.com/svg/) stands for Scalable Vector Graphics. Compared to [raster graphics](https://en.wikipedia.org/wiki/Raster_graphics), [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) won't lost quality when zooming in. 

In html, we can use the `svg` tag to create a canvas for drawing. For example, under the `<h2>SVG</h2>` tag, put the following in your html file to draw a [circle](http://www.w3schools.com/svg/svg_inhtml.asp).

```javascript
<svg width="300" height="300">
  <circle cx="40" cy="40" r="30" stroke="green" stroke-width="2" fill="yellow"/>
</svg>
```

This will create an SVG image with width 300 and height 300 and draw circle centered at (40,40) with radius 30.

**TODO**:

- Draw two more circles and change the center of the two circles to (140,140) and (240,240)

```javascript
<svg width="300" height="300">
  <circle cx="40" cy="40" r="30" stroke="green" stroke-width="4" fill="yellow" />
  <circle cx="140" cy="140" r="30" stroke="green" stroke-width="4" fill="yellow" />
  <circle cx="140" cy="240" r="30" stroke="green" stroke-width="4" fill="yellow" />
</svg>
```

So what are the x and y axis and what are their directions?

- Change the stroke color and fill color as well as stroke width. [HTML Color Values](http://www.w3schools.com/html/html_colorvalues.asp)

- Change the radius of the circle to 20, 30, 40, 50, 60. What happens and why?

```javascript
<svg width="100" height="100">
  <circle cx="50" cy="50" r="60" stroke="green" stroke-width="4" fill="yellow" />
</svg>
```

We can also set the transparency:

```javascript
<svg width="100" height="100">
  <circle cx="40" cy="40" r="30" stroke="green" stroke-width="4" fill="yellow" fill-opacity="0.4"/>
</svg>
```

**TODO**: Can you change the stroke opacity of the circle?

Beside circles, we can create many more shapes like [rectangle](http://www.w3schools.com/svg/svg_rect.asp):

```javascript
<svg width="400" height="50">
  <rect x="10" y="20" width="350" height="20" style="fill:gray;stroke:blue;stroke-width:2;fill-opacity:0.8;stroke-opacity:0.5" />
</svg>
```

More more shapes, check out [here](http://www.w3schools.com/svg/svg_ellipse.asp).

## JavaScript

JavaScript is a programming language for the Web. You can learn the basics from [here](http://www.w3schools.com/js/). In HTML, we need to punt JavaScript code between <script> and </script> tags. And we can use it to change the html content. Put the following code under the `<h2>JavaScript</h2>` tag in your html file:

```javascript
<script>
  var paragraphs = document.getElementsByTagName("p");
  for (var i = 0; i < paragraphs.length; i++) {
    var paragraph = paragraphs[i];
    if (i % 2 == 0) {
      paragraph.style.setProperty("color", "DarkViolet");
    } else {
      paragraph.style.setProperty("color", "Teal");
    }
  }
</script>
```

What does this for? Here the `document` object means the html document itself. The lists of its methods are showed [here](http://www.w3schools.com/jsref/dom_obj_document.asp). [**`getElementsByTagName()`**](http://www.w3schools.com/jsref/met_document_getelementsbytagname.asp) means to get all elements with the given tag, in our case all `p` tags. The [`style`](http://www.w3schools.com/jsref/dom_obj_style.asp) object is for style statement. Some basics used here are:

* [Variables](http://www.w3schools.com/js/js_variables.asp);
* [Comparison](http://www.w3schools.com/js/js_comparisons.asp);
* [for loop](http://www.w3schools.com/js/js_loop_for.asp)

**TODO**: Let's make some changes to the style of h2:

1. Set the background color to grey;
2. Change the font color.

## [D3](http://d3js.org/): Data-Driven Documents 

D3 is built upon JavaScript. There are two ways to reference D3. One is to directly put the following in the head section of your html files.

```javascript
<script src="http://d3js.org/d3.v3.min.js" charset="utf-8"></script>
```

The other one is to download the files from [here](https://github.com/mbostock/d3/releases/download/v3.5.6/d3.zip), put it to the working directory (`Desktop/W11/`), and then put the following code in the `head` section of the html file.

```javascript
<script src="d3.v3.min.js" charset="utf-8"></script>
```

We can use D3 to change the content of the document. For example, to change the style of all `h2` tags.

```javascript
<script>
  d3.selectAll("h2").style("color", "#FF8C00");
</script>
```

Here `selectAll()` is to select all elements that meet the requirements (all `h2` tags). You can know more about this from [Selections](https://github.com/mbostock/d3/wiki/Selections). More styles to change:

```javascript
<script>
  d3.selectAll("h2").style("color", "#FF8C00").style("background-color", "Lavender");
</script>
```

We can also create content:

```javascript
<script>
  var body = d3.select("body");
  var p = body.append("p");
  p.text("This is a paragraph created by D3!")
</script>
```

The [**`append()`**](https://github.com/mbostock/d3/wiki/Selections#append) method is to append a new element.

Do it in a chain style:

```javascript
<script>
  var body = d3.select("body").append("p").text("This is another paragraph created by D3!!");
</script>
```

But I want to do data visualization!

Let's create horizontal bars, manually, which are just many rectangles. Recall that we can draw rectangles using SVG. First, to separate the contents between different parts of the document, we can use a `<div>` tag:

<div id="bar">
</div>

Now we can create an SVG canvas, draw the first bar, and place the value at the end of the bar:

```javascript
<script>
  var data = [43, 27, 18, 9, 2]
  var svg = d3.select("#bar")
      .append("svg")
      .attr("width",  d3.max(data)*10)
      .attr("height", data.length*25);
  
  var bar1 = svg.append("rect")
      .attr("x", "0")
      .attr("y", "0")
      .attr("width", 43*10)
      .attr("height", 23)
      .attr("fill", "DarkGray");
  
  svg.append("text")
     .attr("x", 410)
     .attr("y", 16)
     .text("43")
     .style("fill", "white");
</script>
```

**TODO**: Can you draw the other four bars and also show the values?
