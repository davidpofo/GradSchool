#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on April 23, 2018, at 16:12
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
expName = 'Shapebuilder_8_8_2016'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
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

# Initialize components for Routine "ShapebuilderFunction"
ShapebuilderFunctionClock = core.Clock()



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "ShapebuilderFunction"-------
t = 0
ShapebuilderFunctionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
#

def ShapeBuilderFunction(**OptionalParameters):

    #
    #####################   MODULES TO IMPORT
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    #
    import math
    import numpy as np
    import random
    from psychopy import visual, info, core
    from sys import platform as _platform
    import numbers

#    jeopardy = sound.SoundPyo(volume = 1)
#    jeopardy.setSound('jeopardy.wav')
#    expInfo = info.RunTimeInfo(refreshTest = None)
#    versionNum = int(str(expInfo['psychopyVersion']).replace('.',''))

    #
    #####################   Functions
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    #
    def EucDist(Pos1,Pos2):
        return math.sqrt(abs(Pos1[0]-Pos2[0])**2 + abs(Pos1[1]-Pos2[1])**2)

    def shift(seq, n):
        n = n % len(seq)
        return seq[n:] + seq[:n]

    def DrawStimuliFlip(WhatToDisplay,Window):
        [curImage.draw() for curImage in WhatToDisplay]
        Window.flip()

    def AngleCalc(Rad,Xorigin,Yorigin,YCorrectionFactor,AngleNum,Start):
        X=Start - float(360)/AngleNum
        Degrees = []
        for i in range(0,AngleNum):
            X = X + float(360)/AngleNum
            Degrees.append(X)
        Degrees=np.array(Degrees)
        Xcoordinates=Xorigin + np.cos(np.deg2rad(Degrees)) * Rad
        Ycoordinates=Yorigin + np.sin(np.deg2rad(Degrees)) * Rad * YCorrectionFactor
        return (zip(Xcoordinates,Ycoordinates))

    #This is just used because I have had problems with the mouse 
    #when switching between macs and windows. The main issue is that
    #event.Mouse() has issues if a window (e.g., event.Mouse(win =myWindow) is not supplied on windows machines
    #however, on macs specifying the window causes problems, but only on older versions 
    #of psychopy...what a mess. On a mac, with new versions (>1.82..I think!), you need to specify the window.
    #Thus, this function gets what the version.
    def DetermineSystemType(psychopyVersion):
        if _platform == "linux" or _platform == "linux2":
            core.quit()
        elif _platform == "darwin":
            if versionNum <= 18201:
                compType = 'mac'
            else:
                compType = 'pc'
        elif _platform == "win32":
            compType = 'pc'
        else:
            compType = 'pc'
        return(compType)


    ################# Optional Paramaeter Stuff
    #########################################################################################################
    #########################################################################################################
    #########################################################################################################
    #Do you want to write data to the file
    if 'writeData' in OptionalParameters:
        WriteData = OptionalParameters['writeData']
        if WriteData not in [True,False]:
            print('Only True or False are possible parameters for writeData brahh!')
    elif 'writeData' not in OptionalParameters:
        WriteData = True

    if 'numPracTrials' in OptionalParameters:
        if isinstance(OptionalParameters['numPracTrials'],numbers.Number):
            if OptionalParameters['numPracTrials'] < 27 and OptionalParameters['numPracTrials'] > -1:
                numPracticeTrials = int(OptionalParameters['numPracTrials'])
            elif OptionalParameters['numPracTrials'] < 0 or OptionalParameters['numPracTrials'] > 26:
                print('Please enter a non-negative integer for the number of practice trials that is less than 26.')
                core.quit()
        else:
            print('Please enter a single number for "numPracTrials".')
            core.quit()
    elif 'numPracTrials' not in OptionalParameters:
        numPracticeTrials = 6


    if 'win' in OptionalParameters:
        window = OptionalParameters['win']
    elif 'win' not in OptionalParameters:
        window = visual.Window(fullscr=True,monitor='Default',units='norm',colorSpace='rgb')

    #Had to include this because I was having trouble 
    #automatically detecting the version type on windows machines.
    if 'computerAndVersionType' in OptionalParameters:
        if OptionalParameters['computerAndVersionType'] == 'pc':
            myMouse = event.Mouse(win=window)
        elif OptionalParameters['computerAndVersionType'] == 'mac':
            myMouse = event.Mouse(win=window)
        elif OptionalParameters['computerAndVersionType'] == 'macOld':
            myMouse = event.Mouse()
        else:
            print('Not a valid option for "computerAndVersionType" -- "pc", "mac", or "macOld" d00d.')
            core.quit()
    elif 'computerAndVersionType' not in OptionalParameters:
        myMouse = event.Mouse(win=window)

    if 'physicalMonSize' in OptionalParameters:
        screenRez = win.size
        physicalMonSize = OptionalParameters['physicalMonSize']
        yCorrFactor = float(physicalMonSize[0])/physicalMonSize[1]
    elif 'physicalMonSize' not in OptionalParameters:
        yCorrFactor = 1.6


    background = visual.Rect(window, size=(window.size)*2, fillColor=(-1.0,-1.0,-1.0))
    #Enter monitor size in cm. If left at [0,0] it is assumed that
    #1 pixel on the x axis is the same size as 1 pixel on the y axis
    monSize=[0,0]

    shapeLWidth=3
    lineCol=[-1,-1,-1]

    trialNum = 0 
    curMemSize=2
    startShapeDur=0.7
    curScore = 0
    curMemTrial = 0
    timeBetweenShapes = 0.5
    
    if numPracticeTrials == 0:
        numTimesThroughSB = 1
    else:
        numTimesThroughSB = 2

    timesThrough = 0
    whenToChange = [3,6,9]

    difColors=[
    [ 1, 1,-1],
    [-1,-1, 1],
    [ 1,-1,-1],
    [-1, 1,-1]
    ]

