# Module 5: Design

One of the things that make data visualization fun and interesting is its artistic aspect.
A beautiful visualization may not only pleasing to the eyes, but also can be more effective and engaging in communicating the message.
At the same time, the design principles are not arbitrary, but are based on the human perception and cognition that we covered. 

To think about the importance of design in visualization, let us start with two visualization examples. 
The first one is "Gun deaths in Florida" from Reuters: https://www.businessinsider.com/gun-deaths-in-florida-increased-with-stand-your-ground-2014-2 
This graphic shows the number of murders committed using firearms in Florida for a couple of decades, highlighting the year (2005) when the "Stand Your Ground" law was enacted.
It shows that the number of murders _may_ be increasing after the law was enacted. 
As we discussed earlier, it is hard to conclude anything from this single graph given the complex contexts that this graph does not show.

You may wonder, "wait, what do you mean by _increasing_? I think the number of murders is going down."
Yeah, that's the problem. 
This visualization is super confusing!
The y-axis is flipped—the top is 0 and the bottom is 1,000! 
Indeed, this visualization is often mentioned as one of the most confusing visualizations.

Here is another one: https://www.simonscarr.com/iraqs-bloody-toll 
Sorry for all these morbid examples, but these two are the best examples that I know of. 
It is similar to the previous one, in a sense that it flipped the y-axis and used the same red color. 
However, I would say this visualization is extremely well-done and effective and conveying the message of "bloody toll"!

This visualization also lets us understand the idea behind the first visualization. 
"Ah, the first visualization was trying to have the same effect, representing the number of murders as the blood dripping down!"
Actually, the creator of the first visualization said that they were directly inspired by the second one. 
But the problem is that it failed to do so (spectacularly), not because the data was bad, not because the idea was bad, not because bad visual encodings were used, but because of the design!


## Tufte's Data-ink ratio 

- Tufte, Data-Ink Ratio (Canvas)
- S. Bateman et al., [Useful Junk? The Effects of Visual Embellishment on comprehension and memorability of charts](http://dl.acm.org/citation.cfm?id=1753716), CHI'10
- Thomas Haslwanter, [An Introduction to Statistics: basic principles](http://work.thaslwanter.at/Stats/html/statsBasics.html)
- [The Best Stats You've Ever Seen | Hans Rosling](https://www.youtube.com/watch?v=hVimVzgtD6w)

## More on colors

- [Beginning Graphic Design: Color](https://www.youtube.com/watch?v=_2LLXnUdUIc)
- [Your Friendly Guide to Colors in Data Visualisation](https://lisacharlotterost.github.io/2016/04/22/Colors-for-DataVis/)
- [YYiki: Color](http://yyahnwiki.appspot.com/Color)

## Chartjunk

[Chartjunk](https://en.wikipedia.org/wiki/Chartjunk) has attracted some interests in academia, particularly about their effect on memorability or engagement. 
- Bateman et al., [Useful junk?: the effects of visual embellishment on comprehension and memorability of charts](https://dl.acm.org/doi/pdf/10.1145/1753326.1753716)
- Borkin et al., [What Makes a Visualization Memorable?](https://ieeexplore.ieee.org/iel7/2945/6634084/06634103.pdf)

## Design

- [The Non-Designer's Design Book](http://www.amazon.com/Non-Designers-Design-Book-3rd/dp/0321534042) by Robin Williams concisely and easily explains some of the most fundamental design principles. 
- [99% invisible](http://99percentinvisible.org) is a podcast about "invisible" designs that surround us. It is one of the most fascinating podcast. 

## Data visualization zoo

- [A tour through the visualization zoo](http://queue.acm.org/detail.cfm?id=1743567)
- [The Grammar of Graphics](http://www.amazon.com/The-Grammar-Graphics-Statistics-Computing/dp/0387245448)

## Sparkline

[Sparkline](https://en.wikipedia.org/wiki/Sparkline) is a nice, minimalistic visualization technique that fits perfectly with E. Tufte's minimalism. It is useful when you want to communicate general trends and shapes of many timeseries quickly, particularly within a text. For instance, FiveThirtyEight uses it to display [the historical primary endorsement trends in the text](The Endorsement Primary). 
