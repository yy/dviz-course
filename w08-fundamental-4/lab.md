# Before the class

- [matplotlib - 2D and 3D plotting in Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)


# Part 1
See the ipython notebook.

# Part 2: Introduction to Javascript (including D3) IV

## More about Javascript objects

In javascript, almost everything is an object. An object is a collection of named values in the form of key:value pairs. For example:

    var Batman = {realName: "Bruce Wayne", residence:"Gotham City"};

We can compare them to dictionaries in Python. 

To create an object, one common way is to use the object constructor by the keyword `new`:

    var theOneRing = new Object{};
    theOneRing.color = "yellow";
    theOneRing.material = "gold";
    theOneRing.maker = "Sauron";
    
Or more directly:
   
    var theOneRing = {
    color:"yellow",
    material:"gold",
    maker:"Sauron",
    };
    
The values of the object are called their properties. To access the properties of objects, there are two ways:

Dot notation

    console.log(theOneRing.color);

Bracket notation


    console.log(theOneRing['color']);

Notice that if the property name is numerical, we can only use the bracket notation.

	var theOneRingOwners = {
	0:"Sauron",
	1:"Isildur"
	};
	
    >theOneRingOwners.0
    x Uncaught SyntaxError: Unexpected number
    
    >theOneRingOwners[1]
    <"Isildur"
    
What if the property that I try to access does not exist?

    > theOneRing.price
    < undefined
     
When we create a selection using D3, we're creating an object. 

    	var svg = d3.select("body").append("svg")
    	
   	    console.log(typeof(svg))
   	    < object

