#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 1
Use this template script to present one trial with your desired structure
@author: katherineduncan
"""
#%% Required set up 
# this imports everything you might need and opens a full screen window
# when you are developing your script you might want to make a smaller window 
# so that you can still see your console 
import numpy as np
import pandas as pd
import os, sys
from psychopy import visual, core, event, gui, logging

# open a white full screen window
win = visual.Window(fullscr=True, allowGUI=False, color='white', unit='height') 

# uncomment if you use a clock. Optional because we didn't cover timing this week, 
# but you can find examples in the tutorial code 
#trialClock = core.Clock()

#%% up to you!
# this is where you build a trial that you might actually use one day!
# just try to make one trial ordering your lines of code according to the 
# sequence of events that happen on one trial
# if you're stuck you can use the responseExercise.py answer as a starting point 

# maybe start by making stimulus objects (e.g. myPic = visual.ImageStim(...))  

dirPath = os.getcwd()

# define flower stimuli
flower1 = visual.ImageStim(win, image=dirPath+"/Images/flowers_3333.png")

# define prompt for response
responseText = visual.TextStim(win, "Did the flower like sun (press 'f') or shade (press 'j')?",color='black')


# then draw the stimuli
flower1.draw()
# then flip your window
win.flip()
core.wait(2)
responseText.draw()
win.flip()
core.wait(2)
# then record your responses
key = event.getKeys()

print(key)




#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
