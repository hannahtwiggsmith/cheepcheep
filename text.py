"""
Author: Hannah Twigg-Smith
Main game file for cheepcheep
"""

import pygame
from pygame.locals import *
import sys
import os

global current_text

X_SIZE = 620
Y_SIZE = 480

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 24)
SCREEN = pygame.display.set_mode((X_SIZE, Y_SIZE))
background = pygame.image.load('images/background.bmp').convert()
SCREEN.blit(background, (0, 0))

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
	def __init__(self, display_text, option_array, font_color=(255,255,255), option_color=(0,0,255), background_color=(0,0,0), kind='text', gamefile=''):
		"""
		display_text: the information displayed at the top of the screen
		option_array: the options the player can choose to advance through the story
		next_array: an array of text objects that will be rendered when the corresponding options are chosen
		"""
		self.display_text = display_text
		self.option_array = option_array
		self.font_color = font_color
		self.background_color = background_color
		self.option_color = option_color
		self.kind = kind
		self.gamefile = gamefile

	def set_next_array(self, arr):
		self.next_array = arr

	def blit_text(self):
		SCREEN.fill(self.background_color)
		option_y = 80
		for value, line in enumerate(wrapline(self.display_text, myfont, 570)):
			SCREEN.blit(myfont.render(line, False, self.font_color),(30, 30+value*25))
			option_y +=20

		for value, option in enumerate(self.option_array):
			op = '[{0}] '.format(str(value+1)) + option
			SCREEN.blit(myfont.render(op, False, self.option_color),(30, option_y+value*25))



# Text Screen Definitions
#

welcome = TextScreen('Welcome to cheepcheep! Use the number keys to advance. Good Luck!', ['continue'])

intro = TextScreen('You wake up. Your head is throbbing.', ['look around'])
intro2 = TextScreen('You\'re in a desert, somewhere. There are dark blue feathers scattered around.', ['Oh. Right. I crashed.'])
intro3 = TextScreen('It\'s all coming back to you now- you need to get home. You know your home is across the desert', ['Start walking', 'Stay where you are'])
intro4 = TextScreen('You start walking -well, er, trudging. It\'s slow going in this sand.', ['continue'])
intro5 = TextScreen('The desert is... bright. And... pretty empty of terrors.', ['Blink', 'Blink twice', 'Blink three times'])

wait = TextScreen('What the hell is waiting going to accomplish? You\'re stuck in the desert.', ['Keep Going', 'Wait some more'])
wait2 = TextScreen('You don\'t have very good survival skills.', ['Move', 'Sit still and get thirsty'])
wait3 = TextScreen('The only thing that changes is your level of thirst. It is increasing.', ['Move, dumbass.', 'Accept your fate. Your thirsty fate.'])

die = TextScreen('You died of thirst. Try again with a few more brain cells.', ['Try again'])

bright = TextScreen('It\'s very bright. You see something glimmering off in the distance. If you squint, you can make out some palm trees.', ['An oasis!', 'A mirage!'])
oasis = TextScreen('You take off towards the glittering spot off in the distance. It draws closer.', ['next'])
oasis2 = TextScreen('Ah yes, palm trees, a pool of cool, blue water, and... teeth?', ['whoops'])
oasis3 = TextScreen('The illusion disappears! You find yourself staring down at the gaping maw of the infamous sarlacc!', ['oh no!'])
oasis4 = TextScreen('Something colorful catches your eye... you see a brilliantly colored parrot slipping and sliding into the pit below. Do you rescue him?', ['Yes', 'No'])


