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

# font fize for all text boxes
BASICFONTSIZE = 20

def main():
	global FPSCLOCK, DISPLAYSURF, BASICFONT, button_list

	# initialize fps, main window, text, buttons
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
	DISPLAYSURF.fill(BGCOLOR)
	pygame.display.set_caption("Try the New Button Class")
	BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

	button_list = []
	createButtons()

	# main loop
	while True:

		# draw buttons to screen
		drawButtons()

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

def createButtons():

	# init the buttons that will be used in program
	b1 = Button(int(WINDOWWIDTH / 2), int(WINDOWHEIGHT - 450), 200, 100, BASICFONT,"hello world")
	button_list.append(b1)

	b2 = Button(int(WINDOWWIDTH / 2), int(WINDOWHEIGHT - 200), 200, 100, BASICFONT,"hello earth")
	button_list.append(b2)

def drawButtons():

	for b in button_list:
		b.draw(DISPLAYSURF)

if __name__ == '__main__':
	main()