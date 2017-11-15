# Before the class

- W6 class slides (canvas) and [reading](https://github.com/yy/dviz-course/blob/master/w06-fundamental-2/class.md#before-the-class)
- http://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
- https://en.wikipedia.org/wiki/Cumulative_distribution_function


# Part 1:

https://github.com/yy/dviz-course/blob/master/w06-fundamental-2/w06_lab.ipynb

# Part 2: Introduction to D3
**Note:** We haven’t updated to D3.v4 yet, and all following class materials are using D3.v3. I you choose to use v4, a few changes would need to be made depending on your code. 

Here is a list of changes that you’re likely to encounter: [Upgrading d3 from v3 to v4](https://keithpblog.org/post/upgrading-d3-from-v3-to-v4/)

And this is the full list of changes: [https://github.com/d3/d3/blob/master/CHANGES.md](https://github.com/d3/d3/blob/master/CHANGES.md)

Just keep in mind that if you see errors, you may want to check if they're relevant to version difference.


## What is D3?

D3 stands for Data-Driven Documents. Loosely, this means instead of thinking of
a webpage as a static and pre-constructed document, it can be conceptualized as
a document constructed "on-the-fly" from data. Think of D3 as a means of
creating and modifying HTML elements without having to type them out by hand.

Note that D3 is NOT a distinct language. It is a library written in JavaScript
and, thus, obeys all the syntax and rules that are applicable to JavaScript. It
has emerged as one of the most popular libraries for web-based visualizations.
Interestingly, the original framework for D3 was created by Mike Bostock (a PhD
student), Vadim Ogievetsky (MS student) and Prof. Jeff Heer. Just goes to show
what can be achieved in school!

## Referencing D3

The JavaScript code for D3 is stored in a file called d3.js and just like any
other JavaScript code, it should be referenced in the ‘head’ section as
follows:

    <script src="http://d3js.org/d3.v3.min.js" charset="utf-8">
    </script>

Alternatively, you can download this JavaScript file and save it to the folder
where the HTML page would be. In such a case, you can reference it as follows:

    <script src="d3.v3.min.js" charset="utf-8"></script>

You can then start writing the code that uses D3 inside `<script>`tags in the
`body` section to generate visualizations, create HTML elements, etc.

## Writing code using D3

Remember, D3 is nothing but JavaScript, except that, it provides custom-written
functions for the creation of powerful data visualizations. Try the following
example on a basic HTML page:

    <body>
      <script type="text/javascript">
        var body = d3.select("body");
        var p = body.append("p");
        p.text("New paragraph!");
      </script>
    </body>
 
Open this in the browser and see what happens. Open up the ‘Web Inspector’ and
view the code for the page. Is it the same as what you’ve written? What has
happened here?

Let us go over each line of this code:

`d3.select()` selects an element of the HTML page and stores this selection in
a variable. The input to this function is the name of the element. In this
case, the selected element was `body` and the variable was `body`. 

`.append()` appends an element into the element selected above. In
this case, a `p` tag is created inside the `body` element. That is why in the
`Inspector` you now see `p` tags inside the body. Here, `p` is input to the
function whose output is stored in a variable named `p`.  `.text()`
adds some input text to the selected element.

Thus, without typing any HTML code out, new content has been generated on your
page by the functions pulled from d3.js. Note that functions such as
`d3.select()`, `.append()` and `.text()` have already been
written out for you in this JavaScript file. All you need to know is what
functions are available and how to use them. For a full list of functions and
their input/output parameters, you can always refer to the D3 API. 

## Chaining in D3

A very nice feature of D3 is that you can string together function-calls in one
command as if it were a ‘chain’ of commands. This eliminates the need for too
many variables and helps make the code more efficient. For example, the above
code can be rewritten as follows and the end-result would be no different than
before:

    <body>
      <script type="text/javascript">
        d3.select("body").append("p").text("New paragraph!");
      </script>
    </body>

To improve readability, the general convention that is adopted is to separate
out each chained statement in different lines, as follows:

    <body>
      <script type="text/javascript">
      d3.select("body")
        .append("p")
        .text("New paragraph!");
      </script>
    </body>

## Exercise: simple bar chart using D3

We have introduced how to use SVG elements to create a desired shape. Now we
can create and manipulate SVG elements using D3.

Start with a simple skeleton HTML page as shown below and save it as
`barchart.html`:

    <html>
    <head>
      <title>"Bar chart"</title>
      <script src="http://d3js.org/d3.v3.min.js" charset="utf-8">
      </script>
    </head>
    <body>
    </body>
    </html>

Here we'll not use more sophiscated functions, but draw each bar manually. Create five `div` elements with IDs `bar1`, `bar2`, `bar3`, `bar4` and `bar5`:

    <body>
      <div id="bar1">
      </div>
      <div id="bar2">
      </div>
      ...
    </body>

Inside each `div`, open `script` tags and write D3 code to select the `div`,
append an SVG canvas of a particular size. This will create the spaces to draw the rectangles. Ensure that for all `divs`, the same dimensions are used:

    <div id="bar1">
    <script type="text/javascript">
    var svg1 = d3.select("#bar1")
                 .append("svg")
                 .attr("width", 500)
                 .attr("height", 30);
    </script>
    </div>

Notice a new function called `attr()`? This function assigns attributes to a
given HTML tag. In the case of the `svg` tag, we want to specify its width and
height. As you can see in the example, the `attr()` function takes two inputs -
the name of the attribute and the value of the attribute.

Now that the canvases have been created, create bars of with DIFFERENT widths
but the same height inside each `div`. This can be done by appending
rectangles:

    <div id="bar1">
    <script type="text/javascript">
    var svg1 = d3.select("#bar1")
                 .append("svg")
                 .attr("width", 500)
                 .attr("height", 30);

    var bar1 = svg1.append("rect")
                   .attr("width", 250)
                   .attr("height", 30);
    </script>
    </div>


Once you have done this for all divs, open the file in the browser to see if
the bars appear. Check 'Inspector' to see if all the correct HTML code has been
generated.

Now, at the top of each bar, include the width of the bars as an indicator of
the value that it represents. For example, a bar of width 250 will have the
number 250 at the base. This can be done as following:

    <div id="bar1">
    <script type="text/javascript">
    var svg1 = d3.select("#bar1")
                 .append("svg")
                 .attr("width", 500)
                 .attr("height", 30);

    var bar1 = svg1.append("rect")
                   .attr("width", 250)
                   .attr("height", 30);

    svg1.append("text")
        .attr("x", 200)
        .attr("y", 17.5)
        .text("250")
        .style("fill", "white");
    </script>
    </div>

Once you have done this, numbers should be visible at the top of the bar.
Depending on the dimensions, you may have to adjust the ‘x’ and ‘y’ attributes
in the above statement.

Finally, it is time to style all these elements. There are two ways to do this:
one is to use CSS in the `head` section of the code like we have done in
previous labs. The other is to use the `select.style()` function in D3 to do it
from within the JavaScript code.

 Can you change these bars to be colored 'steelblue' with the numbers in
 'sans-serif' font? 
 
#### Submit this file on Canvas.




