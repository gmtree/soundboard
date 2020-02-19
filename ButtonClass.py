#!/usr/bin/python3

import pygame, sys, time
from pygame.locals import *
import getsounds

# button colors
PKI_GREEN = (0, 102, 0)
STR_LIMEGREEN = (0, 204, 0)
STR_CYAN_LIMEGREEN = (0, 204, 102)
BLACK = (0, 0, 0)

DARKER = PKI_GREEN
NORMAL = STR_LIMEGREEN
SHINY = STR_CYAN_LIMEGREEN

# actual list of sounds pulled from ./sounds folder
sound_list = getsounds.grabSoundNames()

# helps me better manage my Buttons in pygame
class Button(object):
    def __init__(self, x, y, w, h, font, text, color=None, button_id=None, the_sound=None):
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
        self.button_id = button_id
        self.the_sound = None

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

    def activateFunction(self):

        if self.button_id[0:1] == "p":
            play(self.the_sound)

            return (None, None, None)

        elif self.button_id[0:1] == "s":
            stop(self.the_sound)

            return (None, None, None)

        elif self.button_id[0:1] == "l":

            self.activated = False

            user_sound_text, self.the_sound = load(self.text, self.the_sound)

            return (user_sound_text, self.the_sound, self.button_id)

def play(sound_obj):
    # play the assigned sound object
    sound_obj.play()
    time.sleep(1) # after playing once, wait for x secs, then stop
    sound_obj.stop()

def stop(sound_obj):
    # stop the assigned sound object
    sound_obj.stop()

def load(button_text, the_sound):

    while True:

        sound_name = input("What is your sound name? -> ")

        if sound_name in sound_list:

            print(pygame.mixer.Sound(f"./sounds/{sound_name}"))

            return sound_name, pygame.mixer.Sound(f"./sounds/{sound_name}")