When we set, for example, the attributes of the svg, what are we calling?

    	var svg = d3.select("body").append("svg")
        .attr("width", 700);

	    console.log(svg.attr)
		< function (n,t){if(arguments.length<2){if("string"==typeof n)`{vare=this.node();return n=ao.ns.qualify(n),n.local?e.getAttributeNS(n.space,n.local):e.getAttribute(n)}for(t in n)this.each(z(t,n[t]));ret…

It's a property that contains a function. These are Javascript methods: functions stored as object properties.

## 2-D scatter plot with D3

The file `co2_income.csv` can be found on Canvas. We'll make a 2-D scatter plot of average income against CO2 emission per person in different countries, where each circle’s size is proportional to the amount of CO2 produced (data from Gapminder).

### Binding data from external files

Recall from the last lab that binding data means linking elements of our visualization such as circles, bars, etc. to elements in our data such as income, hours, etc. Specifically, we use d3.js to bind data to certain HTML elements and their attributes. For example:

    svg.selectAll("circle")
    .data(values)
    .enter()
    .append("circle")
    .attr("cy", height/2)
    .attr("r", 5)
    .attr("cx", function(d) {return width * d;});

Remember that .data() and .enter() bound the data to all circles (that were not drawn yet until the call to the .append() function).

This time we'll use some data from external files. To read data from a csv file, D3 provides a method:

    d3.csv("co2_income.csv", function(data) {
        //do something with the data
        });

In the case of web pages like ours, think about what would happen if we had an extremely large CSV file? Would it not take a really long time to load and slow down the display of the rest of the page? To avoid this, D3 uses a 'callback' function that is executed asynchronously. This allows the rest of the page to be displayed while the data is being loaded, instead of waiting for it. 

In the case of such asynchronous functions, put EVERYTHING else in this exercise within the d3.csv() function as follows:

    d3.csv("co2_income.csv", function(data) {
		// THE CODE FOR THE VIZ GOES HERE
        });
        
    

### Scaling in D3

First, make a skeleton HTML page like the ones in previous exercises. In the HTML, define two variables `w` and `h` with some numbers like width 1000 and height 500. Also create another variable called `padding` and set it to 30 (we will use this later).

Create an SVG element with the width and height attributes set to `w` and `h` using `.attr()` and append it to the `body` using `.append()`.

In Lab 7, when you set the center of each circle to be a value from your array of random numbers, they were placed on top of each other at the left border of the SVG element. Remember that in order to separate them out, you multiplied the values by the width to correctly "scale"" each center’s position along the x-axis. What if the math was more complicated than that?

Luckily, the d3.scale() function does this automatically for us. A scale is a transformation of some number (within a specific range) into the SVG coordinates. Then, the browser translates these numbers as a physical location on the browser screen.

It consists of two parts: a domain and a range. The domain is the input, i.e. the range of numbers in your dataset. The range is the output, i.e. the range of numbers that you want to squeeze the original numbers into (see the illustration below). In our case, the range would be related to the dimensions of our canvas.

![image](https://github.com/yy/dviz-course/blob/master/w08-fundamental-4/d3_scale_illustration.png)

In the web console, type the following:
	
    var s = d3.scale.linear();

Now type: 

    s(200);
    
What happens?

Now type the following:

    s.domain([100, 500]);
    s.range([10, 100]);

If you type `s(200)` again, what happens? Try a few more numbers between 100 and 500. See a pattern? You have essentially created a function stored in the variable `s` that scales an input range to a desired output range.

For our HTML page, we need to create three different scales - two for the axes and one for the circle size. Let us start with the x-axis first. Since we will be plotting the `income` on this axis, the domain of this scale will lie between 0 and the maximum value in the `income` column. To find this value, we will use the function called d3.max().  However, this function only works on a single array of numbers. So we can’t just simply do:

    d3.max(data);

You will need to make your own function to return the specific object (column name) that you want to find the max of. In the case of the x-axis, add the following line to your code:

    var xmax = d3.max(data, function(d) {return +d.income; });

The `+` converts strings into numbers here. Now, you can go ahead and create the scale for the x-axis as follows:
	
    var xScale = d3.scale.linear()
                 .domain([0, xmax])
                 .range([0, w]);

Note that the range here is set between 0 and `w` because the x-axis will go from left to right (the entire width of the SVG element).

Can you repeat this for the remaining columns in the data? Name them `ymax` and `rmax`. Create two more scales using these max values. Store them in variables called `yScale` and `rScale`, respectively. For `rScale`, you can use any arbitrary maximum value in the range, such as 10. What would be the maximum range value for `yScale`?


### Drawing the plot
In the previous lab, we learned how to make circles for each datapoint:

    var circles = svg.selectAll("circle")
 			 	 .data(data)
       	         .enter().append("circle")
 			 	 .attr('cy', h/2)
 			 	 .attr('r', 5)
 	      	     .attr('cx', function(d) {return w*d;});

Now the `data` is no longer a simple list as it was the last time. So instead of returning `d`, we need to return `+d.income`. Also, we need to return a scaled version of these values. Remember that `xScale` is a function that we created. Can you call `xScale` to set the `cx` values?

Also use yScale and rScale on the appropriate quantities to generate `cy` and `r` (remember the y-axis should be the amount of CO2 emitted per person).

At this point, you should have a plot that looks like the following:

![image](https://github.com/yy/dviz-course/blob/master/w08-fundamental-4/plot_halfdone.png)

The resulting plot looks a little weird, doesn’t it?

First, the points seem to be placed at the top of our canvas. This is because (0,0) is at the top-left corner. In order to place the points correctly, you need to flip the min and max values for the `.range()` function in yScale, i.e. instead of [0, h], you will have [h, 0]. Go back and change this.

Second, the points at the edge seem to get cut off. To fix this, we create some margin space for the plot on all sides by using the variable that we created earlier called padding. Go back and change xScale and yScale such that the min values are no longer 0 but padding and the max values are reduced by the value stored in padding.

Now the plot will look like this:

![image](https://github.com/yy/dviz-course/blob/master/w08-fundamental-4/plot_final.png)

Next week, we will be adding axes to this plot. <b>Submit this file on Canvas. </b>



    
