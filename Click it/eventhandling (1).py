'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Joshua Carrillo
Mr. Davis
Event Handling
2/3/2017
Adv. Comp. Prog.
Version 2
'''

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 15 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 400)) ##Imorta all the pics
pygame.display.set_caption('Event Handling')
d=pygame.image.load('Pacman.png')
wow=pygame.image.load('other.png')
l=pygame.image.load('BG.png')
ux=0
uy=0
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255) ## SHOWS ALL THE COLOR
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

#sprite

dx=200
dy=200 ## defines the d s and th w s
wx=100
wy=100

#buttons
exitBtn=pygame.image.load('Exit.png') ## Imports the SAVE LOAD QUIT BUTTONS AND THE CHANGE COLOR
saveBtn=pygame.image.load('Save.png')
loadBtn=pygame.image.load('load.png')
clickBtn=pygame.image.load('CLICK.png')

#audio
soundObj=pygame.mixer.Sound('haha.wav') ##brings in sound

#other variables
quitted=False
saved=False
loaded=False

# run the game loop
while True:
    DISPLAYSURF.blit(l, (ux, uy))
    pygame.draw.line(DISPLAYSURF, BLACK, (0, 95), (500, 95), 1)
    DISPLAYSURF.blit(exitBtn,(10,10))
    DISPLAYSURF.blit(loadBtn, (150, 10))
    DISPLAYSURF.blit(saveBtn,(250,10))
    mouseClicked=False
    buttonClicked=False

    for event in pygame.event.get(): ##This for the Mouse CLick
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == MOUSEBUTTONDOWN:
            mousex, mousey = event.pos
            mouseClicked = True
        elif event.type==KEYDOWN:
            buttonClicked=True

    #event handling for button clicked
    if quitted: ##Adds to file when saved
        pygame.quit()
        sys.exit()
    elif saved:
        DISPLAYSURF.blit(clickBtn, (290, 10))
        f=open('location.txt','w')
        f.write(str(dx)+" "+(str(dy)))
        f.close()
        pygame.time.wait(100)
        saved=False
    elif loaded:
        DISPLAYSURF.blit(clickBtn, (150, 10))
        f=open('location.txt','r')
        points=f.readline().split()
        f.close()
        dx=int(points[0])
        dy=int(points[1])
        pygame.time.wait(100)
        loaded=False


    oldDx=dx
    oldDy=dy ## It is some awesomeness
    oldWx = wx
    oldWy = wy

    if mouseClicked: ##Makes sure it stays withing border
        dx,dy=mousex-32,mousey-60
        if mousey-60<=90:
            dy=90
        elif mousey-60>=300:
            dy=320
        if mousex-32>=250:
            dx=250
        elif mousex-32<=50:
            dx=0
        #check if button clicked
        if mousex>=10 and mousex<=110 and mousey>=10 and mousey<=60: ## Checks if clicked on one of the buttons
            DISPLAYSURF.blit(clickBtn,(10,10))
            quitted=True
            dx,dy=oldDx,oldDy
        elif mousex>=290 and mousex<=390 and mousey>=10 and mousey<=60:
            DISPLAYSURF.blit(clickBtn,(290,10))
            saved=True
            dx,dy=oldDx,oldDy
        elif  mousex>=150 and mousex<=250 and mousey>=10 and mousey<=60:
            DISPLAYSURF.blit(clickBtn, (150, 10))
            loaded=True
            dx,dy=oldDx,oldDy
        if quitted!=True and saved!=True and loaded!=True:
            soundObj.play()
    elif buttonClicked:
        if event.key in (K_a,): #mAKES SURE ALL THEE KEYS ARE GUCCI
            dx,dy=oldDx-10,oldDy
            if dx<=0:
                dx=0
        elif event.key in (K_d,): #right
            dx, dy = oldDx +10, oldDy
            if dx>250:
                dx=250
        elif event.key in (K_w,): #up
            dx,dy=oldDx,oldDy-10
            if dy<=85:
                dy=90
        elif event.key in (K_s,): #down
            dx,dy=oldDx,oldDy+10
            if dy>=325:
                dy=325
        if event.key in (K_LEFT,): #left
            wx,wy=oldWx-10,oldWy
            if wx<=0:
                wx=0
        elif event.key in (K_RIGHT,): #right
            wx, wy = oldWx +10, oldWy
            if wx>325:
                wx=325
        elif event.key in (K_UP,): #up
            wx,wy=oldWx,oldWy-10
            if wy<=85:
                wy=90
        elif event.key in (K_DOWN,): #down
            wx,wy=oldWx,oldWy+10
            if wy>=325:
                wy=325

        soundObj.play()

    DISPLAYSURF.blit(d, (dx, dy))
    DISPLAYSURF.blit(wow, (wx, wy))

    pygame.display.update()