# Before the class

- [10 Minutes to pandas](http://pandas.pydata.org/pandas-docs/stable/10min.html)
  - [10-minute tour of pandas (video tutorial)](https://vimeo.com/59324550)
- [Beginner's guide](http://matplotlib.org/users/beginner.html) - follow "Pyplot tutorial" and scheme through other parts. 
- [matplotlib - 2D and 3D plotting in Python](http://nbviewer.ipython.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)

# Lab assignment

## Part 1: Introduction to pandas and matplotlib

- https://github.com/yy/dviz-course/blob/master/w03-viztools/W03Lab.ipynb

## Part 2: Javascript

### What is JavaScript? 

It is the programming language of the web. Because web is becoming the
universal platform for all kinds of stuff, Javascript is also getting more
prominent (see: [The Principle of Least Power][atwood]). 

You can consider that HTML is like a body, CSS is like a clothing, and
Javascript is the puppeteer that makes the body dance. 

Last week, we had talked about HTML and CSS. We thought of them as two layers
that make up a webpage, where HTML is about the content and CSS is about
presentation. Think of JavaScript as the third, "behavior" layer. 

### On an HTML page, where does the JavaScript code go?

Just like CSS, there are multiple ways to do this. But as discussed before, it
is always good to keep the content, style and interactions separated. There are
two ways to do this:

1. Write the JavaScript code within `<script>` tags within the `<head>` or
   `<body>` tags (Figure below - left).

1. Write the code in a separate file and `link` it (Figure below - right). Note
   that, in this case, the file extension will be `.js` instead of `.css`


![where to put javascript code](https://github.com/yy/dviz-course/blob/master/w03-viztools/js_where.png)

### Javascript console

One nice thing about Javascript is you can directly interact with the browser
in a given webpage. Pretty much every browser has "developer tools" (or
something similar) and "Javascript console". For instance, in Chrome browser,
you can find the developer tools here: 

![where to put javascript code](https://github.com/yy/dviz-course/blob/master/w03-viztools/js_where.png)

### Declaring/initializing variables in JavaScript

A variable is a storage location for some value. Here is how you initialize
some basic variable types in JavaScript:

1. Declaring a variable - `var i;`
1. Initializing a numeric variable - `var i = 20;`
1. Initializing a string - `var word = "the word";`
1. Boolean/logical - `var passTheTest = true;`

Variable typing is dynamic, i.e. you do not have to specify whether a variable
is an integer, floating point number, string, etc. Be aware that Javascript is
not particularly good at handling operations that are outside of "normal"
operations: 

![wtf javascript](https://pbs.twimg.com/media/CpZUexOVUAE1Ihb.jpg)



[atwood]: https://blog.codinghorror.com/the-principle-of-least-power/