#    edges=[[-0.32,0.32],[0.32,0.32],[0.32,-0.32],[-0.32,-0.32]]
    edges=[[-0.25,0.25],[0.25,0.25],[0.25,-0.25],[-0.25,-0.25]]
    edges=[[curEdge[0],curEdge[1]*yCorrFactor] for curEdge in edges]

    Ydist=float(max(edges[0][0],edges[2][0]) - min(edges[0][0],edges[2][0]))/5*yCorrFactor
    Xdist=float(max(edges[1][0],edges[3][0]) - min(edges[1][0],edges[3][0]))/5

    outerRect=visual.Rect(window,lineWidth=0,lineColor=(-0.6,-0.6,-0.6),fillColor=(0,0,0),width=abs(edges[0][0])*5,height=abs(edges[0][0])*4*yCorrFactor,pos=(0,0))
    outerRectShapeColor = visual.Rect(window,lineWidth=0,fillColor=[-0.2,-0.2,-0.2],width=abs(edges[0][0])*5*1.01,height=abs(edges[0][0])*4*yCorrFactor*1.01,pos=outerRect.pos,opacity=0.4)
    defRectColor = outerRectShapeColor.fillColor

    triangleDistX=0.052
    triangleDistY=triangleDistX * yCorrFactor

    realTriDistX = triangleDistX * 0.8
    realTriDistY = triangleDistY * 1.45
    triangleYAdj = 2.9

    if yCorrFactor > 1.3:
        textSizeInc = 0.65
        realTriDistX = triangleDistX * 0.8
        realTriDistY = triangleDistY * 1.45
        triangleYAdj = 2.9
    else:
        textSizeInc = 0.45
        realTriDistX = triangleDistX * 0.8
        realTriDistY = triangleDistY * 1.65
        triangleYAdj = 2.5


    pushOut = 1.05

    allPos = []
    cenPos = []
    for i in range(0,len(edges)):
        curPos=[]
        if i == 0 or i== 2:
            curEdgeDist = float(max(edges[i][0],edges[i+1][0]) - min(edges[i][0],edges[i+1][0]))/5
            float(max(edges[i][0],edges[i+1][0]) - min(edges[i][0],edges[i+1][0]))/2
            if i == 0:
                for j in range(1,5):
                    curPos.append([edges[i][0] + curEdgeDist*j,edges[i][1]])
            else:
                for j in range(1,5):
                    curPos.append([edges[i][0] - curEdgeDist*j,edges[i][1]])
                curPos=curPos[::-1]
        elif i == 1:
            curEdgeDist = float(max(edges[i][1],edges[i+1][1]) - min(edges[i][1],edges[i+1][1]))/5
            for j in range(1,5):
                curPos.append([edges[i][0], edges[i][1] - curEdgeDist*j])
        else:
            curEdgeDist = float(max(edges[3][1],edges[0][1]) - min(edges[3][1],edges[0][1]))/5
            for j in range(1,5):
                curPos.append([edges[i][0], edges[i][1] + curEdgeDist*j])
            curPos=curPos[::-1]
        allPos.append(curPos)
    for i in range(len(allPos)):
        for j in range(len(allPos[i])):
            for k in range(1):
                if i == 0 or i == 2:
                    allPos[i][j][1] = float(allPos[i][j][1]) * pushOut
                else:
                    allPos[i][j][0] = float(allPos[i][j][0]) * pushOut


    squareOutlinePos=[]

    allSquarePos=[]
    allXSqPos=[]
    allYSqPos=[]
    yTempStart = edges[0][0]
    for i in range(1,5):
        allXSqPos.append(edges[0][0]+Xdist*i)
        allYSqPos.append(-edges[0][1]+Ydist*i)

    for i in range(0,len(allYSqPos)):
        for j in range(0,len(allXSqPos)):
            allSquarePos.append([allXSqPos[j],allYSqPos[i]])

    allSquareRect=[]
    for i in range(0,len(allSquarePos)):
        allSquareRect.append(visual.Rect(window,lineWidth=shapeLWidth*2,lineColor=lineCol,fillColor=(0.4,0.4,0.4),width=Xdist,height=Ydist,pos=allSquarePos[i]))


    scoreRect=visual.Rect(window,lineWidth=shapeLWidth*2,lineColor=lineCol,fillColor=(0.45,0.45,0.45),width=Xdist*2.5,height=Ydist*0.8,pos=(0,edges[0][1]*1.5))

    scoreNum=visual.TextStim(window, text=curScore,color = (-1,0.2,0.2),pos=scoreRect.pos,height=Ydist*0.7)
    scoreLabel=visual.TextStim(window, text="Score",color = 'black',pos=(scoreRect.pos[0],scoreRect.pos[1]+Ydist*0.8),height=Ydist*0.5)

    scoreValueTexts=[visual.TextStim(window, text=0,color = (-1,-1,-1),pos=scoreRect.pos,height=Ydist*0.6) for i in range(0,4)]

    beginRect=visual.Rect(window,lineWidth=shapeLWidth*2,lineColor=lineCol,fillColor=(0,0.3,0.8),width=Xdist*2,height=Ydist*0.8,pos=(0.2,edges[0][1]*-1.5))
    beginText=visual.TextStim(window, text="Begin",color = (-1,-1,-1),pos=beginRect.pos,height=Ydist*0.5)

    practiceRect=visual.Rect(window,lineWidth=shapeLWidth*2,lineColor=lineCol,fillColor=(0,0.3,0.8),width=Xdist*2,height=Ydist*0.8,pos=(-beginRect.pos[0],edges[0][1]*-1.5))
    practiceText=visual.TextStim(window, text="Practice",color = (-1,-1,-1),pos=practiceRect.pos,height=beginText.height)

    rectangles=[]
    testRect=[]
    unRect=[]
    for i in range(0,len(edges)):
        curPos=allPos[i][0]
        rectangles.append(visual.Rect(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],width=triangleDistX*1.4,height=triangleDistY*1.4,pos=curPos))
        testRect.append(visual.Rect(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],width=triangleDistX*1.4,height=triangleDistY*1.4,pos=curPos))
        unRect.append(visual.Rect(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],width=triangleDistX*1.4,height=triangleDistY*1.4,pos=curPos))

    circles=[]
    testCircles=[]
    unCircles=[]
    for i in range(0,len(edges)):
        curPos=allPos[i][1]
        curVertices = AngleCalc(float(triangleDistX)/2*1.5,0,0,yCorrFactor,90,-90)
        circles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))
        testCircles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))
        unCircles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))




    triangles=[]
    testTriangles=[]
    unTriangles=[]
    for i in range(0,len(edges)):
        curPos=allPos[i][2]
        triangles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i], \
                        vertices=((-realTriDistX,-float(realTriDistX)/2*triangleYAdj),(0,float(realTriDistY)/2),(realTriDistX,-float(realTriDistX)/2*triangleYAdj)), closeShape=True, pos=curPos))
        testTriangles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i], \
                        vertices=((-realTriDistX,-float(realTriDistX)/2*triangleYAdj),(0,float(realTriDistY)/2),(realTriDistX,-float(realTriDistX)/2*triangleYAdj)), closeShape=True, pos=curPos))
        unTriangles.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i], \
                        vertices=((-realTriDistX,-float(realTriDistX)/2*triangleYAdj),(0,float(realTriDistY)/2),(realTriDistX,-float(realTriDistX)/2*triangleYAdj)), closeShape=True, pos=curPos))


    diamonds=[]
    testDiamonds=[]
    unDiamonds=[]
    diamondCorrX = 1.15
    diamondCorrY = 1.6
    for i in range(0,len(edges)):
        curPos=allPos[i][3]
        curVertices = [[0,float(triangleDistY)*diamondCorrY/2],[float(triangleDistX)*diamondCorrX/2,0],[0,-(float(triangleDistY)*diamondCorrY/2)],[-(float(triangleDistX)*diamondCorrX/2),0]]
        diamonds.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))
        testDiamonds.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))
        unDiamonds.append(visual.ShapeStim(window,lineWidth=shapeLWidth,lineColor=lineCol,fillColor=difColors[i],vertices=curVertices,pos=curPos))

    instRect = visual.Rect(window,lineWidth=shapeLWidth,lineColor='black',fillColor=(0,0,0),width=Xdist*4,height=Ydist*4,pos=(0,0),opacity=0.9)

    borderingRects = []
    borderingRects2 = []
    for i in range(0,len(edges)):
        if i == 0 or i ==2:
            curPos=[edges[i][0]*pushOut,0]
            curXSize = Xdist
            curYSize = Ydist*4
        else:
            curPos=[0,edges[i][1]*pushOut]
            curXSize = Xdist*4
            curYSize = Ydist
            
        borderingRects.append(visual.Rect(window,lineWidth=0,lineColor='black',fillColor=(0,0,0),width=curXSize,height=curYSize,pos=curPos,opacity=0.6))
        borderingRects2.append(visual.Rect(window,lineWidth=shapeLWidth,lineColor='black',fillColor=(0.4,0.4,0.4),width=curXSize,height=curYSize,pos=curPos))




    allShapes=[]
    testShapes=[]
    unShapes=[]
    for i in range(0,4):
        allShapes.append(rectangles[i])
        allShapes.append(circles[i])
        allShapes.append(triangles[i])
        allShapes.append(diamonds[i])
        testShapes.append(testRect[i])
        testShapes.append(testCircles[i])
        testShapes.append(testTriangles[i])
        testShapes.append(testDiamonds[i])
        unShapes.append(unRect[i])
        unShapes.append(unCircles[i])
        unShapes.append(unTriangles[i])
        unShapes.append(unDiamonds[i])


    allPosFlat=np.array(allPos)
    allPosFlat=np.reshape(allPosFlat,(allPosFlat.shape[0]*allPosFlat.shape[1],allPosFlat.shape[2]))
    allPosFlat=allPosFlat.tolist()

    allStimNoPres = []
    allStimNoPres.extend([outerRectShapeColor,outerRect,scoreRect,scoreLabel,scoreNum])
    for i in range(len(allSquareRect)):
        allStimNoPres.append(allSquareRect[i])
    [allStimNoPres.append(borderingRects2[i]) for i in range(len(borderingRects2))]
    for i in range(len(allShapes)):
        allStimNoPres.append(allShapes[i])


    ####################### Outer loop starts here
    for outerLoop in range(numTimesThroughSB):

        curScore = 0

        instructions='This task tests your ability to remember the ' +\
        'order and spatial position in which a series of colored geometric ' +\
        'shapes are presented. You will see between 2 and 4 shapes. Your job ' +\
        'is to remember the order, spatial position, color, and shape of each ' +\
        'item presented. After the final shape is presented, recreate the ' +\
        'sequence by clicking on the correct colored shape and dragging ' +\
        'it to the appropriate spatial position. The better you do the ' +\
        'more points you will earn. The number of points you earn will ' +\
        'increase the more you get correct without making a mistake. ' +\
        'Click begin to start.'

        instStim = visual.TextStim(window, text=instructions,color = (-1,-1,-1),pos=(0,0),height=triangleDistX*textSizeInc,wrapWidth = instRect.width * 0.93)
        outerRect.setOpacity(0.6)
        
        
