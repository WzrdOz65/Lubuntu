# Balloon game main code

from pygame.locals import *
import pygwidgets
import sys
import pygame
from BalloonMgr import *

#2 - Define Constants
BLACK = (0,0,0)
GRAY = (200,200,200)
BACKGROUND_COLOR = (0,180,180)
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 800
PANEL_HEIGHT = 60
USABLE_WINDOW_HEIGHT = WINDOW_HEIGHT - PANEL_HEIGHT
FRAMES_PER_SECOND = 30

#3 - Initizalize the world 
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

#4 - load assets
oScoreDisplay = pygwidgets.DisplayText(window, (10, USABLE_WINDOW_HEIGHT + 25), 
                                       'Score: 0', textColor=BLACK,
                                       backgroundColor=None, width=140, fontSize=24)

oStatusDisplay = pygwidgets.DisplayText(window, (180, USABLE_WINDOW_HEIGHT + 25), 
                                       '', textColor=BLACK,
                                       backgroundColor=None, width=300, fontSize=24)

oStartButton = pygwidgets.TextButton(window,
                                         (WINDOW_WIDTH - 110, USABLE_WINDOW_HEIGHT + 10), 'Start')

#5 - Initialize variables
oBalloonMgr = BalloonMgr(window, WINDOW_WIDTH, USABLE_WINDOW_HEIGHT)
playing = False     #Wait till user clicks

#6 - Loop Forever 
while True:
    #7 - Check for and handle events
    nPointsEarned = 0 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
        
        if playing:
            oBalloonMgr.handleEvent(event)
            theScore = oBalloonMgr.getScore()
            oScoreDisplay.setValue('Score: ' + str(theScore))
        elif oStartButton.handleEvent(event):
            oBalloonMgr.start()
            oScoreDisplay.setValue('Score: 0')
            playing = True
            oStartButton.disable()
            

#8 Do any per frame actions
    if playing:
        oBalloonMgr.update()
        nPopped = oBalloonMgr.getCountPopped()
        nMissed = oBalloonMgr.getCountMissed()
        round = oBalloonMgr.getRound()
        oStatusDisplay.setValue('    Round: ' + str(round)+ '     Missed : '+ str(nMissed)+ '     Out of: '+ str( N_BALLOONS)) 
        
        
        if(nPopped + nMissed) == N_BALLOONS:
            playing = False
            oBalloonMgr.AddRound()
            oStartButton.enable()
            oBalloonMgr.start()  



#9 Clear the window
    window.fill(BACKGROUND_COLOR)       

#10 - Draw all window elements
    if playing:
        oBalloonMgr.draw()
    holdMyRect = pygame.Rect(0, WINDOW_WIDTH, WINDOW_WIDTH, PANEL_HEIGHT)
    pygame.draw.rect(window, GRAY, holdMyRect)
    
    oScoreDisplay.draw()
    oStatusDisplay.draw()
    oStartButton.draw()

#11 - Update the Window
    pygame.display.update()

#12 - Slow thing down
    clock.tick(FRAMES_PER_SECOND) 
        