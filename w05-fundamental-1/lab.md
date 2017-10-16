# Before the class

- Take a look at numpy's random number generators: http://docs.scipy.org/doc/numpy/reference/routines.random.html
- Matplotlib has a `scatter()` function for scatter plot: http://matplotlib.org/api/pyplot_api.html?highlight=scatter#matplotlib.pyplot.scatter
- [Small multiple](https://www.google.com/search?client=safari&rls=en&q=small+multiples&ie=UTF-8&oe=UTF-8)
- Matplotlib's [subplot](https://www.google.com/search?client=safari&rls=en&q=matplotlib+subplot&ie=UTF-8&oe=UTF-8)

# Part 1

https://github.com/yy/dviz-course/blob/master/w05-fundamental-1/w05_lab.ipynb

# Part 2:Introduction to Javascript II

## A simple JS program

Let's start some actual coding with JS. First, we'll write a small JS program that adds 2 numbers.

Create a webpage called "Lab3.html". Make sure that you have the `head` and `body` sections correctly organized.

Inside the `body` section, type the following:

    <script type="text/javascript">
    // JAVASCRIPT CODE GOES HERE
    </script>

Now let's have the program accept some user inputs.

We will need to first create a `form` element in the body section of the HTML code that takes in two numbers as input:

    <form id="myform">
    First number: <input type="text" name="num1"><br /><br />
    Second number: <input type="text" name="num2"><br /><br />
    </form>

Then, we need to make JavaScript "talk" with this form such that the two input numbers are stored in the `num1` and `num2` variables. To do this, first create a function called `adder()` inside the JavaScript section of your code as follows:

	<script type="text/javascript">
		function adder() {
			…
		}
	<script>

Inside this function, add the following line:

	var num1 = parseInt(document.getElementById("myform").elements[0].value);

This line extracts the first number from `myform` and stores it in `num1`. Note that the first number is the first element in the `elements` array. Do the same for num2 by changing the index from 0 to 1.

Additional note: `parseInt` converts the number from the string format (as extracted from the form) into an integer format.

Next, create a variable `total` that stores the sum of the two numbers.

    var total = num1 + num2

To view the output, we can have it printed to the console by the following:

    console.log("num1 = " + num1);

Do the same to print `num2` and `total`.

Finally, we will need to add a trigger in your HTML code - in this case, a ‘Submit’ button right between the form and script elements:

    <button onclick="adder()">Submit</button>


We may also want to write out the result on the webpage. To do this, we need to first create a paragraph. Note that this should be *outside* the Javascript tags:

    <p id="result"></p>

Then add this line *inside* the Javascript tags. It "prints" the result to the webpage by changing the value inside the `result` paragraph.

        document.getElementById("result").innerHTML = "total = " + total;

The full code is as following:

	<!DOCTYPE html>

	<html>
	<head>
	</head>
	<body>

	<form id="myform">
		First number: <input type="text" name="num1"><br><br>
		Second number: <input type="text" name="num2"><br><br>
	</form>

	<p id="result"></p>

	<button onclick="adder()">Submit</button>

	<script type="text/javascript">
	function adder() {
		var num1 = parseInt(document.getElementById("myform").elements[0].value);
		var num2 = parseInt(document.getElementById("myform").elements[1].value);
		var total = num1 + num2;
		console.log("num1 = " + num1 );
		console.log("num2 = " + num2 );
		console.log("total = " + total);
        document.getElementById("result").innerHTML = "total = " + total;

	}

	</script>
	</body>
	</html>
	
## Control sequences in JS

### `if … else` statements

Example:

    if (numOfNodsInClass >= 5) {
      console.log(“Awake”);
    } else {
      console.log(“Asleep”);
    }

In this example, the value stored in `numOfNodsInClass` is checked. If the value is 5 or more, `Awake` will be printed; otherwise `Asleep` will be printed.

### `for` and `while` loops
What would you do if you want to print a series of numbers, say from 1 to 100 to the console? Clearly, writing out 100 `console.log()` statements is not practical. In such instances, you can use iterative constructs such as `for` and `while`. The `for` construct allows for the execution of a block of code `for` a set number of iterations:

	for (var i = 0; i < 5; i++) {
		console.log(i);
	}

In the above statement, a variable called `i` is used as a counter or iterator. The first time the loop is executed, `i = 0`. The second time `i` will be 1. This is because in every iteration, 1 will be added to the current value of `i`. This is indicated by the `i++` part of the statement. This is  essentially shorthand for `i = i + 1`. The middle part of the statement is the stopping condition, i.e. the point at which the program exits the `for` loop. In this case, `console.log()` will be executed until `i = 5`.

The `while` construct allows for the execution of a block of code "while" a certain condition is true:

	var i = 0;
	while (i < 5) {
	  console.log("Awake");
	  i++;
	}
	console.log("Asleep");


## Exercise
Let's modify the add-2-numbers program that we just created. This time we can add multiple numbers. Use only one text entry box and let the user put in numbers repeatedly. Each time when the user clicks the `submit` button, print out the sum of all input numbers on the page. 

Using the control sequences, when the sum is larger than 100, the program should print "process ended" and stop.

Hints
Think about how to store the value of the sum. One way is to store it in the html paragraph we used before:

    <p id="result"></p>

Similar to writing to the `innerHTML`, we can also read from it:

    result = document.getElementById("result").innerHTML


**Save this as a file and submit to Canvas.**
