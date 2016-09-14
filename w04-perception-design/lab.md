# Before the class

- [A better default colormap for matplotlib](https://www.youtube.com/watch?v=xAoljeRJ3lU)
- [Choosing Colormaps](http://matplotlib.org/users/colormaps.html)

# Lab assignment
## Part 1: Experiments with Steven's power-law and color maps

- https://github.com/yy/dviz-course/blob/master/w04-perception-design/w04_lab.ipynb

Also download the following two images and put them in the same folder.

- https://github.com/yy/dviz-course/blob/master/w04-perception-design/sneakySnake.png
- https://github.com/yy/dviz-course/blob/master/w04-perception-design/stevenspowerlaw_barh.png 

## Part 2: Introducing SVG

**Discussion question**: First of all, think about ways to store an image, which can be a beautiful scenary or a geometric shape (a square). How can you efficiently store them in a computer? Discuss pros and cons of different approaches. Which methods would work best for a photograph of a scene? Which methods would work best for a blueprint of a building?

[SVG](http://www.w3schools.com/svg/) stands for Scalable Vector Graphics. Compared to [raster graphics](https://en.wikipedia.org/wiki/Raster_graphics), [vector graphics](https://en.wikipedia.org/wiki/Vector_graphics) won't lose quality when zooming in. It is essentially an image file format and you can make and edit them in Adobe Illustrator, Inkscape, etc. In this course, we will mostly be using it for drawing/loading data with maps.

In HTML, there is a simple ‘svg’ tag that can be used to create a ‘canvas’ of sorts. It  tells the browser to reserve some space for a drawing that you will be making. For example:

	<svg width="200" height="200">
	   <circle cx="100" cy="100" r="22" fill="yellow" stroke="orange" stroke-width="5"/>
	</svg>


This code creates a drawing space of width 200 pixels and height 200 pixels as seen in the red-colored line. Inside the ‘svg’ tags, is a line that specifies a yellow circle of radius 22 to be drawn centered at the coordinates (100, 100).

Try to place this code snippet to an html file. What do you see?


There are two ways to style an svg element. The first way is in-line as in the code above, which is mostly self-explanatory. 


The second way involves the use of CSS. You can place all these attributes in the ‘head’ section of your code as follows:

	<head>
	<style>
	.krypton_sun {
	  fill: red;
	  stroke: orange;
	  stroke-width: 10;
	}
	</style>
	</head>
	<body>
	<svg width="500" height="500">
	   <circle cx="200" cy="200" r="50" class="krypton_sun"/>
	</svg>
	</body>

There are other shapes in SVG, such as [ellipse](http://www.w3schools.com/graphics/svg_ellipse.asp), [line](http://www.w3schools.com/graphics/svg_line.asp), [polygon](http://www.w3schools.com/graphics/svg_polygon.asp) (this can be used to create triangles), and [path](http://www.w3schools.com/graphics/svg_path.asp) (for curved and other complex lines). You can even place text with advanced formatting inside an ‘svg’ element using text.

###Exercise: 
Try to reproduce the symbol for the Deathly Hallows (as shown below) with SVG as closely as possible. What's the most efficient way of drawing this? Color it in the way you like. Upload this file to canvas.

![The deathly hallows](http://vignette1.wikia.nocookie.net/harrypotter/images/2/23/Hallows.png/revision/latest/scale-to-width-down/160?cb=20090309113642)




	
