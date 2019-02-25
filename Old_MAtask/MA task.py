#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.04),
    on April 23, 2018, at 15:40
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
expName = 'MA task'  # from the Builder filename that created this script
expInfo = {u'session': u'', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1536, 864), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "SessionNum"
SessionNumClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Enter Session number',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Ma_Task_Desc"
Ma_Task_DescClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=u'This modular arithmetic (MA) task involves judging the truth value of equations such as 34=22 (mod 4). To solve such equations, the second number is subtracted from the first number(i.e., 34 \u2013 22), and this difference is then divided by the last number, the mod, (i.e., 12 /4). \nIf the resultant is a whole number (here, 3), the statement is True. Problems with remainders are considered False (i.e., 3.5). Hit any key to continue',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Step_1"
Step_1Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Step 1: 34=22 (mod 4)\n\nStep 2: 34-22 -> 12',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Step_2"
Step_2Clock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Step 3: 12/ 4 -> 3\n\nStep 4: 3 is a whole number, so would respond true',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "MA_task_instr"
MA_task_instrClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will now do 12 practice problems that have accuracy feedback after each problem.\nJudge the Truth validity of each problem as quickly as possible without sacrificing accuracy, indicate your response using the z (true) or m (false) keys. Remember to rest your left and right index fingers on the z and m keys, respectively, throughout the experiment.\n',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
trial_text = visual.TextStim(win=win, name='trial_text',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
MA = visual.TextStim(win=win, name='MA',
    text='default text',
    font='Arial',
    pos=[0.0, 0.0], height=0.10, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "practicefeedback"
practicefeedbackClock = core.Clock()
msg=''
text = visual.TextStim(win=win, name='text',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Intertrial"
IntertrialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "practice_over"
practice_overClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='You have completed the practice session. Now you will solve two sets of 24 MA problems with a similar format except without accuracy feedback. Remember to rest your index fingers on the z and m keys.\n\nHit any key to continue\n',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "basetrial"
basetrialClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
base_lineprobs = visual.TextStim(win=win, name='base_lineprobs',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Intertrial2"
Intertrial2Clock = core.Clock()
ISI_2 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "Manipulation"
ManipulationClock = core.Clock()
msg=''
text_2 = visual.TextStim(win=win, name='text_2',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.07, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "exptrial"
exptrialClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
text_9 = visual.TextStim(win=win, name='text_9',
    text='default text',
    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "Intertrial3"
Intertrial3Clock = core.Clock()
ISI_3 = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_3')

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='Arial',
    pos=[0, 0], height=0.3, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "SessionNum"-------
t = 0
SessionNumClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
session_number_key = event.BuilderKeyResponse()
# keep track of which components have finished
SessionNumComponents = [text_14, session_number_key]
for thisComponent in SessionNumComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "SessionNum"-------
while continueRoutine:
    # get current time
    t = SessionNumClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)
    
    # *session_number_key* updates
    if t >= 0.0 and session_number_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        session_number_key.tStart = t
        session_number_key.frameNStart = frameN  # exact frame index
        session_number_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(session_number_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if session_number_key.status == STARTED:
        theseKeys = event.getKeys(keyList=['0', '1'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            session_number_key.keys = theseKeys[-1]  # just the last key pressed
            session_number_key.rt = session_number_key.clock.getTime()
            # was this 'correct'?
            if (session_number_key.keys == str('1')) or (session_number_key.keys == '1'):
                session_number_key.corr = 1
            else:
                session_number_key.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SessionNumComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SessionNum"-------
for thisComponent in SessionNumComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if session_number_key.keys in ['', [], None]:  # No response was made
    session_number_key.keys=None
    # was no response the correct answer?!
    if str('1').lower() == 'none':
       session_number_key.corr = 1  # correct non-response
    else:
       session_number_key.corr = 0  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('session_number_key.keys',session_number_key.keys)
thisExp.addData('session_number_key.corr', session_number_key.corr)
if session_number_key.keys != None:  # we had a response
    thisExp.addData('session_number_key.rt', session_number_key.rt)
thisExp.nextEntry()
# the Routine "SessionNum" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Ma_Task_Desc"-------
t = 0
Ma_Task_DescClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
MA_task_desc_key = event.BuilderKeyResponse()
# keep track of which components have finished
Ma_Task_DescComponents = [text_13, MA_task_desc_key]
for thisComponent in Ma_Task_DescComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Ma_Task_Desc"-------
while continueRoutine:
    # get current time
    t = Ma_Task_DescClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)
    
    # *MA_task_desc_key* updates
    if t >= 5 and MA_task_desc_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        MA_task_desc_key.tStart = t
        MA_task_desc_key.frameNStart = frameN  # exact frame index
        MA_task_desc_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if MA_task_desc_key.status == STARTED:
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
    for thisComponent in Ma_Task_DescComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Ma_Task_Desc"-------
for thisComponent in Ma_Task_DescComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Ma_Task_Desc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Step_1"-------
t = 0
Step_1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Step1_key = event.BuilderKeyResponse()
# keep track of which components have finished
Step_1Components = [text_4, Step1_key]
for thisComponent in Step_1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Step_1"-------
while continueRoutine:
    # get current time
    t = Step_1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0.0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t
        text_4.frameNStart = frameN  # exact frame index
        text_4.setAutoDraw(True)
    
    # *Step1_key* updates
    if t >= 2 and Step1_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        Step1_key.tStart = t
        Step1_key.frameNStart = frameN  # exact frame index
        Step1_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Step1_key.status == STARTED:
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
    for thisComponent in Step_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Step_1"-------
for thisComponent in Step_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Step_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Step_2"-------
t = 0
Step_2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Step2_key = event.BuilderKeyResponse()
# keep track of which components have finished
Step_2Components = [text_6, Step2_key]
for thisComponent in Step_2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Step_2"-------
while continueRoutine:
    # get current time
    t = Step_2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t
        text_6.frameNStart = frameN  # exact frame index
        text_6.setAutoDraw(True)
    
    # *Step2_key* updates
    if t >= 2 and Step2_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        Step2_key.tStart = t
        Step2_key.frameNStart = frameN  # exact frame index
        Step2_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if Step2_key.status == STARTED:
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
    for thisComponent in Step_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Step_2"-------
for thisComponent in Step_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Step_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MA_task_instr"-------
t = 0
MA_task_instrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
MA_task_instr_key = event.BuilderKeyResponse()
# keep track of which components have finished
MA_task_instrComponents = [text_3, MA_task_instr_key]
for thisComponent in MA_task_instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "MA_task_instr"-------
while continueRoutine:
    # get current time
    t = MA_task_instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)
    
    # *MA_task_instr_key* updates
    if t >= 3 and MA_task_instr_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        MA_task_instr_key.tStart = t
        MA_task_instr_key.frameNStart = frameN  # exact frame index
        MA_task_instr_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if MA_task_instr_key.status == STARTED:
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
    for thisComponent in MA_task_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MA_task_instr"-------
for thisComponent in MA_task_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "MA_task_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_trials = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('MA practice problems.xlsx'),
    seed=None, name='Practice_trials')
thisExp.addLoop(Practice_trials)  # add the loop to the experiment
thisPractice_trial = Practice_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
if thisPractice_trial != None:
    for paramName in thisPractice_trial.keys():
        exec(paramName + '= thisPractice_trial.' + paramName)

for thisPractice_trial in Practice_trials:
    currentLoop = Practice_trials
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_trial.rgb)
    if thisPractice_trial != None:
        for paramName in thisPractice_trial.keys():
            exec(paramName + '= thisPractice_trial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    MA.setText(MA_practice)
    trial_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [trial_text, MA, trial_key]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trial_text* updates
        if t >= 0.0 and trial_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_text.tStart = t
            trial_text.frameNStart = frameN  # exact frame index
            trial_text.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if trial_text.status == STARTED and t >= frameRemains:
            trial_text.setAutoDraw(False)
        
        # *MA* updates
        if t >= 0.5 and MA.status == NOT_STARTED:
            # keep track of start time/frame for later
            MA.tStart = t
            MA.frameNStart = frameN  # exact frame index
            MA.setAutoDraw(True)
        frameRemains = 0.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if MA.status == STARTED and t >= frameRemains:
            MA.setAutoDraw(False)
        
        # *trial_key* updates
        if t >= 0.5 and trial_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            trial_key.tStart = t
            trial_key.frameNStart = frameN  # exact frame index
            trial_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(trial_key.clock.reset)  # t=0 on next screen flip
        if trial_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                trial_key.keys = theseKeys[-1]  # just the last key pressed
                trial_key.rt = trial_key.clock.getTime()
                # was this 'correct'?
                if (trial_key.keys == str(corrAns)) or (trial_key.keys == corrAns):
                    trial_key.corr = 1
                else:
                    trial_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if trial_key.keys in ['', [], None]:  # No response was made
        trial_key.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           trial_key.corr = 1  # correct non-response
        else:
           trial_key.corr = 0  # failed to respond (incorrectly)
    # store data for Practice_trials (TrialHandler)
    Practice_trials.addData('trial_key.keys',trial_key.keys)
    Practice_trials.addData('trial_key.corr', trial_key.corr)
    if trial_key.keys != None:  # we had a response
        Practice_trials.addData('trial_key.rt', trial_key.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "practicefeedback"-------
    t = 0
    practicefeedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if trial_key.corr:#stored on last run routine
      msg="Correct"
    else:
      msg="Incorrect"
    text.setText(msg)
    # keep track of which components have finished
    practicefeedbackComponents = [text]
    for thisComponent in practicefeedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practicefeedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practicefeedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text* updates
        if t >= 0.0 and text.status == NOT_STARTED:
            # keep track of start time/frame for later
            text.tStart = t
            text.frameNStart = frameN  # exact frame index
            text.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text.status == STARTED and t >= frameRemains:
            text.setAutoDraw(False)
        
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
    
# completed 1 repeats of 'Practice_trials'

# get names of stimulus parameters
if Practice_trials.trialList in ([], [None], None):
    params = []
else:
    params = Practice_trials.trialList[0].keys()
# save data for this loop
Practice_trials.saveAsExcel(filename + '.xlsx', sheetName='Practice_trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "practice_over"-------
t = 0
practice_overClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
practice_over_key = event.BuilderKeyResponse()
# keep track of which components have finished
practice_overComponents = [text_12, practice_over_key]
for thisComponent in practice_overComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "practice_over"-------
while continueRoutine:
    # get current time
    t = practice_overClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)
    
    # *practice_over_key* updates
    if t >= 2 and practice_over_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        practice_over_key.tStart = t
        practice_over_key.frameNStart = frameN  # exact frame index
        practice_over_key.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if practice_over_key.status == STARTED:
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
    for thisComponent in practice_overComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_over"-------
for thisComponent in practice_overComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "practice_over" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Baseline_block = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Ma task problem bank.xlsx'),
    seed=None, name='Baseline_block')
thisExp.addLoop(Baseline_block)  # add the loop to the experiment
thisBaseline_block = Baseline_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBaseline_block.rgb)
if thisBaseline_block != None:
    for paramName in thisBaseline_block.keys():
        exec(paramName + '= thisBaseline_block.' + paramName)

for thisBaseline_block in Baseline_block:
    currentLoop = Baseline_block
    # abbreviate parameter names if possible (e.g. rgb = thisBaseline_block.rgb)
    if thisBaseline_block != None:
        for paramName in thisBaseline_block.keys():
            exec(paramName + '= thisBaseline_block.' + paramName)
    
    # ------Prepare to start Routine "basetrial"-------
    t = 0
    basetrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    base_lineprobs.setText(MA_baseline)
    basetrial_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    basetrialComponents = [text_7, base_lineprobs, basetrial_key]
    for thisComponent in basetrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "basetrial"-------
    while continueRoutine:
        # get current time
        t = basetrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t
            text_7.frameNStart = frameN  # exact frame index
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
            text_7.setAutoDraw(False)
        
        # *base_lineprobs* updates
        if t >= 0.5 and base_lineprobs.status == NOT_STARTED:
            # keep track of start time/frame for later
            base_lineprobs.tStart = t
            base_lineprobs.frameNStart = frameN  # exact frame index
            base_lineprobs.setAutoDraw(True)
        frameRemains = 0.5 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if base_lineprobs.status == STARTED and t >= frameRemains:
            base_lineprobs.setAutoDraw(False)
        
        # *basetrial_key* updates
        if t >= 0.5 and basetrial_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            basetrial_key.tStart = t
            basetrial_key.frameNStart = frameN  # exact frame index
            basetrial_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(basetrial_key.clock.reset)  # t=0 on next screen flip
        if basetrial_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                basetrial_key.keys = theseKeys[-1]  # just the last key pressed
                basetrial_key.rt = basetrial_key.clock.getTime()
                # was this 'correct'?
                if (basetrial_key.keys == str(corrAns2)) or (basetrial_key.keys == corrAns2):
                    basetrial_key.corr = 1
                else:
                    basetrial_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in basetrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "basetrial"-------
    for thisComponent in basetrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if basetrial_key.keys in ['', [], None]:  # No response was made
        basetrial_key.keys=None
        # was no response the correct answer?!
        if str(corrAns2).lower() == 'none':
           basetrial_key.corr = 1  # correct non-response
        else:
           basetrial_key.corr = 0  # failed to respond (incorrectly)
    # store data for Baseline_block (TrialHandler)
    Baseline_block.addData('basetrial_key.keys',basetrial_key.keys)
    Baseline_block.addData('basetrial_key.corr', basetrial_key.corr)
    if basetrial_key.keys != None:  # we had a response
        Baseline_block.addData('basetrial_key.rt', basetrial_key.rt)
    # the Routine "basetrial" was not non-slip safe, so reset the non-slip timer
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
    
# completed 1 repeats of 'Baseline_block'

# get names of stimulus parameters
if Baseline_block.trialList in ([], [None], None):
    params = []
else:
    params = Baseline_block.trialList[0].keys()
# save data for this loop
Baseline_block.saveAsExcel(filename + '.xlsx', sheetName='Baseline_block',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Manipulation"-------
t = 0
ManipulationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
if session_number_key.corr:
    msg="We are interested in modular mathematics for a reason.As you probably know, math skills are crucial to performance in many important subjects in college. Yet surprisingly little is known about the mental processes underlying math ability. This research is aimed at better understanding what makes some people better at math than others. Your performance on the math problems you are doing today will be compared to other students from across the nation. Hit any button to continue."
else: 
    msg="As you may know, at most schools male students outnumber female students in math majors and majors with math as a prerequisite, and there seems to be a growing gap in academic performance between these groups. A good deal of research indicates that males consistently score higher than females on standardized tests of math ability. But thus far, there is not a good explanation for this. The research you are participating in is aimed at better understanding these differences. Your performance on the math problems you are doing today will be compared to other students from across the nation. One specific question is whether males are superior at all types of math problems or only certain types."

text_2.setText(msg)
Mani_key = event.BuilderKeyResponse()
# keep track of which components have finished
ManipulationComponents = [text_2, Mani_key]
for thisComponent in ManipulationComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Manipulation"-------
while continueRoutine:
    # get current time
    t = ManipulationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)
    
    # *Mani_key* updates
    if t >= 4 and Mani_key.status == NOT_STARTED:
        # keep track of start time/frame for later
        Mani_key.tStart = t
        Mani_key.frameNStart = frameN  # exact frame index
        Mani_key.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(Mani_key.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if Mani_key.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            Mani_key.keys = theseKeys[-1]  # just the last key pressed
            Mani_key.rt = Mani_key.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ManipulationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Manipulation"-------
for thisComponent in ManipulationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if Mani_key.keys in ['', [], None]:  # No response was made
    Mani_key.keys=None
thisExp.addData('Mani_key.keys',Mani_key.keys)
if Mani_key.keys != None:  # we had a response
    thisExp.addData('Mani_key.rt', Mani_key.rt)
thisExp.nextEntry()
# the Routine "Manipulation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
experimental_block = data.TrialHandler(nReps=1, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Ma task problem bank.xlsx'),
    seed=None, name='experimental_block')
thisExp.addLoop(experimental_block)  # add the loop to the experiment
thisExperimental_block = experimental_block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisExperimental_block.rgb)
if thisExperimental_block != None:
    for paramName in thisExperimental_block.keys():
        exec(paramName + '= thisExperimental_block.' + paramName)

for thisExperimental_block in experimental_block:
    currentLoop = experimental_block
    # abbreviate parameter names if possible (e.g. rgb = thisExperimental_block.rgb)
    if thisExperimental_block != None:
        for paramName in thisExperimental_block.keys():
            exec(paramName + '= thisExperimental_block.' + paramName)
    
    # ------Prepare to start Routine "exptrial"-------
    t = 0
    exptrialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_9.setText(MA_exp)
    exptrial_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    exptrialComponents = [text_8, text_9, exptrial_key]
    for thisComponent in exptrialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "exptrial"-------
    while continueRoutine:
        # get current time
        t = exptrialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if t >= 0.0 and text_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_8.tStart = t
            text_8.frameNStart = frameN  # exact frame index
            text_8.setAutoDraw(True)
        frameRemains = 0.0 + .5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_8.status == STARTED and t >= frameRemains:
            text_8.setAutoDraw(False)
        
        # *text_9* updates
        if t >= .5 and text_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_9.tStart = t
            text_9.frameNStart = frameN  # exact frame index
            text_9.setAutoDraw(True)
        frameRemains = .5 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_9.status == STARTED and t >= frameRemains:
            text_9.setAutoDraw(False)
        
        # *exptrial_key* updates
        if t >= 0.5 and exptrial_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            exptrial_key.tStart = t
            exptrial_key.frameNStart = frameN  # exact frame index
            exptrial_key.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(exptrial_key.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if exptrial_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['z', 'm'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                exptrial_key.keys = theseKeys[-1]  # just the last key pressed
                exptrial_key.rt = exptrial_key.clock.getTime()
                # was this 'correct'?
                if (exptrial_key.keys == str(corrAns3)) or (exptrial_key.keys == corrAns3):
                    exptrial_key.corr = 1
                else:
                    exptrial_key.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in exptrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "exptrial"-------
    for thisComponent in exptrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if exptrial_key.keys in ['', [], None]:  # No response was made
        exptrial_key.keys=None
        # was no response the correct answer?!
        if str(corrAns3).lower() == 'none':
           exptrial_key.corr = 1  # correct non-response
        else:
           exptrial_key.corr = 0  # failed to respond (incorrectly)
    # store data for experimental_block (TrialHandler)
    experimental_block.addData('exptrial_key.keys',exptrial_key.keys)
    experimental_block.addData('exptrial_key.corr', exptrial_key.corr)
    if exptrial_key.keys != None:  # we had a response
        experimental_block.addData('exptrial_key.rt', exptrial_key.rt)
    # the Routine "exptrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Intertrial3"-------
    t = 0
    Intertrial3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    Intertrial3Components = [ISI_3]
    for thisComponent in Intertrial3Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Intertrial3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Intertrial3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI_3* period
        if t >= 0.0 and ISI_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI_3.tStart = t
            ISI_3.frameNStart = frameN  # exact frame index
            ISI_3.start(1)
        elif ISI_3.status == STARTED:  # one frame should pass before updating params and completing
            ISI_3.complete()  # finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Intertrial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Intertrial3"-------
    for thisComponent in Intertrial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
# completed 1 repeats of 'experimental_block'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
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
