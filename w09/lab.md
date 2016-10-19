# Before the class
- http://setosa.io/ev/principal-component-analysis/
- http://distill.pub/2016/misread-tsne/


# Part 1
See the ipython notebook.

# Part 2: Axes and interactivity in D3

For this lab, we will start with the code that we wrote in the previous lab. You will need the `co2_income.csv` data file from the previous lab. 

## Adding axes
We need to give the scaling for the axis and the orientation of the tick labels. Add the following after the `svg.selectAll()` statement:

    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient("bottom");

To draw the x-axis, we need to append it to the SVG element. We can use the `g` element to group together the axis, ticks and numeric labels:

    svg.append("g")
  	   .attr("class", "x axis")
  	   .call(xAxis);

But this draws the axis at the top. To bring it down, we use the [`transform`](https://www.w3.org/TR/SVG/coords.html#TransformAttribute) attribute with the `translate` value. Basically, `translate(<x> [<y>])` specifies a translation from x to y. If y is not provided, it is assumed to be zero. This will move the entire group.

    svg.append("g")
  	   .attr("class", "x axis")
  	   .attr("transform", "translate(0," + (h - padding) +")")
  	   .call(xAxis);

Similarly, we can do this for the y-axis, with a few subtle changes:

    var yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left");

    svg.append("g")
  	   .attr("class", "y axis")
  	   .attr("transform", "translate(" + (padding) +",0)")
  	   .call(yAxis);

Notice how the scale and orientation has changed. Also, the `translate` values have been flipped from ‘0, h-padding’ to ‘padding, 0’. Note we have assigned the axes into different classes instead of a single class. This will allow us to modify only the x-axis when introducing interactivity later on.

### Making the axes "nice": 
The big circle on the left is extending beyond the limit of the axis. How can we fix this?

This is simple. Just add .nice() to the scales. For xScale, this would be:
	
    var xScale = d3.scale.linear()
                 	.domain([0, xmax])
                 	.range([padding, w - padding])
					.nice();
	
Do this for the other scales and refresh the page on the browser. What has happened? .nice() extends the domain limits so that we have "nicely" rounded values at the ends.

### Prettifying the plot: 
We can now change line thickness, font sizes and font styles of the axes by updating the CSS up in the `<style>` tags. You can customize the plot to your pleasing. For example:

    <head>
    <meta charset="utf-8">
    <style>
    circle {
    		fill: steelblue;
 			}
			.axis path,
 			.axis line {
    				fill: none;
    				stroke: black;
    				shape-rendering: crispEdges;
 			}

 			.axis text {
    				font-family: sans-serif;
    				font-size: 11px;
 			}
    </style>
    </head>

## Introducing interactivity
We are going to learn about animating visualizations through an example using our scatterplot. The effect we want is that clicking on some text will change the scale of the x-axis from a simple linear scale to a logarithmic scale. 

Any interactive system has three components: a trigger, a transition and an outcome. These are explained in the steps below: 

### Set up a trigger for transition
We need to first set up some kind of triggering mechanism to transition into the log scale - maybe a mouse hover, clicking on text or clicking on a button. To do this, first add this HTML code to the body (before the script and outside the `<script>` tags):

    <p>                                                                                                                                                                                     
    Click on this text to change to log-scale.                                                                                                                                                
    </p>

To try if the click is working, inside the script tags, at the very bottom, add the following:

    d3.select("p")
 	     .on("click", function() {
	     alert("Click working!");
 	     });

This part of the code selects the paragraph element and sets up a function such that when you click on the element, an alert message will be displayed. (After trying you can delete or comment out the code for the message.)

### Setting the outcome of the trigger
To change the x-axis to log scale on clicking, we simply need to update the scale and the x-positions of the circles in our scatter plot. 

Let us create a new variable containing the logarithmic scaling function. To change the x-axis to the logarithmic scale, all you need to do is use d3.scale.log() instead of d3.scale.linear(). Additionally, the minimum value in the domain will be 1 instead of 0 (because log 0 is not defined).

    d3.select("p")
 	      .on("click", function() {
              var xScale = d3.scale.log()
    		      .domain([1, xmax])
            	  .range([padding, w - padding])
                  .nice();
 	       });

Now, it is simply a matter of changing the x-position of the circles. Note that in the code below, the new logarithmic `xScale` will be used by the browser:

    d3.select("p")
 	    .on("click", function() {
        var xScale = d3.scale.log()
    		         .domain([1, xmax])
            	     .range([padding, w - padding])
                    .nice();

		svg.selectAll("circle")
        	   .attr('cx', function(d) {return xScale(+d.income));})
 	   });

### Adding and customizing a transition:
This is probably the easiest part! Just add .transition() above the `.attr` line.

    d3.select("p")
 	    .on("click", function() {
        var xScale = d3.scale.log()
    		         .domain([1, xmax])
            	     .range([padding, w - padding])
                    .nice();

		svg.selectAll("circle")
        	 .transition()
            .attr('cx', function(d) {return xScale(+d.income);})
 	   });

You can customize the duration of your transition by adding `.duration(1000) `below the transition line. This would make the transition take 1000 milliseconds (1 second). You can also add a delay after clicking by adding `.delay(1000)` after the transition statement. Finally, you can change the way the actual transition appears. For example, adding this after the transition statement: `.ease("bounce")` make the points "bounce in".  [Here](https://github.com/d3/d3-ease#d3-ease) is a complete list for the easing functions available.

Play with all these parameters and choose any customization of your liking.

### Updating the axis:
Finally, the only thing left to do is to update the x-axis tick values with a transition. This involves just updating the scale of xAxis to the new xScale that we’ve created. Can you update the code above and include the transition of the x axis?

Hint: you may want to figure out how to "select" the x axis to update it. Useful query: [d3 select axis](https://www.google.com/#q=d3+select+axis)

Note that if you want this transition to occur in the same manner as the points, then you will have to apply the same customization (delay, duration, etc.).

<b> Submit this file to Canvas.</b>

### Advanced(optional):
Another commonly used way of interaction is that with mouse hovering over the circles, display the data that the circle represents (That is, in our case, the x and y values). Can you implement this feature? For an example, see [this](http://bl.ocks.org/weiglemc/6185069) (ignore the coloring/legends).