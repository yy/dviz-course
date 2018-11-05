# Part 1: Gephi

Gephi is probably the most popular network visualization tool nowadays; it also supports the calculation of basic network statistics. You can download and install Gephi from [here](https://gephi.org/).

Gephi supports CSV, spreadsheet, [GML](https://en.wikipedia.org/wiki/Geography_Markup_Language) and other formats. Some network datasets are available [here](https://github.com/gephi/gephi/wiki/Datasets). Download one of your choice; if you don't know which one to use, the Zachary's karate club is a classic network dataset, you can read its story [here](https://sites.google.com/site/ucinetsoftware/datasets/zacharykarateclub). 

The official tutorial of Gephi is available [here](https://gephi.org/tutorials/gephi-tutorial-quick_start.pdf), it shows many of Gephi's most useful features. ** Go through the tutorial but substitute the Les Miserables network with the network you downloaded (feel free to try other layouts/compute other metrics, etc). Make a screenshot of your final network visualization and submit it to Canvas.**

Note that the tutorial uses an older version of Gephi, so some details may be different, but the main points should be the same.




# Part 2: [Force layout](https://github.com/d3/d3-3.x-api-reference/blob/master/Force-Layout.md) in D3

[Force-directed graph drawing](https://en.wikipedia.org/wiki/Force-directed_graph_drawing) is a class of graph layout algorithms that calculate the positions of each node by simulating an attractive force between each pair of linked nodes, as well as a repulsive force between all nodes. You can think of this as how star and planets in the solar system exert force on each other.

Start with the following HTML tempelate:

    <!DOCTYPE html>
    <html>
    <head>
    </head>
  
    <body>
    <script src="//d3js.org/d3.v3.min.js" charset="utf-8"></script>
    <script type="text/javascript">

    width = 700;
    height = 500;
    
    </script>
    </body>

Let's use a toy network, represented as an edgelist.

    var links = [
    {'source': 'Baratheon', 'target':'Lannister'},
    {'source': 'Baratheon', 'target':'Stark' },
    { 'source': 'Lannister', 'target':'Stark' },
    { 'source': 'Stark', 'target':'Bolton' },
    ];


D3's algorithm requires both nodes and edges, so we'll need to create a variable for the nodes seperately.

    // create empty nodes array
    var nodes = {};
    
    // compute nodes from links data
    links.forEach(function(link) {
        link.source = nodes[link.source] ||
            (nodes[link.source] = {name: link.source});
        link.target = nodes[link.target] ||
            (nodes[link.target] = {name: link.target});        
    });

As before, we create an SVG canvas for our visualization.

    var svg=d3.select('body').append('svg')
        .attr('width', width)
        .attr('height', height);

Then we call `d3.layout.force()` to initiate a force layout.

    var force = d3.layout.force() 
        .size([width, height]) 
        .nodes(d3.values(nodes))
        .links(links)
        .on("tick", tick)
        .linkDistance(300)
        .start(); 
        
`nodes` and `links` adds the notes and links using our data. Each `"tick"` is an iteration; We'll define a function `tick` in the following part so that at each tick, the nodes are pulled towards each other or pushed away from each other to arrive at a distance as close to the `linkDistance` value as possible.

Now we actually add our links and nodes to the visualization:

    var link = svg.selectAll('.link')
        .data(links)
        .enter().append('line')
        .attr('class', 'link'); 

    var node = svg.selectAll('.node')
        .data(force.nodes()) 
        .enter().append('circle')
        .attr('class', 'node')
        .attr('r', width * 0.03); 
        
And define the `tick` function.

    function tick(e) {
        
        node.attr('cx', function(d) { return d.x; })
            .attr('cy', function(d) { return d.y; })
            .call(force.drag);
            
        link.attr('x1', function(d) { return d.source.x; })
            .attr('y1', function(d) { return d.source.y; })
            .attr('x2', function(d) { return d.target.x; })
            .attr('y2', function(d) { return d.target.y; });
        
    }

The `.call(force.drag)` allows you to drag the nodes around. You can try this in your browser. 

** Adapt the code to visualize the Les Miserables network (data is available as `miserables.json` on Canvas, you can also modify the data if you want to). Submit the file to Canvas.**

**Advanced:** Color the nodes based on the `groups` category in the data. You can refer to [Mike Bostock's example](http://bl.ocks.org/mbostock/4062045).


Reference:

[D3 Force Layout Basics](http://bensullins.com/d3-force-layout-basics/)

[Understanding the Force](https://medium.com/@sxywu/understanding-the-force-ef1237017d5#.tf5h2goby)