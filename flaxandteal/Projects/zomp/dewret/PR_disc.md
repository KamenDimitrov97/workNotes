remind that I closed out some issues 

in core.py 
from line 40 to 140 

there's a bunch of abstract methods that I'm unsure how to use

Do you have a moment to go over the changes in dewret - somethings I don't understand 

If not:
It looks to me that you're changing the core of dewret which means that it may not make sense to separate the core and the renderers and docs(first more obvious split)

I tried going through the core changes and trying to separate those - incremental core changes in incremental PRs(was the idea)
 - but understanding the whole thing without testing it out incrementally is a bit difficult for me (maybe suggestions on how to handle similar situations might help?)

PR Questions:

`in core.py from line 40 to 140`
There's a bunch of abstract methods with good docstring documentation 
but I don't quite get why they have to be abstract and their usage 
