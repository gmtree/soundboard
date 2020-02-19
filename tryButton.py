#!/usr/bin/python3

import pygame, sys, time
from pygame.locals import *
from ButtonClass import *
import getsounds

# program constants
WINDOWWIDTH = 1000
WINDOWHEIGHT = 500
FPS = 30

# colors to be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKTURQUOISE = (3, 54, 73)
BURNTORANGE = (80, 33, 0)

# color for the whole window
BGCOLOR = BURNTORANGE

# color for the controller background rectangle
CTRL_BGCOLOR = DARKTURQUOISE

# font fize for all text boxes
BASICFONTSIZE = 12

# margins for the spacing of the whole general grid of sound players
XMARGIN = 123
YMARGIN = 100

# size of the controller background rectangle
PLAYERWIDTH = 250
PLAYERHEIGHT = 100

# margins for the buttons of inside each controller background
CTRL_XMARGIN = 10
CTRL_YMARGIN = 5

# size of each button INSIDE of each controller background
BUTTONWIDTH = 80
BUTTONHEIGHT = 20

# actual list of sounds pulled from ./sounds folder
sound_list = getsounds.grabSoundNames()

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, button_list

    # init fps, main window, text, buttons
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    DISPLAYSURF.fill(BGCOLOR)
    pygame.display.set_caption("Try the New Button Class")
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    # empty list for holding button objects
    button_list = []

    TITLE_SURF, TITLE_RECT = makeText('Personal Soundboard', BLACK, WHITE, WINDOWWIDTH / 2, WINDOWHEIGHT - 450)

    createSoundPlayerGrid()

    # loadALLButton_id = "loALL"

    # loadALLButton = Button(WINDOWWIDTH - 400, WINDOWHEIGHT - 460, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "Load Sounds", None, loadALLButton_id)
    # button_list.append(loadALLButton)

    for ele in button_list:
        print(ele.button_id)

    # main loop
    while True:

        # draw buttons to screen
        drawButtonsAndBGs()

        # check if user tried to exit
        checkForQuit()

        # event handling loop
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                update_click(event.pos) # when L-mousebutton is clicked, update button
                # print(event.pos)
            # elif event.type == MOUSEMOTION: # if mouse moves at all
                # mousex, mousey = event.pos 

        DISPLAYSURF.blit(TITLE_SURF, TITLE_RECT)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

# factor out the exit methods
def terminate():
    pygame.quit()
    sys.exit()

# this checks if the user pressed quit or another way to quit
def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

# mouse click handler
def update_click(pos):
    """
    mouse got clicked
    returns whether a change occurred
    """
    global disable_select

    selected_found = None
    selected_set = None

    for elm in button_list:
        if elm.on_button(pos):
            if elm.activated == False:
                elm.activated = True
                user_sound_text, a_sound, b_id = elm.activateFunction()

                if user_sound_text == None:
                    pass
                else:
                    for e in button_list:
                        if e.button_id[1:3] == elm.button_id[1:3]:
                            if e.button_id[0:1] == 'p':
                                e.the_sound = a_sound
                            elif e.button_id[0:1] == 's':
                                e.the_sound = a_sound
                            elif e.button_id[0:1] == 'l':
                                e.the_sound = a_sound
                            elif e.button_id[0:1] == 'n':
                                e.text = user_sound_text
                                e.the_sound == a_sound
                            else:
                                pass

            else:
                elm.activated = False

def makeText(text, color, bgcolor, x_pos, y_pos):
    # create the Surface and Rect objects just for regular text
    textSurf = BASICFONT.render(text, True, color, bgcolor)
    textRect = textSurf.get_rect()
    textRect.center = (x_pos, y_pos)
    return (textSurf, textRect)

# this is to calculate the top, left corner --> in order to make a rect
def getTopLeftofSoundRect(ctrlNumX, ctrlNumY):
    # XMARGIN - the margin to the left so that the rects don't appear on the left wall
    # ctrlNumX - the x coordinate of the sound player as if on a grid
    # BUTTONWIDTH - how wide the button will be
    # BUTTONHEIGHT - how tall each button will be
    # the last subtraction, ctrlNumX - 1, helps make a little space between rects
    left = XMARGIN + (ctrlNumX * PLAYERWIDTH) + (ctrlNumX - 1)
    top = YMARGIN + (ctrlNumY * PLAYERHEIGHT) + (ctrlNumY - 1)
    return (left, top)


def createButtons(ctrlNumX, ctrlNumY, adjx=0, adjy=0):
    # from ctrlNum X and Y coordinates, draw a rectangle for that sound ctrl
    # with an optional few pixels over (by adjx and adjy)

    left, top = getTopLeftofSoundRect(ctrlNumX, ctrlNumY)

    playButton_id = "p" + str(ctrlNumX) + str(ctrlNumY)

    playButton = Button(left + CTRL_XMARGIN + adjx, top + int(PLAYERHEIGHT / 2) - int(BUTTONHEIGHT / 2) - BUTTONHEIGHT - 1 + adjy, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "PLAY", None, playButton_id)
    button_list.append(playButton)

    stopButton_id = "s" + str(ctrlNumX) + str(ctrlNumY)

    stopButton = Button(left + CTRL_XMARGIN + adjx, top + int(PLAYERHEIGHT / 2) - int(BUTTONHEIGHT / 2) + adjy, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "STOP", None, stopButton_id)
    button_list.append(stopButton)

    loadButton_id = "l" + str(ctrlNumX) + str(ctrlNumY)

    loadButton = Button(left + CTRL_XMARGIN + adjx, top + int(PLAYERHEIGHT / 2) - int(BUTTONHEIGHT / 2) + BUTTONHEIGHT + 1 + adjy, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "LOAD", None, loadButton_id)
    button_list.append(loadButton)

    soundNameButton_id = "n" + str(ctrlNumX) + str(ctrlNumY)

    soundNameButton = Button(left + CTRL_XMARGIN + BUTTONWIDTH + 10 + adjx, top + int(PLAYERHEIGHT / 2) - int(BUTTONHEIGHT / 2) + adjy, BUTTONWIDTH + 55, BUTTONHEIGHT, BASICFONT, "soundName", None, soundNameButton_id)
    button_list.append(soundNameButton)

def createSoundPlayerGrid():

    # create a grid of SoundCtrlRects based on the number of sounds in folder

    for ctrlNumY in range(3):
        # use 0,0 box coordinate system
        # boxes are counted as 0 , 2 -> 3 boxes to the right
        # 2 , 3 -> 3 boxes down [0,1,2] and 4 boxes right [0,1,2,3]
        for ctrlNumX in range(3):
            createButtons(ctrlNumX, ctrlNumY)

def drawButtonsAndBGs(adjx=0, adjy=0):

    # create a grid of SoundCtrlRects based on the number of sounds in folder + 1

    for ctrlNumY in range(3):
        # use 0,0 box coordinate system
        # boxes are counted as 0 , 2 -> 3 boxes to the right
        # 2 , 3 -> 3 boxes down [0,1,2] and 4 boxes right [0,1,2,3]
        for ctrlNumX in range(3):
            # this is the left top corner of each button
            left, top = getTopLeftofSoundRect(ctrlNumX, ctrlNumY)

            # BG rect which represents one player per one sound
            pygame.draw.rect(DISPLAYSURF, CTRL_BGCOLOR, (left + adjx, top + adjy, PLAYERWIDTH, PLAYERHEIGHT))

    for b in button_list:
        b.draw(DISPLAYSURF)

if __name__ == '__main__':
    main()