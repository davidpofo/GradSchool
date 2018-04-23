#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on January 24, 2018, at 11:08
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'ModTask'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date']) 

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\decisionlab\\Desktop\\MT study\\MA task\\ModTask.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1280, 1024), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "MaInstr"
MaInstrClock = core.Clock()
InstrText = visual.TextStim(win=win, name='InstrText',
    text=u'In this task your job is to judge whether the problems are "true" or "false" as quickly and accurately as possible.You are going to see problems on the screen that look like the following: 44\u226118 (mod 2)\n\nTo solve such equations, you subtract the second number from the first (i.e., 44 \u2013 18), and then the difference is divided by the last number,(i.e., 26 /2). \n\nIf the resultant is a whole number (here, 13), the statement is True.Problems with remainders are considered False (i.e., 13.5).\n\n Hit any key to continue',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "MaInstr2"
MaInstr2Clock = core.Clock()
InstrText2 = visual.TextStim(win=win, name='InstrText2',
    text=u"Here's another example \nIs the following statement true?:\n36\u226119 (mod 2)\n\nFirst we subtract 19 from 36:\n36 \u2013 19 = 17\nDoes 2 divide 17 with 0 as the remainder? \n\nSecond we divide the resultant by the mod number: \n17/2 = 8.5\nNo, 2 goes into 17 8.5 times, with a remainder of Five. \n\nThus our statement is False. \n\nHit any key to continue",
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "MaInstr3"
MaInstr3Clock = core.Clock()
InstrText3 = visual.TextStim(win=win, name='InstrText3',
    text='You will now do a set of practice problems that have accuracy feedback after each problem.\nJudge the truth validity of each problem as quickly as possible without sacrificing accuracy, indicate your response using the z (true) or m (false) keys. Remember to rest your left and right index fingers on the z and m keys, respectively, throughout the experiment.\n\nHit any key to start',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "PracticeTrial"
PracticeTrialClock = core.Clock()
PracticeCross = visual.TextStim(win=win, name='PracticeCross',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
PracticeText = visual.TextStim(win=win, name='PracticeText',
    text='default text',
    font='Arial',
    pos=[0.0, 0.0], height=0.10, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "practicefeedback"
practicefeedbackClock = core.Clock()
msg=''
PracticeFeedbackText = visual.TextStim(win=win, name='PracticeFeedbackText',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Intertrial"
IntertrialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "PracticeOver"
PracticeOverClock = core.Clock()
PracticeOverText = visual.TextStim(win=win, name='PracticeOverText',
    text='You have completed the practice session. Now you will solve MA problems with a similar format except without accuracy feedback. Remember to rest your index fingers on the z and m keys.\n\nHit any key to continue\n',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "TestTrial"
TestTrialClock = core.Clock()
TestCross = visual.TextStim(win=win, name='TestCross',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
TestText = visual.TextStim(win=win, name='TestText',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Intertrial2"
Intertrial2Clock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "Thanks"
ThanksClock = core.Clock()
ThanksText = visual.TextStim(win=win, name='ThanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "MaInstr"-------
t = 0
MaInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrKey = event.BuilderKeyResponse()
# keep track of which components have finished
MaInstrComponents = [InstrText, InstrKey]
for thisComponent in MaInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MaInstr"-------
while continueRoutine:
    # get current time
    t = MaInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText* updates
    if t >= 0.0 and InstrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText.tStart = t
        InstrText.frameNStart = frameN  # exact frame index
        InstrText.setAutoDraw(True)
    
    # *InstrKey* updates
    if t >= 2 and InstrKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrKey.tStart = t
        InstrKey.frameNStart = frameN  # exact frame index
        InstrKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if InstrKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MaInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MaInstr"-------
for thisComponent in MaInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MaInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MaInstr2"-------
t = 0
MaInstr2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrKey2 = event.BuilderKeyResponse()
# keep track of which components have finished
MaInstr2Components = [InstrText2, InstrKey2]
for thisComponent in MaInstr2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MaInstr2"-------
while continueRoutine:
    # get current time
    t = MaInstr2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText2* updates
    if t >= 0.0 and InstrText2.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText2.tStart = t
        InstrText2.frameNStart = frameN  # exact frame index
        InstrText2.setAutoDraw(True)
    
    # *InstrKey2* updates
    if t >= 2 and InstrKey2.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrKey2.tStart = t
        InstrKey2.frameNStart = frameN  # exact frame index
        InstrKey2.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if InstrKey2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MaInstr2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MaInstr2"-------
for thisComponent in MaInstr2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MaInstr2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MaInstr3"-------
t = 0
MaInstr3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
InstrKey3 = event.BuilderKeyResponse()
# keep track of which components have finished
MaInstr3Components = [InstrText3, InstrKey3]
for thisComponent in MaInstr3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MaInstr3"-------
while continueRoutine:
    # get current time
    t = MaInstr3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *InstrText3* updates
    if t >= 0.0 and InstrText3.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrText3.tStart = t
        InstrText3.frameNStart = frameN  # exact frame index
        InstrText3.setAutoDraw(True)
    
    # *InstrKey3* updates
    if t >= 2 and InstrKey3.status == NOT_STARTED:
        # keep track of start time/frame for later
        InstrKey3.tStart = t
        InstrKey3.frameNStart = frameN  # exact frame index
        InstrKey3.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if InstrKey3.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MaInstr3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MaInstr3"-------
for thisComponent in MaInstr3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MaInstr3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeBlock = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MA practice problems.xlsx'),
    seed=None, name='PracticeBlock')
thisExp.addLoop(PracticeBlock)  # add the loop to the experiment
thisPracticeBlock = PracticeBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeBlock.rgb)
if thisPracticeBlock != None:
    for paramName in thisPracticeBlock.keys():
        exec(paramName + '= thisPracticeBlock.' + paramName)

for thisPracticeBlock in PracticeBlock:
    currentLoop = PracticeBlock
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeBlock.rgb)
    if thisPracticeBlock != None:
        for paramName in thisPracticeBlock.keys():
            exec(paramName + '= thisPracticeBlock.' + paramName)
    
    # ------Prepare to start Routine "PracticeTrial"-------
    t = 0
    PracticeTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    PracticeText.setText(MA_practice)
    PracticeKey = event.BuilderKeyResponse()
    # keep track of which components have finished
    PracticeTrialComponents = [PracticeCross, PracticeText, PracticeKey]
    for thisComponent in PracticeTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PracticeTrial"-------
    while continueRoutine:
        # get current time
        t = PracticeTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PracticeCross* updates
        if t >= 0.0 and PracticeCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            PracticeCross.tStart = t
            PracticeCross.frameNStart = frameN  # exact frame index
            PracticeCross.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PracticeCross.status == STARTED and t >= frameRemains:
            PracticeCross.setAutoDraw(False)
        
        # *PracticeText* updates
        if t >= 0.5 and PracticeText.status == NOT_STARTED:
            # keep track of start time/frame for later
            PracticeText.tStart = t
            PracticeText.frameNStart = frameN  # exact frame index
            PracticeText.setAutoDraw(True)
        frameRemains = 0.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PracticeText.status == STARTED and t >= frameRemains:
            PracticeText.setAutoDraw(False)
        
        # *PracticeKey* updates
        if t >= 0.5 and PracticeKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            PracticeKey.tStart = t
            PracticeKey.frameNStart = frameN  # exact frame index
            PracticeKey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(PracticeKey.clock.reset)  # t=0 on next screen flip
        if PracticeKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                PracticeKey.keys = theseKeys[-1]  # just the last key pressed
                PracticeKey.rt = PracticeKey.clock.getTime()
                # was this 'correct'?
                if (PracticeKey.keys == str(corrAns)) or (PracticeKey.keys == corrAns):
                    PracticeKey.corr = 1
                else:
                    PracticeKey.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeTrial"-------
    for thisComponent in PracticeTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if PracticeKey.keys in ['', [], None]:  # No response was made
        PracticeKey.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           PracticeKey.corr = 1  # correct non-response
        else:
           PracticeKey.corr = 0  # failed to respond (incorrectly)
    # store data for PracticeBlock (TrialHandler)
    PracticeBlock.addData('PracticeKey.keys',PracticeKey.keys)
    PracticeBlock.addData('PracticeKey.corr', PracticeKey.corr)
    if PracticeKey.keys != None:  # we had a response
        PracticeBlock.addData('PracticeKey.rt', PracticeKey.rt)
    # the Routine "PracticeTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practicefeedback"-------
    t = 0
    practicefeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if PracticeKey.corr:#stored on last run routine
      msg="Correct"
    else:
      msg="Incorrect"
    PracticeFeedbackText.setText(msg)
    # keep track of which components have finished
    practicefeedbackComponents = [PracticeFeedbackText]
    for thisComponent in practicefeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practicefeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practicefeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *PracticeFeedbackText* updates
        if t >= 0.0 and PracticeFeedbackText.status == NOT_STARTED:
            # keep track of start time/frame for later
            PracticeFeedbackText.tStart = t
            PracticeFeedbackText.frameNStart = frameN  # exact frame index
            PracticeFeedbackText.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PracticeFeedbackText.status == STARTED and t >= frameRemains:
            PracticeFeedbackText.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practicefeedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practicefeedback"-------
    for thisComponent in practicefeedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    
    # ------Prepare to start Routine "Intertrial"-------
    t = 0
    IntertrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    IntertrialComponents = [ISI]
    for thisComponent in IntertrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intertrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = IntertrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(1)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            ISI.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in IntertrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intertrial"-------
    for thisComponent in IntertrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeBlock'

# get names of stimulus parameters
if PracticeBlock.trialList in ([], [None], None):
    params = []
else:
    params = PracticeBlock.trialList[0].keys()
# save data for this loop
PracticeBlock.saveAsExcel(filename + '.xlsx', sheetName='PracticeBlock',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "PracticeOver"-------
t = 0
PracticeOverClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
PracticeOverKey = event.BuilderKeyResponse()
# keep track of which components have finished
PracticeOverComponents = [PracticeOverText, PracticeOverKey]
for thisComponent in PracticeOverComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PracticeOver"-------
while continueRoutine:
    # get current time
    t = PracticeOverClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PracticeOverText* updates
    if t >= 0.0 and PracticeOverText.status == NOT_STARTED:
        # keep track of start time/frame for later
        PracticeOverText.tStart = t
        PracticeOverText.frameNStart = frameN  # exact frame index
        PracticeOverText.setAutoDraw(True)
    
    # *PracticeOverKey* updates
    if t >= 2 and PracticeOverKey.status == NOT_STARTED:
        # keep track of start time/frame for later
        PracticeOverKey.tStart = t
        PracticeOverKey.frameNStart = frameN  # exact frame index
        PracticeOverKey.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if PracticeOverKey.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PracticeOverComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PracticeOver"-------
for thisComponent in PracticeOverComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "PracticeOver" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
TestBlock = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Ma task problem bank.xlsx'),
    seed=None, name='TestBlock')
thisExp.addLoop(TestBlock)  # add the loop to the experiment
thisTestBlock = TestBlock.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTestBlock.rgb)
if thisTestBlock != None:
    for paramName in thisTestBlock.keys():
        exec(paramName + '= thisTestBlock.' + paramName)

for thisTestBlock in TestBlock:
    currentLoop = TestBlock
    # abbreviate parameter names if possible (e.g. rgb = thisTestBlock.rgb)
    if thisTestBlock != None:
        for paramName in thisTestBlock.keys():
            exec(paramName + '= thisTestBlock.' + paramName)
    
    # ------Prepare to start Routine "TestTrial"-------
    t = 0
    TestTrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    TestText.setText(MA_test
)
    TestKey = event.BuilderKeyResponse()
    # keep track of which components have finished
    TestTrialComponents = [TestCross, TestText, TestKey]
    for thisComponent in TestTrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "TestTrial"-------
    while continueRoutine:
        # get current time
        t = TestTrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *TestCross* updates
        if t >= 0.0 and TestCross.status == NOT_STARTED:
            # keep track of start time/frame for later
            TestCross.tStart = t
            TestCross.frameNStart = frameN  # exact frame index
            TestCross.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if TestCross.status == STARTED and t >= frameRemains:
            TestCross.setAutoDraw(False)
        
        # *TestText* updates
        if t >= 0.5 and TestText.status == NOT_STARTED:
            # keep track of start time/frame for later
            TestText.tStart = t
            TestText.frameNStart = frameN  # exact frame index
            TestText.setAutoDraw(True)
        frameRemains = 0.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if TestText.status == STARTED and t >= frameRemains:
            TestText.setAutoDraw(False)
        
        # *TestKey* updates
        if t >= 0.5 and TestKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            TestKey.tStart = t
            TestKey.frameNStart = frameN  # exact frame index
            TestKey.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(TestKey.clock.reset)  # t=0 on next screen flip
        if TestKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                TestKey.keys = theseKeys[-1]  # just the last key pressed
                TestKey.rt = TestKey.clock.getTime()
                # was this 'correct'?
                if (TestKey.keys == str(corrAns2)) or (TestKey.keys == corrAns2):
                    TestKey.corr = 1
                else:
                    TestKey.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TestTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TestTrial"-------
    for thisComponent in TestTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if TestKey.keys in ['', [], None]:  # No response was made
        TestKey.keys=None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           TestKey.corr = 1  # correct non-response
        else:
           TestKey.corr = 0  # failed to respond (incorrectly)
    # store data for TestBlock (TrialHandler)
    TestBlock.addData('TestKey.keys',TestKey.keys)
    TestBlock.addData('TestKey.corr', TestKey.corr)
    if TestKey.keys != None:  # we had a response
        TestBlock.addData('TestKey.rt', TestKey.rt)
    # the Routine "TestTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Intertrial2"-------
    t = 0
    Intertrial2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Intertrial2Components = [ISI_2]
    for thisComponent in Intertrial2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intertrial2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Intertrial2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI_2* period
        if t >= 0.0 and ISI_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_2.tStart = t
            ISI_2.frameNStart = frameN  # exact frame index
            ISI_2.start(1)
        elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
            ISI_2.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intertrial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intertrial2"-------
    for thisComponent in Intertrial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'TestBlock'

# get names of stimulus parameters
if TestBlock.trialList in ([], [None], None):
    params = []
else:
    params = TestBlock.trialList[0].keys()
# save data for this loop
TestBlock.saveAsExcel(filename + '.xlsx', sheetName='TestBlock',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Thanks"-------
t = 0
ThanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ThanksComponents = [ThanksText]
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *ThanksText* updates
    if t >= 0.0 and ThanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        ThanksText.tStart = t
        ThanksText.frameNStart = frameN  # exact frame index
        ThanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if ThanksText.status == STARTED and t >= frameRemains:
        ThanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Thanks"-------
for thisComponent in ThanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