#        compType = DetermineSystemType(versionNum)
#        if compType == 'pc':
#            myMouse = event.Mouse(win=window)
#        elif compType == 'mac':
#            myMouse = event.Mouse()


        background.draw()
        [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
        outerRect.draw()
        instRect.draw()
        instStim.draw()
        if timesThrough == 0:
            if numPracticeTrials > 0:
                practiceRect.draw()
                practiceText.draw()
            else:
                beginRect.draw()
                beginText.draw()
        else:
            beginRect.draw()
            beginText.draw()


        window.flip()

        somethingPressed = False
        while not somethingPressed:
            for key in event.getKeys():
                if key in ['escape']:
                    core.quit()
            if myMouse.isPressedIn(beginRect) and timesThrough == 0:
                numTimesThroughSB = 1
                trialNums = [26,26]
                trialTypes = ["ExperimentalTrials","ExperimentalTrials"]
                somethingPressed = True
            elif myMouse.isPressedIn(practiceRect):
                numTimesThroughSB = 2
                trialNums = [numPracticeTrials,26]
                trialTypes = ["Practice","ExperimentalTrials"]
                somethingPressed = True
            elif myMouse.isPressedIn(beginRect) and timesThrough == 1:
                somethingPressed = True
                trialTypes = ["Practice","ExperimentalTrials"]


        trialNum = 0 
        curMemSize=2
        startShapeDur=0.7
        curMemTrial = 0
        timeBetweenShapes = 0.5
        totalHighScore = 0

        scoreNum.setText(curScore)

        timeBetweenShapes = 1.0
        startShapeDur = 0.8

        

        trialType = trialTypes[timesThrough]
        numTrials = trialNums[timesThrough]
        outerRect.setOpacity(1.0)
        shiftNums = [0,4,8,12]
        timeShifts = [0.25]*3 + [0.5]


#        jeopardy.play()
        for k in range(len(timeShifts)):
            for i in range(len(shiftNums)):
                colorsDummy = shift(allPosFlat,shiftNums[i])
                [allShapes[j].setPos(colorsDummy[j]) for j in range(len(allShapes))]
                background.draw()
                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                window.flip()
                countDown1 = core.CountdownTimer(timeShifts[k])
                while countDown1.getTime() > 0:
                    doNothing = 1


        [allShapes[j].setPos(allPosFlat[j]) for j in range(len(allShapes))]
        background.draw()
        [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
        window.flip()


        timesThrough += 1

        #####################################Outer loop ends here
        for shapeBuilderInnerLoop in range(numTrials):
            myMouse.setVisible(False)

            ranNumStim=[i for i in xrange(0,len(testShapes))]
            random.shuffle(ranNumStim)

            ranNumPos=[i for i in xrange(0,len(allSquarePos))]
            random.shuffle(ranNumPos)

            allSameColor=np.array([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
            allSameShape=np.transpose(allSameColor)

            allShapeTestPos=[i for i in range(len(allSquarePos))]
            allShapeTestRandom=[i for i in range(len(allSquarePos))]
            random.shuffle(allShapeTestRandom)

            normList = [i for i in range(len(allSameColor))]
            colorShuffle = [i for i in range(len(allSameColor))]
            shapeShuffle = [i for i in range(len(allSameColor))]
            random.shuffle(colorShuffle)
            random.shuffle(shapeShuffle)

            whatType = random.randint(0,2)

            correctShapesList=[]
            correctShapes=[]
            correctAtt=[]
            cTrialShapes=[]
            positions=[]
            AA=0
            BB=0

            oneStep = [9,10,11,18,19,20,21,22,23]
            allDiff = [3,4,5,12,13,14,24,25]

            if curMemSize == 4 and trialNum in [18,19,20]:
                changeIt = [0,2]
                random.shuffle(changeIt)
                changeIt = changeIt[0]
            else:
                changeIt = random.randint(0,curMemSize-2)

            allObjects = []
            allPositions = []
            for i in range(0,curMemSize):
                curColor = normList[colorShuffle[AA]]
                curShape = normList[shapeShuffle[BB]]
                if whatType == 0:
                    if (trialNum in allDiff):
                        AA += 1
                        BB += 1
                    elif (trialNum in oneStep) and (i==changeIt):
                        AA += 1
                        BB += 1
                    else: 
                        AA += 0
                        BB += 1
                else:
                    if (trialNum in allDiff):
                        AA += 1
                        BB += 1
                    elif (trialNum in oneStep) and (i==changeIt):
                        AA += 1
                        BB += 1
                    else: 
                        AA += 1
                        BB += 0
                curObject = allSameColor[curColor][curShape]
                allObjects.append(curObject)
                newShape=testShapes[curObject]
                newShape.setPos(allSquarePos[allShapeTestPos[allShapeTestRandom[i]]])
                cTrialShapes.append(newShape)
                correctShapes.append([curObject,allShapeTestPos[allShapeTestRandom[i]]])
                allPositions.append(allShapeTestRandom[i])
                correctAtt.append([allSameColor[curColor].tolist(),allSameShape[curShape].tolist()])

            core.wait(1.0)
            for i in xrange(0,len(cTrialShapes)):
                background.draw()
                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                [borderingRects[j].draw() for j in range(len(borderingRects))]
                window.flip()
                core.wait(timeBetweenShapes)
                background.draw()
                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                [borderingRects[j].draw() for j in range(len(borderingRects))]
                cTrialShapes[i].draw()
                window.flip()
                core.wait(startShapeDur)

            background.draw()

            [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
            window.flip()


            grabbedShape = -1
#            myMouse.setVisible(visible=True)

            selectedShapesNum = []
            timer = [core.CountdownTimer(400.0) for i in range(curMemSize)]
            perfect = 0
            limboShapes = []
            limbShapesTime = [0,0,0,0]
            coloredRectsBin = [0,0,0,0]
            allScores=[]
            placedShapes=[]
            coloredRects=[]
            lightSquare = 0
            #Mouse start
            myMouse.setVisible(True)
            while len(selectedShapesNum) < curMemSize: #continue until keypress
                if sum(limbShapesTime) > 0:
                    outerRectShapeColor.fillColor = defRectColor
                    for j in range(len(limboShapes)):
                        if timer[j].getTime() <= 0:
                            limbShapesTime[j] = 0
                    lightSquare = 0
                    background.draw()
                    coloredRects=[]
                    [allShapes[k].setPos(allPosFlat[k]) for k in range(len(allShapes))]
                    [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                    [limboShapes[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                    [allShapes[k].draw() for k in range(len(allShapes))]
                    [scoreValueTexts[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                    window.flip()
                for key in event.getKeys():
                    if key in ['escape']:
                        core.quit()
                for i in range(0,len(allShapes)):
                    if myMouse.isPressedIn(allShapes[i]) == True:
                        grabbedShape = i
                        allShapes[i].setPos(myMouse.getPos())
                        mouse1, mouse2, mouse3 = myMouse.getPressed()
                        clickedOn = True
                        if grabbedShape <= 3 and grabbedShape > -1:
                            curRectCol = 0
                        elif grabbedShape <= 7 and grabbedShape > 3:
                            curRectCol = 1
                        elif grabbedShape <= 11 and grabbedShape > 7:
                            curRectCol = 2
                        elif grabbedShape <= 15 and grabbedShape > 11:
                            curRectCol = 3
                        outerRectShapeColor.fillColor = difColors[curRectCol]
                        while (clickedOn):
                            allShapes[grabbedShape].setPos(myMouse.getPos())
                            for j in range(len(allSquarePos)):
                                if EucDist([allShapes[grabbedShape].pos[0],allShapes[grabbedShape].pos[1]],allSquarePos[allShapeTestPos[allShapeTestRandom[j]]]) <= 0.06:
                                    coloredRects = []
                                    coloredRectsBin[len(selectedShapesNum)] = 1
                                    lightSquare = 1
                                    coloredRects.append(visual.Rect(window,lineWidth=shapeLWidth*3,lineColor=difColors[curRectCol],fillColor=(0.4,0.4,0.4),width=Xdist,height=Ydist,pos=allSquarePos[allShapeTestPos[allShapeTestRandom[j]]],opacity=0.5))
                            background.draw()
                            [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                            if lightSquare == 1:
                                [coloredRects[k].draw() for k in range(len(coloredRects))]
                            [limboShapes[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                            [scoreValueTexts[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                            [allShapes[k].draw() for k in range(len(allShapes))]
                            window.flip()
                            mouse1, mouse2, mouse3 = myMouse.getPressed()
                            if not mouse1:
                                for j in xrange(0,len(allSquarePos)):
                                    if EucDist([allShapes[grabbedShape].pos[0],allShapes[grabbedShape].pos[1]],allSquarePos[allShapeTestPos[allShapeTestRandom[j]]]) <= 0.06:
                                        placedShapes.append(grabbedShape)
                                        squareSel = allShapeTestPos[allShapeTestRandom[j]]
                                        selectedShapesNum.append(squareSel)
                                        if lightSquare == 1:
                                            [coloredRects[k].draw() for k in range(len(coloredRects))]
                                        unShapes[grabbedShape].setPos(allSquarePos[squareSel])
                                        unShapes[grabbedShape].draw()
                                        ShapeSet = True
                                        curShapeVal = 0
                                        if squareSel == correctShapes[len(selectedShapesNum)-1][1]:
                                            if grabbedShape == correctShapes[len(selectedShapesNum)-1][0]:
                                                if len(selectedShapesNum)-1 == 0 or perfect == 0:
                                                    curShapeVal = 15
                                                else:
                                                    curShapeVal = int(scoreValueTexts[len(selectedShapesNum)-2].text) * 2
                                                perfect = 1
                                            elif grabbedShape in correctAtt[len(selectedShapesNum)-1][1]:
                                                curShapeVal = 10
                                                perfect = 0
                                            elif squareSel == correctShapes[len(selectedShapesNum)-1][1]:
                                                curShapeVal = 5
                                                perfect = 0
                                            else :
                                                curShapeVal = 0
                                                perfect = 0
                                        curScore += curShapeVal
#                                        scoreNum.setText(curScore)
                                        allScores.append(curShapeVal)
                                        [allShapes[k].setPos(allPosFlat[k]) for k in range(len(allShapes))]
                                        scoreValueTexts[len(selectedShapesNum)-1].setText(curShapeVal)
                                        scoreValueTexts[len(selectedShapesNum)-1].setPos(allSquarePos[squareSel])
                                        timer[len(selectedShapesNum)-1] = core.CountdownTimer(1.5)
                                        unShapes[grabbedShape].setPos(allSquarePos[squareSel])
                                        limboShapes.append(unShapes[grabbedShape])
                                        limbShapesTime[len(selectedShapesNum)-1] = 1
                                        clickedOn = False
                                background.draw()
                                [allStimNoPres[k].draw() for k in range(len(allStimNoPres))]
                                if lightSquare == 1:
                                    [coloredRects[k].draw() for k in range(len(coloredRects))]
                                [limboShapes[k].draw() for  k in range(len(limboShapes)) if limbShapesTime[k] == 1]
                                [scoreValueTexts[k].draw() for  k in range(len(limboShapes)) if limbShapesTime[k] == 1]
                                [allShapes[k].draw() for k in range(len(allShapes))]
                                clickedOn = False
                            if sum(limbShapesTime) > 0:
                                for j in range(len(limboShapes)):
                                    if timer[j].getTime() <= 0:
                                        limbShapesTime[j] = 0
                                background.draw()
                                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                                if lightSquare == 1:
                                    [coloredRects[k].draw() for k in range(len(coloredRects))]
                                [limboShapes[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                                [scoreValueTexts[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                                [allShapes[k].draw() for k in range(len(allShapes))]
                                window.flip()
                        if clickedOn == False:
                            outerRectShapeColor.fillColor = defRectColor
                            lightSquare = 0
                            if sum(limbShapesTime) > 0:
                                for j in range(len(limboShapes)):
                                    if timer[j].getTime() <= 0:
                                        limbShapesTime[j] = 0
                                lightSquare = 0
                                background.draw()
                                coloredRects=[]
                                [allShapes[k].setPos(allPosFlat[k]) for k in range(len(allShapes))]
                                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                                [limboShapes[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                                [scoreValueTexts[j].draw() for  j in range(len(limboShapes)) if limbShapesTime[j] == 1]
                                [allShapes[k].draw() for k in range(len(allShapes))]
                                window.flip()
                            else:
                                background.draw()
                                [allShapes[k].setPos(allPosFlat[k]) for k in range(len(allShapes))]
                                [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]
                                [allShapes[k].draw() for k in range(len(allShapes))]
                                window.flip()
                event.clearEvents()#get rid of other, unprocessed events

            countDown3 = core.CountdownTimer(0.5)
            while countDown3.getTime() > 0:
                doNothing = 1

            if (curScore - int(scoreNum.text)) <= 0:
                scoreTime = 0.1
            else:
                scoreTime = (0.75/(curScore - int(scoreNum.text)))*0.25
            countDown1 = core.CountdownTimer(1.5)
            countDown2 = core.CountdownTimer(0)
            if curScore - int(scoreNum.text) < 45:
                curInc = 1
            elif curScore - int(scoreNum.text) < 100:
                curInc = 5
            else:
                curInc = 10
            while countDown1.getTime() > 0:
                countDown2.add(scoreTime)
                if (curScore - int(scoreNum.text)) < 11:
                    curInc = 1
                if int(scoreNum.text) < curScore:
                    scoreNum.setText(int(scoreNum.text) + curInc)
                else:
                    scoreNum.setText(curScore)
                DrawStimuliFlip([background] + allShapes + allStimNoPres + allShapes,window)
                while countDown2.getTime() > 0:
                    doNothing = 1
            scoreNum.setText(curScore)

            background.draw()
            [allShapes[i].setPos(allPosFlat[i]) for i in range(len(allShapes))]
            [allStimNoPres[j].draw() for j in range(len(allStimNoPres))]

            window.flip()


            posHighSchores = [15,30,60,120]
            maxScoreTrial = sum(posHighSchores[0:curMemSize])
            totalHighScore += maxScoreTrial
            
            if WriteData:
                thisExp.addData("Trial", trialNum)
                thisExp.addData("CurrentMemorySetSize", curMemSize)

                thisExp.addData("TimeBetweenShapes", timeBetweenShapes)
                thisExp.addData("ShapeDuration", startShapeDur)

                thisExp.addData("TrialType", trialType)

                thisExp.addData("CurrentScore", curScore)
                thisExp.addData("MaxScore_Trial", maxScoreTrial)
                thisExp.addData("MaxScore_Total", totalHighScore)

                for temp in range(len(selectedShapesNum)):
                    thisExp.addData("Shape_" + str(temp+1) + "_DraggedTo", selectedShapesNum[temp])
                    thisExp.addData("Shape_" + str(temp+1) + "_Score", allScores[temp])
                    thisExp.addData("Shape_" + str(temp+1) + "_Placed", placedShapes[temp])
                    thisExp.addData("Shape_" + str(temp+1) + "_CorrectShape", allObjects[temp])
                    thisExp.addData("Shape_" + str(temp+1) + "_CorrectPosition", allPositions[temp])
                    for temp2 in range(len(correctAtt[temp])):
                        thisExp.addData("Shape_" + str(temp+1) + "_CorrectColors", correctAtt[temp][0][temp2])
                        thisExp.addData("Shape_" + str(temp+1) + "_CorrectShapes", correctAtt[temp][1][temp2])

            curMemTrial += 1
            trialNum += 1

            startShapeDur -= 0.1
            timeBetweenShapes -= 0.4

            whenToInc = [6,15]

            if curMemTrial in  whenToChange:
                timeBetweenShapes = 1.0
                startShapeDur = 0.8

            if trialNum in whenToInc:
                curMemSize += 1
                startShapeDur=1.0
                curMemTrial = 0

            ####Inner Loop end

    doneText = visual.TextStim(window, text="You are done with the experiment. \
    Press the SPACEBAR to end the task.",color = (1,-1,-1),pos=(0,0),height=0.03,wrapWidth = instRect.width * 0.95)

    background.draw()
    scoreRect.draw()
    scoreNum.draw()
    scoreLabel.draw()
    doneText.draw()
    window.flip()

    event.waitKeys(keyList='space')

    if WriteData:
        thisExp.addData("FinalScore", curScore)
    
    return curScore
#myWindow = visual.Window(fullscr = True)
shapeBuilderScore = ShapeBuilderFunction(win=win,physicalMonSize=[33,20.7],writeData = True,computerAndVersionType='macOld',numPracTrials=4)
'''
Optional parameters for ShapeBuilderFunction:

writeData -- Either True or False. Do you want write data to the data file. Assumed to be True if nothing is given.

nunPracTrials -- Should be an integer between 0 and 26. It is the number of practice trials participants go through before
               starting the real trials. Set at 6 if nothing is specified. 
               
win -- what is the name of the window that you want to use. If not specified, a new window will be created.

computerAndVersionType -- either 'pc', 'mac', or 'macOld' should be specified. If you have a mac and are using 
                          psychopy version 1.82 or earlier, you should specify 'macOld' -- otherwise 'mac'.

physicalMonSize -- should be a vector with two numbers (e.g., [30,20]). Should correspond to the size of your monitor.
                   width should be listed first. This will alter how the stimuli appear. If this is mis-specified, the 
                   stimuli will look funky. 

'''
# keep track of which components have finished
ShapebuilderFunctionComponents = []
for thisComponent in ShapebuilderFunctionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "ShapebuilderFunction"-------
while continueRoutine:
    # get current time
    t = ShapebuilderFunctionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShapebuilderFunctionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ShapebuilderFunction"-------
for thisComponent in ShapebuilderFunctionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


# the Routine "ShapebuilderFunction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
