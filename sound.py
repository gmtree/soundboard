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

BASICFONTSIZE = 14

TEXTBGCOLOR = WHITE
TEXTCOLOR = BLACK

CTRL_BGCOLOR = WHITE
CTRL_TEXTCOLOR = BLACK

# margins for the spacing of the area for the sound controllers
XMARGIN = 50
YMARGIN = 100

# margins for the buttons inside each sound controller
CTRL_XMARGIN = 5
CTRL_YMARGIN = 5

# size of the controller background rectangle
PLAYERWIDTH = 300
PLAYERHEIGHT = 40

# sample list of 3 sounds
sound_list = ['sound0.wav', 'sound1.wav', 'sound2.wav']

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
	TITLE_SURF, TITLE_RECT = makeText('This is your personal soundboard', TEXTCOLOR, TEXTBGCOLOR, 
		WINDOWWIDTH / 2, WINDOWHEIGHT - 450)

	# main loop
	while True:
		# auto-make the grid of sound controllers
		drawSoundPlayerGrid()

		checkForQuit()
		for event in pygame.event.get(): # event handling loop
			if event.type == MOUSEBUTTONUP:
				print("Hello world!")
				playSound()

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

# this is to test out the playing of a simple sound, using the mouse
# need to remove this later, or refactor it, to be able to apply
# play sounds to every controller
def playSound():
	# small sounds
	soundObj = pygame.mixer.Sound('sound0.wav')
	soundObj.play()
	time.sleep(1) # after playing once, wait for x secs, then stop
	soundObj.stop()

# used this only for making the title text
# can be used for other main text on the board
def makeText(text, color, bgcolor, x_pos, y_pos):
	# create the Surface and Rect objects for some text
	textSurf = BASICFONT.render(text, True, color, bgcolor)
	textRect = textSurf.get_rect()
	textRect.center = (x_pos, y_pos)
	return (textSurf, textRect)

# the sound controller has a large BG rectangle which
# houses the play and stop button + sound name
# this is to calculate the top, left tip --> in order to make a rect
def getTopLeftofSoundRect(ctrlNumX, ctrlNumY):
	# XMARGIN - the margin to the left so that the rects don't appear on the left wall
	# ctrlNumX - the x coordinate of the sound player as if on a grid
	# PLAYERWIDTH - how wide the rect will be
	# the last subtraction, ctrlNumX - 1, helps make a little space between rects
	left = XMARGIN + (ctrlNumX * PLAYERWIDTH) + (ctrlNumX - 1)
	top = YMARGIN + (ctrlNumY * PLAYERHEIGHT) + (ctrlNumY - 1)
	return (left, top)
		

def drawSoundCtrlRect(ctrlNumX, ctrlNumY, adjx = 0, adjy = 0):
	# from ctrlNum X and Y coordinates, draw a rectangle for that sound ctrl
	# with an optional few pixels over (by adjx and ajdy)

	# each BG rect will consist of 3 surfaces created with 3 with invisible rects
	# one box for play, stop, sound name

	# calculate each rect top left corner pixel
	left, top = getTopLeftofSoundRect(ctrlNumX, ctrlNumY)

	# BG rect
	pygame.draw.rect(DISPLAYSURF, CTRL_BGCOLOR, (left + adjx, top + adjy, PLAYERWIDTH, PLAYERHEIGHT))

	# make the play button
	playSurf = BASICFONT.render('PLAY', True, CTRL_TEXTCOLOR)
	playRect = playSurf.get_rect()
	playRect.topleft = (left + CTRL_XMARGIN + adjx, top + CTRL_YMARGIN + adjy)
	DISPLAYSURF.blit(playSurf, playRect)

	# make the stop button
	stopSurf = BASICFONT.render('STOP', True, CTRL_TEXTCOLOR)
	stopRect = stopSurf.get_rect()
	stopRect.topleft = (left + CTRL_XMARGIN + adjx, top + CTRL_YMARGIN + (BASICFONTSIZE + 1) + adjy)
	DISPLAYSURF.blit(stopSurf, stopRect)

	# make the text invis rect for the sound name
	soundNameSurf = BASICFONT.render('SOUND NAME', True, CTRL_TEXTCOLOR)
	soundNameRect = stopSurf.get_rect()
	soundNameRect.midleft = (left + CTRL_XMARGIN + int(PLAYERWIDTH / 5) + adjx, top + int(PLAYERHEIGHT / 2) + adjy)
	DISPLAYSURF.blit(soundNameSurf, soundNameRect)

def drawSoundPlayerGrid():

	# TODO
	# create a grid of SoundCtrlRects based on the number of sounds in folder, add 1

	ctrlNumY = 0

	for ctrlNumX in range(3):

		# use 0,0 box coordinate system
		# boxes are counted as 0 , 2 -> 3 boxes to the right
		# 2 , 3 -> 3 boxes down and 4 boxes right
		drawSoundCtrlRect(ctrlNumX, ctrlNumY)

# main area to run program like with a C function
if __name__ == '__main__':
	main()