# Before the class

Read the following online tutorial and have a basic understanding of

* [numbers](https://docs.python.org/3.5/tutorial/introduction.html#numbersnumbers) and [strings](https://docs.python.org/3.5/tutorial/introduction.html#strings);
* [if](https://docs.python.org/3.5/tutorial/controlflow.html#if-statements) and [for](https://docs.python.org/3.5/tutorial/controlflow.html#for-statements) statement
* data structure ([lists](https://docs.python.org/3.5/tutorial/introduction.html#lists), [sets](https://docs.python.org/3.5/tutorial/datastructures.html#sets), [dictionaries](https://docs.python.org/3.5/tutorial/datastructures.html#dictionaries))
* [functions](https://docs.python.org/3.5/tutorial/controlflow.html#defining-functions) and [modules](https://docs.python.org/3.5/tutorial/modules.html)

[Google's Python Class](https://developers.google.com/edu/python/?hl=en) is also a nice resource.

# Lab assignment

## Python assignment

* https://github.com/yy/dviz-course/blob/master/w02-history-integrity-review/lab02.ipynb


## html and css practice
### Set up a local web server

Many browsers don't allow loading files locally due to security concerns. We can get around by creating a local web server with Python by the following:

- Open the ‘Command Prompt’.
- Move to the folder where you keep your lab materials by typing `cd <FOLDER_LOCATION>`. We will use this folder as the ‘root’ for our webserver.
- Then type `python -m http.server`.

If successful, you'll see

	Serving HTTP on 0.0.0.0 port 8000 …
	
This means that now your computer is running a webserver and its IP address is 0.0.0.0 and the port is 8000. Now you can open a browser and type "0.0.0.0:8000" on the address bar to connect to this webserver. Equivalently, you can type "localhost:8000". After typing, click on the different links. You can also directly access one of these links by typing in `localhost:8000/NAME_OF_YOUR_FILE.html` in the address bar.

### html review
Webpages are written in a standard markup language called HTML (HyperText Markup Language). The basic syntax of HTML consists of elements enclosed within `<` and `>` symbols. Browsers such as Firefox and Chrome parse these tags and display the content of a webpage in the designated format. This is called rendering.

Here is a list of important tags and their descriptions.

- `html` - Surrounds the entire document.

- `head` - Contains info about the document itself. E.g. the title, any external stylesheets or scripts, etc.

- `title` - Assigns title to page. This title is used while bookmarking.

- `body` - The main part of the document.

- `h1`, `h2`, `h3`, ... - Headings (Smaller the number, larger the size).

- `p` - Paragraph.

- `br` - Line break.

- `em` - emphasize text.

- `strong` or `b` - Bold font.

- `a` - Defines a hyperlink and allows you to link out to the other webpages.

- `img` - Place an image.

- `ul`, `ol`, `li` - Unordered lists with bullets, ordered lists with numbers and each item in list respectively.

- `table`, `th`, `td`, `tr` - Make a table, specifying contents of each cell.

- `<!-->` - Comments – will not be displayed.

- `span` - This will not visibly change anything on the webpage. But it is important while referencing in CSS or JavaScript. It spans a section of text, say, within a paragraph.

- `div` - This will not visibly change anything on the webpage. But it is important while referencing in CSS or JavaScript. It stands for division and allocates a section of a page.

<b>Exercise: Use the top 5 voted movies found in the first part, try the following:

- Create an HTML page. Add a table with the following columns: Movie Title, Year, Rating, Votes. Fill in with the 5 movies' information. Create a link with each movie title to its IMDB page.

- Add a title for the table. Can you change its font and set it to bold?

- Change the background color of the page.

- Add an entry of your favorite movie to the table. Can you set the text to a different color to highlight it?</b>


### CSS review

While HTML directly deals with the content and structure, CSS (Cascading Style Sheets) is the primary language that is used for the look and formatting of a web document.

A CSS stylesheet consists of one or more selectors, properties and values. For example:

	body {   
  	  background-color: white;   
  	  color: steelblue;   
	}
	
Selectors are the HTML elements to which the specific styles (combination of properties and values) will be applied. In the above example, all text within the `body` tags will be in steelblue.

There are three ways to include CSS code in HTML. This is called "referencing".

Embed CSS in HTML - You can place the CSS code within `style` tags inside the `head` tags. This way you can keep everything within a single HTML file but does make the code lengthy.

    <head>  			
        <style type="text/css" 	
        .description {
        font: 16px times-new-roman;
        }
        .viz {
        font: 10px sans-serif;
        } 
        </style>
	
Reference an external stylesheet from HTML - This is a much cleaner way but results in the creation of another file. To do this, you can copy the CSS code into a text file and save it as a .css file in the same folder as the HTML file. In the document head in the HTML code, you can then do the following:

	<head>
 	 <link rel=”stylesheet” href=”stylesheet.css”>
	</head>
	
Attach inline styles - You can also directly attach the styles in-line along with the main HTML code in the body. This makes it easy to customize specific elements but makes the code very messy, because the design and content get mixed up.

	<p style=”color: green; font-size:36px; font-weight:bold;”>
    Inline styles can help when using D3.
    </p>
    
<b>Exercise: make at least 3 more changes to make your web page more attractive using CSS. Show your style!

Test your code by visiting the web page on your local server. Name the .html file with file name "lab02_html_lastname_firstname"", and upload to Canvas.</b>
