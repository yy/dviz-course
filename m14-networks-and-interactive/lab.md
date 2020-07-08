
# Gephi and Cytospace

We will introduce two network visualization tools. The first one is Gephi. It can perform a variety of network analysis and can produce pretty visualizations quickly. The downside is that it's currently not well maintained and as a result the installation has become problematic, particularly in the recent systems including Windows 10 and MacOS 10.12+. 

You can download and install Gephi (For Windows users who have trouble installing, see the end of this assignment for one possible solution): [https://gephi.org/](https://gephi.org/). The following is a tutorial made by a previous AI, Nathaniel.

- [gephi tutorial (by Nathaniel Rodriguez)](https://youtu.be/PAoRKtUfUkA)

Depending upon what version of Gephi you use the location of some buttons and tabs may vary, but the general functionality is roughly the same. If you want to know more about Gephi or what file formats it can read/write you can visit their documentation page. You can also check out some other tutorials online.

Another tool is the Cytoscape. It's developed by biologists & bioinformaticians and thus geared towards biological networks. Additionally, it does not have many network analysis functionalities. However, it is more stable and sensible in many ways than Gephi. You can download it at [http://www.cytoscape.org/](http://www.cytoscape.org/) and check out the tutorials at: [https://github.com/cytoscape/cytoscape-tutorials/wiki](https://github.com/cytoscape/cytoscape-tutorials/wiki).

For this assignment, you can choose one from these two, and experiment with a small network. We'll use the Les Miserables graph, which can be downloaded from: [http://www-personal.umich.edu/~mejn/netdata/](http://www-personal.umich.edu/~mejn/netdata/). (Feel free to play with other networks too: [https://github.com/gephi/gephi/wiki/Datasets](https://github.com/gephi/gephi/wiki/Datasets)) 

Once you have the Les Miserables graph,

For Gephi users:
* Load the network into Gephi as an undirected graph
* Use a force-directed layout to obtain a good layout (also play with other layouts)
* Find communities (modules) and color nodes based on the communities
* Tweak various visual encodings to obtain a good visualization. For example - node size, node labels, edge weights etc
* Export to a PDF or a PNG file
* and upload the image file. 

For Cytospace users:
* Load the network into Cytospace
* Apply the edge-weighted spring embedded layout (also play with other layouts such as "organic")
* Color the nodes and tweak various visual encodings to obtain a good visualization
* Export to a PDF or a PNG file
* and upload the image file. 



----

### How to install Gephi on Microsoft Windows with Oracle Java 9 (by Xuan Wang)

Gephi can't find java by default on Windows with JDK 9. 
I don't know whether others have encountered the same problem. So I am writing it down. Hope it is helpful for somebody.

**First**, you need to download and install Oracle Java. We'll use Java 9. (We don't have support for Java 10.)
http://www.oracle.com/technetwork/java/javase/downloads/index.html
Note: You can install JRE or JDK. JRE needs 110MB space and JDK needs 610MB space.

**Second**, follow the link on homework page to download and install Gephi.

**Third**: Configure Gephi. Gephi by default can't find your JRE 9. 
You need to edit `C:\Program Files\Gephi-0.9.2\etc\gephi.conf`, add this line
`jdkhome="C:\Program Files\Java\jre-9.0.4`
Change the path to your java installation path. You are good to go.

Java 9 by default will add `C:\ProgramData\Oracle\Java\javapath\` to `PATH` and write Windows Registry for JRE. CLASS_PATH is obsoleted in Java 9 and JAVA_HOME is not neccesary for most applications since it is reserved for private JRE. Anyway, Gephi simply doesn't buy it. It doesn't recognize JRE 9's javapath folder. 

You may try to set JAVA_HOME, it might work too.

Well, Oracle has changed the directory structure for JRE on Windows. That is why they use javapath instead. If you are using `conf` files or `JRE_HOME/JAVA_HOME`, whenever you upgrade your JRE, the path will change and you have to set it all over again. If Gephi could use the new javapath, upgrdaing java would have no impact on setting.


# Interactive visualizations

## Controlling plot elements

Let's start with this example on Vega editor: [https://vega.github.io/editor/#/examples/vega/scatter-plot-null-values](https://vega.github.io/editor/#/examples/vega/scatter-plot-null-values).

Notice that the drop-down list allows us to choose what to plot in the `x` and `y` fields: IMDB rating, Rottentomatoes rating, worldwide gross, and so on. How to achieve this?

## `Signals` in Vega

From the Vega documentation:

> "Signals are dynamic variables that parameterize a visualization and can drive interactive behaviors." 

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

That's it!


Assignment: add radio buttons to allow changing the color of the points. Your result should look like this:

![example](https://github.com/yy/dviz-course/raw/master/m14-networks-and-interactive/m14_example.png)

**Submit the URL of your work (can be obtained using the webpage's "share" feature).**
    
    
    
