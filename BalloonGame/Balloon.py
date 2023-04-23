# Balloon base class and 3 subclasses

import pygame
import random
from pygame.locals import *
import pygwidgets
from BalloonConstants import *
from abc import ABC, abstractmethod
from BalloonMgr import *

class Balloon(ABC):
    popSoundLoaded = False
    popSound = None #Load when First Balloon is created
    
    @abstractmethod
    def __init__(self, window, maxWidth, maxHeight, ID,
                 oImage, size, nPoints, speedY):
        self.window = window
        self.ID = ID
        self.balloonImage = oImage
        self.size = size
        self.nPoints = nPoints
        self.speedY = speedY
        if not Balloon.popSoundLoaded: #load First time only
            Balloon.popSoundLoaded = True
            Balloon.popSound = pygame.mixer.Sound('sounds/balloonPop.wav')
        
        balloonRect = self.balloonImage.getRect()
        self.width = balloonRect.width
        self.height = balloonRect.height
        #Postion so balloon is within the width of the window
        #But below the bottom

        self.x = random.randrange(maxWidth - self.width)
        self.y = maxHeight + random.randrange(75)
        self.balloonImage.setLoc((self.x, self.y))
    
    def clickedInside(self, mousePoint):
        myRect = pygame.Rect(self.x, self.y, self.width, self.height)
        if myRect.collidepoint(mousePoint):
            Balloon.popSound.play()
            return True, self.nPoints #True here mean it was hit
        else:
            return False, 0 #Not hit no points

    def update(self):
        self.y = self.y - self.speedY #Upodate y position by speed
        self.balloonImage.setLoc((self.x, self.y))
        if self.y < -self.height: #off the top of the window
            return BALLOON_MISSED
        else:
            return BALLOON_MOVING

    def draw(self):
        self.balloonImage.draw()
    
    def __del__(self):
        self.balloonImage.draw()

class BalloonSmall(Balloon):
    balloonImage = pygame.image.load('images/redBalloonSmall.png')
    def __init__(self,window,maxWidth,maxHeight, ID):
        oImage = pygwidgets.Image(window,(0,0), BalloonSmall.balloonImage)
        super().__init__(window,maxWidth, maxHeight, ID,
                             oImage, 'Small',30, SPEED_S)
    
class BalloonMedium(Balloon):
    balloonImage = pygame.image.load('images/redBalloonMedium.png')
    def __init__(self,window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), BalloonMedium.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Medium', 20, SPEED_M)
        
class BalloonLarge(Balloon):
    balloonImage = pygame.image.load('images/redBalloonLarge.png')
    def __init__(self,window, maxWidth, maxHeight, ID):
        oImage = pygwidgets.Image(window, (0,0), BalloonLarge.balloonImage)
        super().__init__(window, maxWidth, maxHeight, ID,
                         oImage, 'Large', 20, SPEED_L)

    