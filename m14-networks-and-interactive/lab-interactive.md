# Controlling plot elements

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
    
    
    
