#!/usr/bin/python3

import pygame, sys
from pygame.locals import *

# button colors
PKI_GREEN = (0, 102, 0)
STR_LIMEGREEN = (0, 204, 0)
STR_CYAN_LIMEGREEN = (0, 204, 102)
BLACK = (0, 0, 0)

DARKER = PKI_GREEN
NORMAL = STR_LIMEGREEN
SHINY = STR_CYAN_LIMEGREEN

# helps me better manage my Buttons in pygame
class Button(object):
	def __init__(self, x, y, w, h, font, text, color=None):
		if color is None:
			color = NORMAL

		self.normal_color = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.font = font
		self.text = text
		self.activated = False

	def draw(self, screen):
		if self.activated:
			bg = SHINY
		else:
			bg = self.normal_color

		surf = self.font.render(self.text, True, BLACK, bg)
		rect = (self.x, self.y, self.w, self.h)
		xo = self.x + (self.w - surf.get_width()) // 2
		yo = self.y + (self.h - surf.get_height()) // 2
		screen.fill(bg, rect)
		screen.blit(surf, (xo, yo))

	def on_button(self, pos):
		return self.x <= pos[0] and self.x + self.w > pos[0] and \
				self.y <= pos[1] and self.y + self.h > pos[1]