# Python-GUI-Testing
This project is an experiment with GUI's in Python in order to better understand how they work and what they are capable of.  

## Inspiration
When messing around with python years ago in my CIS-115 my professor when talking about the power of python brefly touched on how Python could do GUI's with Tkinter, but we never got around to actually doing anything with them other then drawing with turtle. So well at work I decided to mess around with TKinter and try and make a GUI with Tkinter. The idea behind this project is to do the following 4 things
- Config Editing
- Multi-Threading process/parallel processing
- pop up GUI's
- About button showing basic info about the pc and program

One thing id like to highlight is the multi-threading processes/parallel processing. Well this learning excersise is mainly about making GUI's with Tkinter I thought it would be a good idea to try and add support for multi-threading processes/parallel processing since in my mind the most common place you would use those is in GUI's so that things can happen in the background. I plan on making a dedicated learning excersise on multi-threading processes/parallel processing in the future but for now I am going to touch on it here. There is a good chance I dont figure out multi-threading processes/parallel processing in this excersise but it would be nice to try.


## Results
To be honest with you I really didnt learn much from this excersise and will probably come back to improve this so I actually learn more about tkinter. I dont plan on making GUI's for things any time in the near future, but it was good to get some practice in it. I didnt get around to adding a multi-threading process or parallel process since I couldnt find a use for it but I am not very bothered. So what did I learn from this you may be wondering well heres the list
- An actual use for the lambda function which I still dont understand
- How to make pop ups and put elements on the proper window
- A few best practices for tkinter
- Another use for classes

Yea its not a lot but its whatever. Earlier I mentioned I didnt learn much and thats mainly due to the config editor code being stolen from somewhere online (its basically a text editor I just hard coded a file). I envisioned a screen filled with toggle boxes, text boxes, grayed out things, etc. BUT when I was actually making this I realized that it was not going to be possible in my current state. I will probably revist this later and implament this but I relized that there would be a lot of code for the whole thing since I needed to indavidually call each config section but I got lazy. 

### The main window
On the main window there are 4 buttons Config Editor, Make Config, About, and Exit. They are all pretty self explanitory with config editor opening the config file (PLEASE MAKE SURE YOU HAVE A CONFIG.INI IN THE FILE DIRECTORY OR IT WILL BREAK), The Make Config button makes the config file (Please use this before opening the editor), The About button this tells you about the program and some system info (Yes the code was to get the system info was stolen like 90% of this project), and the exit button that kills the program. 

## The conclusion
I am going to be real here, I stole 90% of the code from other places on the internet and stole 5% from my game-tracker repo (just the config stuff). Yes I know it was not effective since I didnt learn much about tkinter but at the same time I did. Its honestly hard to explain but I am honestly glad I did this. I will probably come back and add the config editor of my dreams but thats for future me and when/if I do I will make an update to the readme.