#avoid oasis
run = TextScreen('Suspicious of the oasis, you walk far around it towards a high dune in the distance.', ['continue'])
run2 = TextScreen('You spot a small tree on top of the dune. It looks like it\'s been dead for a long time.', ['investigate', 'ignore'])
bird = TextScreen('As you approach the tree you hear a gentle crowing. A fat red rooster is perched on one of the dead breanches, looking out over the desert.', ['Say hello'])
howdy = TextScreen('"Well howdy there, stranger! We don\'t get many wanderers in these parts. The name\'s Rhode Island, but you can just call me Red"', ['next'])
howdy2 = TextScreen('"I saw you give the sarlacc down there a wide berth. You musta seen right through it\'s mirage. Must be those eagle eyes."', ['next'])
howdy3 = TextScreen('"Say, I just watched another traveler run straight towards that mouth - I told him not to go down there but he was never gonna listen."', ['next'])
howdy4 = TextScreen('"He went straight into the mouth! Ya know, I\'m sure he could use some help right about now."', ['next'])
howdy5 = TextScreen('"He looked like one of those rich birds that fly in from Philly. You know the type - preened and pretty."', ['next'])
howdy6 = TextScreen('"Anyway, I\'m sure you\'d be handsomely rewarded if you found it in your heart to scuttle down there and rescue that poor parrot!"', ['next'])
howdy7 = TextScreen('Wanting to finally move on in the story, you accept the mission.', ['next'])
howdy8 = TextScreen('You bid farewell to Red and trudge down the hill, reaching the edge of the sarlacc pit.', ['next'])

sarlacc = TextScreen('You ready yourself to face the sarlacc', ['I won!', 'I lost!'], kind='game', gamefile='sarlacc.py')
w = TextScreen('You did it!', ['next'])
l = TextScreen('You died!', ['next'])
thanks = TextScreen('"Why thank you good sir!", chatters the parrot. "That thing would have been flossing its teeth with my feathers for weeks!"', ['next'])
thanks2 = TextScreen('"Here, take this as a reward!"', ['next'])
thanks3 = TextScreen('You gained a bag of jerky.', ['next'])
cont = TextScreen('You leave the parrot behind and set off in the direction of the city.', ['next'])
cont2 = TextScreen('The sand is hot.', ['next'])
cont3 = TextScreen('The air is hot.', ['next'])
cont4 = TextScreen('The wind is hot.', ['next'])
cont5 = TextScreen('The sky is hot.', ['next'])
cont6 = TextScreen('It is hot.', ['next'])
cont7 = TextScreen('Sand is everywhere...', ['Shake out the sand from your feathers'])
cont8 = TextScreen('The sand was chafing under your wings. That\'ll be fun to deal with later.', ['Wait... wings?'])
cont9 = TextScreen('Well, duh. You\'re a bird. You can fly.', ['You\'ve got to be kidding me.'])




# Link all the text screens
welcome.set_next_array([intro])
intro.set_next_array([intro2])
intro2.set_next_array([intro3])
intro3.set_next_array([intro4, wait])
intro4.set_next_array([intro5])
intro5.set_next_array([bright, bright, bright])
bright.set_next_array([oasis, run])
oasis.set_next_array([oasis2])
oasis2.set_next_array([oasis3])
oasis3.set_next_array([oasis4])
oasis4.set_next_array([sarlacc])
wait.set_next_array([intro4, wait2])
wait2.set_next_array([intro4, wait3])
wait3.set_next_array([intro4, die])
die.set_next_array([intro])
run.set_next_array([run2])
run2.set_next_array([bird, bright])
bird.set_next_array([howdy])
howdy.set_next_array([howdy2])
howdy2.set_next_array([howdy3])
howdy3.set_next_array([howdy4])
howdy4.set_next_array([howdy5])
howdy5.set_next_array([howdy6])
howdy6.set_next_array([howdy7])
howdy7.set_next_array([howdy8])
howdy8.set_next_array([sarlacc])
sarlacc.set_next_array([w,l])
l.set_next_array([intro])
w.set_next_array([thanks])
thanks.set_next_array([thanks2])
thanks2.set_next_array([thanks3])
thanks3.set_next_array([cont])
cont.set_next_array([cont2])
cont2.set_next_array([cont3])
cont3.set_next_array([cont4])
cont4.set_next_array([cont5])
cont5.set_next_array([cont6])
cont6.set_next_array([cont7])
cont7.set_next_array([cont8])
cont8.set_next_array([cont9])
cont9.set_next_array([])


#
#
#
#

current_text = welcome

def main_loop():
	global current_text
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			pressed = pygame.key.get_pressed()

			if current_text.kind == 'game':
				os.system("python3 "+current_text.gamefile)
				current_text.kind = 'text'

			if pressed[pygame.K_1]:
				current_text = current_text.next_array[0]
			if pressed[pygame.K_2]:
				current_text = current_text.next_array[1]
			if pressed[pygame.K_3]:
				current_text = current_text.next_array[2]
		current_text.blit_text()
		pygame.display.update()

main_loop()
