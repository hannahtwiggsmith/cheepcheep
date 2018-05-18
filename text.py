"""
Author: Hannah Twigg-Smith
Main game file for cheepcheep
"""

import pygame
from pygame.locals import *
import sys

global current_text

X_SIZE = 620
Y_SIZE = 480

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
SCREEN = pygame.display.set_mode((X_SIZE, Y_SIZE))
background = pygame.image.load('images/background.bmp').convert()
SCREEN.blit(background, (0, 0))

from itertools import chain

def truncline(text, font, maxwidth):
        real=len(text)       
        stext=text           
        l=font.size(text)[0]
        cut=0
        a=0                  
        done=1
        old = None
        while l > maxwidth:
            a=a+1
            n=text.rsplit(None, a)[0]
            if stext == n:
                cut += 1
                stext= n[:-cut]
            else:
                stext = n
            l=font.size(stext)[0]
            real=len(stext)               
            done=0                        
        return real, done, stext             
        
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped


class TextScreen():
	def __init__(self, display_text, option_array, next_array, font_color=(255,255,255), option_color=(0,0,255), background_color=(0,0,0)):
		"""
		display_text: the information displayed at the top of the screen
		option_array: the options the player can choose to advance through the story
		next_array: an array of text objects that will be rendered when the corresponding options are chosen
		"""
		self.display_text = display_text
		self.option_array = option_array
		self.next_array = next_array
		self.font_color = font_color
		self.background_color = background_color
		self.option_color = option_color

	def blit_text(self):
		SCREEN.fill(self.background_color)
		option_y = 80
		for value, line in enumerate(wrapline(self.display_text, myfont, 570)):
			SCREEN.blit(myfont.render(line, False, self.font_color),(30, 30+value*25))
			option_y +=20

		for value, option in enumerate(self.option_array):
			op = '[{0}] '.format(str(value+1)) + option
			SCREEN.blit(myfont.render(op, False, self.option_color),(30, option_y+value*25))


intro3 = TextScreen('It\'s all coming back to you now-', ['continue'], [])
intro2 = TextScreen('You\'re in a desert, somewhere. There are feathers scattered around.', ['Oh. Right. I crashed.'], [intro3])
intro = TextScreen('You wake up. Your head is throbbing.', ['look around'], [intro2])
welcome = TextScreen('Welcome to cheepcheep! Use the number keys to advance. Good Luck!', ['continue', 'also continue'], [intro, intro])

current_text = welcome

def main_loop():
	global current_text
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			pressed = pygame.key.get_pressed()
			if pressed[pygame.K_1]:
				current_text = current_text.next_array[0]
			if pressed[pygame.K_2]:
				current_text = current_text.next_array[1]
			if pressed[pygame.K_3]:
				current_text = current_text.next_array[2]
		current_text.blit_text()
		pygame.display.update()

main_loop()
