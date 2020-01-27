#!/usr/bin/python3

import pygame, sys, time
from pygame.locals import *

# program constants
WINDOWWIDTH = 1000
WINDOWHEIGHT = 500
FPS = 30

# colors to be used
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKTURQUOISE = (3, 54, 73)

BGCOLOR = DARKTURQUOISE
TEXTCOLOR = WHITE
BASICFONTSIZE = 20

BUTTONCOLOR = WHITE
BUTTONTEXTCOLOR = BLACK

GAPSIZE = 40
XMARGIN = 50

### sound area code

# background music
# pygame.mixer.music.load('???.mp3')
# -1 makes the music loop forever, > 0 - only loop certain number of times
# 0.0 means start playing the song from the beginning, > 0.0 - is n number of seconds
# pygame.mixer.music.play(-1, 210.0)
# some more code goes here
# pygame.mixer.music.stop()

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, TITLE_SURF, TITLE_RECT

	# initialize the main window and fps
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	pygame.display.set_caption("Personal Soundboard")
	BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
	DISPLAYSURF.fill(BGCOLOR)

	# top title text of soundboard
	TITLE_SURF, TITLE_RECT = makeText('This is your personal soundboard', BUTTONTEXTCOLOR, BUTTONCOLOR, WINDOWWIDTH / 2, WINDOWHEIGHT - 450)

	# main loop where I'll place to the drawSoundPlayerGrid() call
	while True:
		checkForQuit()
		for event in pygame.event.get(): # event handling loop
			if event.type == MOUSEBUTTONUP:
				print("Hello world!")
				playSound()

		DISPLAYSURF.blit(TITLE_SURF, TITLE_RECT)
		pygame.display.update()
		FPSCLOCK.tick(FPS)

# factor out the simple quit() methods
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

# this is to test out the playing of a simple sound, using the mouse
def playSound():
	# small sounds
	soundObj = pygame.mixer.Sound('sound0.wav')
	soundObj.play()
	time.sleep(1) # after playing once, wait for x secs, then stop
	soundObj.stop()

# used this only for making the title text
# need to make another for creating the play sound buttons, stop, and sound name rectangles
def makeText(text, color, bgcolor, x_pos, y_pos):
	# create the Surface and Rect objects for some text
	textSurf = BASICFONT.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.center = (x_pos, y_pos)
	return (textSurf, textRect)

# def drawSoundCtrlRect()
	
	# TODO
	# create one SoundCtrlRect
	# each Rect consists of 3 smaller boxes + surfaces
	# one box for play sound, stop, sound name

# def drawSoundPlayerGrid()

	# TODO
	# call for the drawSoundCtrlRect() definition
	# create a grid of SoundCtrlRects based on the number of sounds in folder, add 1

# main area to run program like with a C function
if __name__ == '__main__':
	main()