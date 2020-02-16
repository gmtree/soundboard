#!/usr/bin/python3

import pygame, sys, time
from pygame.locals import *
from ButtonClass import *

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
YMARGIN = 150

# size of the controller background rectangle
PLAYERWIDTH = 250
PLAYERHEIGHT = 100

# margins for the buttons of inside each controller background
CTRL_XMARGIN = 10
CTRL_YMARGIN = 5

# size of each button INSIDE of each controller background
BUTTONWIDTH = 80
BUTTONHEIGHT = 40

# sample list of 6 sounds
sound_list = ['sound0.wav', 'sound1.wav', 'sound2.wav', 'sound3.wav', 'sound4.wav', 'sound5.wav']

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

	# init the "title button"
	# should not be able to activate later
	b0 = Button(int(WINDOWWIDTH / 2) - 110, int(WINDOWHEIGHT - 450), 220, 40, BASICFONT,"Personal Soundboard")
	button_list.append(b0)

	createSoundPlayerGrid()

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
				print(event.pos)
			# elif event.type == MOUSEMOTION: # if mouse moves at all
				# mousex, mousey = event.pos 

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
			else:
				elm.activated = False

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

	playButton = "p" + str(ctrlNumX) + str(ctrlNumY)

	# top + CTRL_YMARGIN + adjy, previous y coord
	playButton = Button(left + CTRL_XMARGIN + adjx, top + int(PLAYERHEIGHT / 2) - BUTTONHEIGHT - 1 + adjy, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "PLAY")
	button_list.append(playButton)

	stopButton = "st" + str(ctrlNumX) + str(ctrlNumY)

	# top + CTRL_YMARGIN + (BUTTONHEIGHT + 1) + adjy, previous y coord
	stopButton = Button(left + CTRL_XMARGIN + adjx, top + int(PLAYERHEIGHT / 2) + 1 + adjy, BUTTONWIDTH, BUTTONHEIGHT, BASICFONT, "STOP")
	button_list.append(stopButton)

	soundNameButton = "sn" + str(ctrlNumX) + str(ctrlNumY)

	soundNameButton = Button(left + CTRL_XMARGIN + BUTTONWIDTH + 10 + adjx, top + int(PLAYERHEIGHT / 2) - int(BUTTONHEIGHT / 2) + adjy, BUTTONWIDTH + 55, BUTTONHEIGHT, BASICFONT, "soundName")
	button_list.append(soundNameButton)

def createSoundPlayerGrid():

	# create a grid of SoundCtrlRects based on the number of sounds in folder + 1

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