# Before the class

- Python's [Counter](https://docs.python.org/2/library/collections.html#collections.Counter)
- [matplotlib - 2D and 3D plotting in Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)
- https://speakerdeck.com/jakevdp/statistics-for-hackers

# Part 1:

See the Jupyter notebook.

# Part 2: Introduction to Javascript (including d3) III

## More about Javascript functions

We have used functions in our Javascript code before.  Recall the basic form of a Javascript function:

    function printx(x) {
      console.log(x);
    }

We can also create a function by assign it to a variable:

    var printx = function(x) {
      console.log(x);
    }

The function only has one parameter x. What if we give it more values?

    > printx(1, 2, 3)
      1

An interesting feature of Javascript functions is that it is not strict about
the number of parameters given to it. If there are too many inputs, the extra
ones will be ignored. If too few, the unassigned parameters will be given the
value `undefined`.

Javascript also doesn't care about where we define a function. For example, the
following code:

    printx(1);

    function printx(x){
      console.log(x);
    }

will work, even if I define printx *after* calling it.

It is also possible to define a function within another function: 

    function printx(x){
      function double(y){
        return (y*2);
      }
      console.log(double(x));
    }

## Data binding in D3

In the previous lab, we manually specified the length of the bars in our bar
plot. This time, let's write some functions to generate random data. We'll use it to make a 1D scatterplot.

To generate a random number, we can use the following:

    Math.random();  // generate a random number between 0 and 1

How about a list of numbers? One way is using range and map functions of D3.
Type the following into the console, see what happens and try to understand
what the function is doing:

    d3.range(10);
    d3.range(100);

To this list, you can apply any function using the function `map()`. Try:

    d3.range(10).map(function(x) {return x*2;});

This would return 10 numbers, each multiplied by 2. You can also return any
number and override the original list:

    d3.range(10).map(function(x) {return 5;});

Now, generate a list of 10 random numbers using `Math.random()` together with
`.map()`. Once you’ve figured this out, save this list into a variable called
`values` in your HTML code.

Next, create two variables: `width = 500` and `height = 100`. Create an SVG
canvas with this width and height and 'append' it to the `body` element, and
store it in a variable called svg. Create a border for this SVG element by
adding CSS at the top of the HTML code. 

What we need to do now is draw small circles for each data point. To do that,
the first step is selecting **not-yet-existing** circles in svg, which we will
create later, using the function selectAll(). 

    svg.selectAll("circle");

What is the result of this? At this point, nothing is selected because there
are no circles in the SVG canvas. Now, bind the data into this empty selection
by calling the data() function.

    svg.selectAll("circle").data(values);

Recall that values is the array of random numbers that you saved a while ago.
Now, we call a special function called enter(). This function identifies the
objects that are bound to the data points but do not have any ‘shapes’. In this
case, there are 10 null objects that are bound to the data points.

    svg.selectAll("circle").data(values).enter();

So if you put this into the console, you can see 10 objects in the array and
that some data is attached to each object.

Now we can append actual circles to svg:

    svg.selectAll("circle").data(values).enter().append("circle");

but we can’t see the circles because the circles do not have any attributes
like position, radius or color. We need to at least set the ‘cx’, ‘cy’, ‘r’
properties. ‘cy’ and ‘r’ are easy:

    svg.selectAll("circle").data(values).enter().append("circle")
       .attr("cy", height/2)
       .attr("r", 5);

Try this. What can you see?

All the circles seem to be on the left side of the screen. So we want to set
the position of each circle using the data. How can we do that? Certainly we
don't want to do this one at a time: this is why we bound the data into the
circle objects. The secret is passing a function instead of a value. Let’s try
the following:

    svg.selectAll("circle").data(values).enter().append("circle")
       .attr("cy", height/2)
       .attr("r", 5)
       .attr("cx", function(d) {return d;});
       
This means that when you set the cx attribute, use the data that is bound to
each object. The attr() function pass the data to the function. The return
value of this function is used to set the cx attribute of the circle.

But you still can’t see the difference. Why? Think about what the range of the
random numbers in values are. Can such numbers cause a noticeable change on the
screen? Can you fix it? Put everything into the HTML and check whether you see
something like this:

![image](https://github.com/yy/dviz-course/blob/master/w07-fundamental-3/scatterplot.png)

Add text to the plot: To label the points in the scatter plot, you will need to
add text to your SVG. To do this, you will have to bind the data to text
elements. It is similar to how you’ve done it with the circles, except that the
attributes now are the (x, y) co-ordinates of the starting point of the text.
Can you change the positions such that they don’t overlap with the circles? 

Finally, add an axis label at the bottom of the SVG canvas to indicate what
quantity you are measuring (you can make up whatever you want). You can do this
by simply appending a text element to the SVG as in the previous lab.

**Submit this file on Canvas.**

### Advanced (optional): Jittered one-dimensional scatterplot

Create a plot similar to the one above, but put more dots, say 1000. Now you may want to make a jittered plot with varied transparency. Can you create a plot that looks like the following?

![image](https://github.com/yy/dviz-course/blob/master/w07-fundamental-3/scatterplot_jittered.png)

**Submit this file on Canvas.**



    
