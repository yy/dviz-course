# Before the class


# Part 1
See the ipython notebook.

# Part 2: Line chart

**Note: It is highly recommended to test your page through a local server. If you haven't been doing this, see [here](https://github.com/yy/dviz-course/wiki/Setting-up-a-local-server) for reference.** 

Let's make a line chart and play with some interactive features. 

Line charts are good at visualizing time series, so we'll work with a time series of Spanish silver production in the 18th century. The file can be found on Canvas (`spanish-silver.csv`), we'll only use the columns `year` and `silver_minted`.

We start with creating an SVG canvas and set the x and y axis based on the data. Now that you're familiar with D3, it shouldn't be too difficult. By adjusting the code from last week, create a setup like this:

![image](http://)

Note that the year data starts with not 0 but 1720, and the silver production data starts with not 0 but 7,369,815. This means when creating the `xScale` and `yScale`, in addition to the `xmax` and `ymax` that we calculated, we also need to calculate `xmin` and `ymin` in a similar way and use them to set `xScale` and `yScale`.

Next we just need to draw the line. D3 provides a `Path Data Generator` that can be used to create lines:

    var line = d3.svg.line()
        .x(function(d) { return xScale(d.year); })
        .y(function(d) { return yScale(d.silver_minted); })
        .interpolate("linear");
        
Here the function takes the data and create a series of points, whose x coordinate is year and y is the silver production. Note that we use `xScale` and `yScale` to put the points in the proper places.

`.interpolate("linear");` decides how the points should be connected. D3 has a few line interpolate methods (see [here](https://github.com/d3/d3-3.x-api-reference/blob/master/SVG-Shapes.md) for a list). For example, you can change the interpolate method to `basis` and see what happens.

Now we can append the line to our `svg` object:

    var path = svg.append("path")
        .attr("class", "line")
        .attr("d", line(data))
        .attr("stroke", "steelblue")
        .attr("fill", "none");
        
Here we use `.append("path")` because we really only have one data object (a set of x,y coordinates), so we do not need to selectAll(), .enter(), append() like we have with other data sets.

The attr `d` determines the shape of the `path` object. We call `line` (which works as a function) on our data, and let it give us the x and y coordinates, so that D3 can use it to draw the line.

Now we have a line chart:

![image](http://)

## Animation
We can add some animation effects to the line chart. For example, we can let the line "unroll" itself, imitating the drawing (see the method 2 [in this webpage](http://codepen.io/himmel/live/LpbpLb) for a demo). 

How can we achieve this? The intuition is like this:

1. We have an SVG shape and have drawn a line on it.

2. Imagine that we move the line away, so there is no line there at all.

3. Then gradually put the line back, so it looks as if we're drawing it.

The Actual way that it works with SVG is a bit more complicated. [Here](https://css-tricks.com/svg-line-animation-works/) is a good explanation, but for now we can just focus on the implementation.

First we need to get the lengh of our line:

    var totalLength = path.node().getTotalLength();

Then we'll add some new attributes to the `path` object.

    path
    .attr("stroke-dasharray", totalLength + " " + totalLength)
    .attr("stroke-dashoffset", totalLength)
    .transition() 
    .duration(5000) 
    .ease("linear") 
    .attr("stroke-dashoffset", 0); 
    

The first two `.attr`s moves the line away by setting an "offset". The actual distance that it is moved equals to the total lenth of the line. Recall the `transition` method that we used in the last lab. Here when the transition happens, we gradually reduce the offset to 0, so the line comes back. `.duration(5000)` controls how fast this effect should happen. `.ease("linear") ` customizes how the effect looks like.

Refresh your page, now you should be able to see the animation.

## Interaction
Interactive plots can be more attractive because they give users more control. For example, instead of drawing the line on page load, we can create a button `Start Animation`, so that the line is drawn when the user clicks on it. This is very simple.

Create a button in the HTML (outside the Javascript):
	
	<button id="start">Start Animation</button>

Then, we just need to create an `onclick` event and move the code for drawing the line in it.

    d3.select("#start").on("click", function() {
    //Move the code for creating the path and the animation here
    });
    
We can also create another button `reset` which removes the line onclick, allowing it to be drawn again. Can you implement this?

Hint: you can use `d3.select` to select the line. `.remove()` will delete it.

**Submit this file on Canvas.**    

## Advanced (optional)
An area chart is similar to a line chart, but fills the area underneath the line. Using the same data, can you change the code to create an area chart (no need to do the animation/interactions)? It should look like this:

![image](http://)

You can submit this as a seperate file if you choose to do it.







