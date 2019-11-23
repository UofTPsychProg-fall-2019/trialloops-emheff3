#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build a trial loop Step 2
Use this template to turn Step 1 into a loop
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


#%% your loop here
# start by copying your one trial here, then identify what needs to be
# changed on every trial.  Likely your stimuli, but you might want to change a few things

dirPath = os.getcwd()

# define flower stimuli
flower1 = visual.ImageStim(win, image=dirPath+"/Images/flowers_3333.png")
flower2 = visual.ImageStim(win,image=dirPath+"/Images/flowers_7373.png")
flower3 = visual.ImageStim(win,image=dirPath+"/Images/flowers_7777.png")

# save flowers in a tuple to facilitate looping through them
flowers = (flower1,flower2,flower3)
# create list for responses
responses = []

# define prompt for response
responseText = visual.TextStim(win, "Did the flower like sun (press 'f') or shade (press 'j')?",color='black')

# loop through stimuli
for flower in flowers:
    # first draw a stimuli
    flower.draw()
    # then flip the window
    win.flip()
    # then wait two seconds
    core.wait(2)
    # then display the text
    responseText.draw()
    win.flip()
    core.wait(2)
    # then record the responses
    keys = event.getKeys()
    responses.append(keys)

print(responses)

#%% Required clean up
# this cell will make sure that your window displays for a while and then 
# closes properly

core.wait(2)
win.close()
