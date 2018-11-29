# Gephi

The first part will be introducing you to Gephi, a network visualization software. Go ahead and download and install Gephi (For Windows users who have trouble installing, see the end of this assignment for directions): https://gephi.org/

Cytoscape (http://www.cytoscape.org/) is another tool that you may want to play with if you're interested in network visualization. It's developed by biologists & bioinformaticians and thus geared towards biological networks. However, it is more stable and sensible in many ways than Gephi. 



[gephi tutorial (by Nathaniel Rodriguez)](https://youtu.be/PAoRKtUfUkA)



Depending upon what version of Gephi you use the location of some buttons and tabs may vary, but the general functionality is roughly the same. If you want to know more about Gephi or what file formats it can read/write you can visit their documentation page. You can also check out some other tutorials online.

Now that you have a basic understanding of some of the things Gephi can do, let's draw a network. You can download the Les Miserables graph. (feel free to play with other networks too: [https://github.com/gephi/gephi/wiki/Datasets](https://github.com/gephi/gephi/wiki/Datasets)) 

Once you have the Les Miserables graph,

* Load the network into Gephi as an undirected graph
* Use a force-directed layout to obtain a good layout
* Find communities (modules) and color nodes based on the communities
* Tweak various visual encodings to obtain a good visualization
* Export to a PDF or a PNG file
* and upload the image file. 


----

### How to install Gephi on Microsoft Windows with Oracle Java 9 (by Xuan Wang)

Gephi can't find java by default on Windows with JDK 9. 
I don't know whether others have encountered the same problem. So I am writing it down. Hope it is helpful for somebody.

**First**, you need to download and install Oracle Java. Latest is Java 9. 

http://www.oracle.com/technetwork/java/javase/downloads/index.html

Note; You can install JRE or JDK. JRE needs 110MB space and JDK needs 610MB space.

**Second**, follow the link on homework page to download and install Gephi.

**Third**: Configure Gephi. Gephi by default can't find your JRE 9. 

You need to edit "C:\Program Files\Gephi-0.9.2\etc\gephi.conf", add this line

jdkhome="C:\Program Files\Java\jre-9.0.4"

Change the path to your java installation path. You are good to go.

Java 9 by default will add "C:\ProgramData\Oracle\Java\javapath\" to PATH and write Windows Registry for JRE. CLASS_PATH is obsoleted in Java 9 and JAVA_HOME is not neccesary for most applications since it is reserved for private JRE. Anyway, Gephi simply doesn't buy it. It doesn't recognize JRE 9's javapath folder. 

You may try to set JAVA_HOME, it might work too.

Well, Oracle has changed the directory structure for JRE on Windows. That is why they use javapath instead. If you are using conf files or JRE_HOME/JAVA_HOME, whenever you upgrade your JRE, the path will change and you have to set it all over again. If Gephi could use the new javapath, upgrdaing java would have no impact on setting.


# Interactive visualizations

## Controlling plot elements

Let's start with this example on Vega editor: [https://vega.github.io/editor/#/examples/vega/scatter-plot-null-values](https://vega.github.io/editor/#/examples/vega/scatter-plot-null-values).

Notice that the drop-down list allows us to choose what to plot in the `x` and `y` fields: IMDB rating, Rottentomatoes rating, worldwide gross, and so on. How to achieve this?

## `Signals` in Vega

From the Vega documentation:

>>>"Signals are dynamic variables that parameterize a visualization and can drive interactive behaviors." 

Let's look at the code:

``` 
"signals": [
    { "name": "xField", 
      "value": "IMDB_Rating",
      "bind": {
          "input": "select", 
          "options": [
          "IMDB_Rating", "Rotten_Tomatoes_Rating", 
          "US_Gross", "Worldwide_Gross"
          ]
      }
    },
      ...]
```

`name` is the name of this signal. In this case, `yField` as can be seen in the plot.

`bind` creates the input, in this case, the drop-down list. It can also be a checkbox, a radio button, etc.

Then, we want to use the input to `signal` to update the plot. In this plot, the element to be updated is the `marks`.

```
"marks": [
      {
      "type": "symbol",
      "from": {"data": "valid"},
      "encode": {
        "enter": {
          "size": {"value": 50},
          "tooltip": {"field": "tooltip"}
        },
        "update": {
            "x": {"scale": "xscale", "field": {"signal": "xField"}},
            "y": {"scale": "yscale", "field": {"signal": "yField"}},
            "fill": {"value": "steelblue"},
            "fillOpacity": {"value": 0.5},
            "zindex": {"value": 0}
        },
        "hover": {
            "fill": {"value": "firebrick"},
            "fillOpacity": {"value": 1},
            "zindex": {"value": 1}
        }
      }
    },
    ...
    ]
```
   
In the `update` key, we want to change the `field` of x and y. Previously, we would specify a field as:
    
```
"x": {"scale": "xscale", "field": "IMDB_Rating"}
```
However, here we use the input from the `xField` signal:

```
"x": {"scale": "xscale", "field": {"signal": "xField"}}
```

This is the idea! 

Assignment: add radio buttons to allow changing the color of the points. Your result should look like this:

![example](https://github.com/yy/dviz-course/raw/master/m14-networks-and-interactive/m14_example.png)
    
    
    
