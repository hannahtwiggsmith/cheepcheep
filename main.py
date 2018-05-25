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


"""
Helper function for line wrapping.
"""
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

"""
Pygame doesn't have linewrapping, so I had to write it myself.
"""
def wrapline(text, font, maxwidth): 
    done=0                      
    wrapped=[]                  
                               
    while not done:             
        nl, done, stext=truncline(text, font, maxwidth) 
        wrapped.append(stext.strip())                  
        text=text[nl:]                                 
    return wrapped


"""
This is a hacky, inefficient implementation of twine. To use it, you create passages objects (which are 
functionally Twine passages with a little more info like colors) and connect them together by adding an 
array of Passage objects that the options correspond to. You can also specify whether the passage will
trigger a minigame (or any code in the main directory), and pass in the name of the file. It will be
run when the Passage is navigated to by the player.
"""
class Passage():
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

welcome = Passage('Welcome to cheepcheep! Use the number keys to advance. Good Luck!', ['continue'])

intro = Passage('You wake up. Your head is throbbing.', ['look around'])
intro2 = Passage('You\'re in a desert, somewhere. There are dark blue feathers scattered around.', ['Oh. Right. I crashed.'])
intro3 = Passage('It\'s all coming back to you now- you need to get home. You know your home is across the desert', ['Start walking', 'Stay where you are'])
intro4 = Passage('You start walking -well, er, trudging. It\'s slow going in this sand.', ['continue'])
intro5 = Passage('The desert is... bright. And... pretty empty of terrors.', ['Blink', 'Blink twice', 'Blink three times'])

wait = Passage('What the hell is waiting going to accomplish? You\'re stuck in the desert.', ['Keep Going', 'Wait some more'])
wait2 = Passage('You don\'t have very good survival skills.', ['Move', 'Sit still and get thirsty'])
wait3 = Passage('The only thing that changes is your level of thirst. It is, unsurprisingly, increasing.', ['Move, dumbass.', 'Accept your fate. Your thirsty fate.'])

die = Passage('You died of thirst. Try again with a few more brain cells.', ['Try again'])

bright = Passage('It\'s very bright. You see something glimmering off in the distance. If you squint, you can make out some palm trees.', ['An oasis!', 'A mirage!'])
oasis = Passage('You take off towards the glittering spot off in the distance. It draws closer.', ['next'])
oasis2 = Passage('Ah yes, palm trees, a pool of cool, blue water, and... teeth?', ['whoops'])
oasis3 = Passage('The illusion disappears! You find yourself staring down at the gaping maw of the infamous sarlacc!', ['oh no!'])
oasis4 = Passage('Something colorful catches your eye... you see a brilliantly colored parrot slipping and sliding into the pit below. Do you rescue him?', ['Yes', 'No'])


run = Passage('Suspicious of the oasis, you walk far around it towards a high dune in the distance.', ['continue'])
run2 = Passage('You spot a small tree on top of the dune. It looks like it\'s been dead for a long time.', ['investigate', 'ignore'])
bird = Passage('As you approach the tree you hear a gentle crowing. A fat red rooster is perched on one of the dead breanches, looking out over the desert.', ['Say hello'])
howdy = Passage('"Well howdy there, stranger! We don\'t get many wanderers in these parts. The name\'s Rhode Island, but you can just call me Red"', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy2 = Passage('"I saw you give the sarlacc down there a wide berth. You musta seen right through it\'s mirage. Must be those eagle eyes."', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy3 = Passage('"Say, I just watched another traveler run straight towards that mouth - I told him not to go down there but he was never gonna listen."', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy4 = Passage('"He went straight into the mouth! Ya know, I\'m sure he could use some help right about now."', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy5 = Passage('"He looked like one of those rich birds that fly in from Philly. You know the type - preened and pretty."', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy6 = Passage('"Anyway, I\'m sure you\'d be handsomely rewarded if you found it in your heart to scuttle down there and rescue that poor parrot!"', ['next'], option_color=(255,192,203), background_color=(139,0,0))
howdy7 = Passage('Wanting to finally move on in the story, you accept the mission.', ['next'])
howdy8 = Passage('You bid farewell to Red and trudge down the hill, reaching the edge of the sarlacc pit.', ['next'])

sarlacc = Passage('You ready yourself to face the sarlacc', ['I won!', 'I lost!'], kind='game', gamefile='sarlacc.py')
w = Passage('You did it!', ['next'])
l = Passage('You died!', ['next'])
thanks = Passage('"Why thank you good sir!", chatters the parrot. "That thing would have been flossing its teeth with my feathers for weeks!"', ['next'])
thanks2 = Passage('"Here, take this as a reward!"', ['next'])
thanks3 = Passage('You gained a bag of jerky.', ['next'])
cont = Passage('You leave the parrot behind and set off in the direction of the city.', ['next'])
cont2 = Passage('The sand is hot.', ['next'])
cont3 = Passage('The air is hot.', ['next'])
cont4 = Passage('The wind is hot.', ['next'])
cont5 = Passage('The sky is hot.', ['next'])
cont6 = Passage('Life is hot.', ['next'])
cont7 = Passage('Sand is everywhere...', ['Shake out the sand from your feathers'])
cont8 = Passage('The sand was chafing under your wings. That\'ll be fun to deal with later.', ['Wait... wings?'])
cont9 = Passage('Well, duh. You\'re a bird. You can fly.', ['You\'ve got to be kidding me.'])

fly = Passage('As you take off and leave the sand beneath you, you notice Red, the rooster from earlier, slowly waddling after that parrot.', ['next'])
fly2 = Passage('You let them be.', ['next'])
fly3 = Passage('Another sight catches your eye. Some blurs of color are anxiously zipping around a rather mean-looking cactus.', ['investigate'])

cactus = Passage('As you draw closer, something sharp flies past your head. Woah!', ['next'])
cactus2 = Passage('The color turns out to be a small swarm of hummingbirds, AKA the avian equivalent of rodents.', ['scoff'])
cactus3 = Passage('As you watch, one of the hummingbirds falls to the ground. Hit by one of those flying things!', ['how odd'])
cactus4 = Passage('One of the birds flies up to you and hovers in that infuriating manner. Showoff.', ['next'])
hum = Passage('"Dear sir! We can\'t get to that juicy, juicy flower on this here cactus! He keeps shooting spines at us!"', ['next'], option_color=(199, 234, 70), background_color=(0,139,0))
hum2 = Passage('"We would be forever in your debt if you could retrieve that flower for us! It\'s already taken down three of my friends!"', ['next'], option_color=(199, 234, 70), background_color=(0,139,0))
hum3 = Passage('You look down to see three small bodies. It\'s... pitiful, you guess.', ['grudgingly accept the quest', 'awkwardly walk away'])
quest = Passage('You look at the cactus.', ['next'])
quest2 = Passage('It looks back.', ['next'])
quest3 = Passage('it hurtles some small gray spikes right at you.', ['next'])
quest4 = Passage('Dodge the spikes! Did you win?', ['I won!', 'I lost!'], kind='game', gamefile='sarlacc.py')
cw = Passage('You got the flower! Now the brats can slurp in peace.', ['next'])
cl = Passage('You lost! Oh well.', ['next'])

sand = Passage('You walk away from the cactus feeling no different about yourself.', ['next'])
sand2 = Passage('Finally, you can fly.', ['Take off'])

sky = Passage('The desert is so pretty from up here. This is how it should be viewed... none of that walking business.', ['next'])
sky2 = Passage('And there... off in the distance... the city!', ['Pick up the pace'])
sky3 = Passage('flying...', ['next'])
sky4 = Passage('soaring...', ['next'])
sky5 = Passage('gliding...', ['next'])
sky6 = Passage('This is getting old now. You\'re almost there.', ['next'])
city = Passage('You land in front of the city gates. They\'re locked, of course, as if you didn\'t have enough to deal with today.', ['next'])
city2 = Passage('And that infernal bird netting is over the top...', ['next'])
city3 = Passage('Customs it is.', ['next'])

customs = Passage('The customs officers are a pair of grim turkeys. They ask you to turn out your pockets.', ['hand over the jerky'])
customs2 = Passage('They give it a glance', ['next'])
customs3 = Passage('They give it a sniff', ['next'])
customs4 = Passage('They give it a taste', ['next'])
customs5 = Passage('Grim turkey #2 recoils in terror at what he\'s done.', ['next'])
customs6 = Passage('The bag was, in fact, turkey jerky.', ['next'])
customs7 = Passage('Good job there, partner. You succeeded in introducing cannibalism to some turkeys.', ['next'])
customs8 = Passage('Bet that\'s not where you thought this game was going? ;)', ['next'])
end = Passage('Thanks for playing!', [])
# It probably would have been easier to just do this all in twine. GUIs rule.

# Link all the text screens
# I hate this
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
die.set_next_array([welcome])
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
cont9.set_next_array([fly])
fly.set_next_array([fly2])
fly2.set_next_array([fly3])
fly3.set_next_array([cactus])
cactus.set_next_array([cactus2])
cactus2.set_next_array([cactus3])
cactus3.set_next_array([cactus4])
cactus4.set_next_array([hum])
hum.set_next_array([hum2])
hum2.set_next_array([hum3])
hum3.set_next_array([quest, sand])
quest.set_next_array([quest2])
quest2.set_next_array([quest3])
quest3.set_next_array([quest4])
quest4.set_next_array([cw, cl])
cl.set_next_array([welcome])
cw.set_next_array([sand])
sand.set_next_array([sand2])
sand2.set_next_array([sky])
sky.set_next_array([sky2])
sky2.set_next_array([sky3])
sky3.set_next_array([sky4])
sky4.set_next_array([sky5])
sky5.set_next_array([sky6])
sky6.set_next_array([city])
city.set_next_array([city2])
city2.set_next_array([city3])
city3.set_next_array([customs])
customs.set_next_array([customs2])
customs2.set_next_array([customs3])
customs3.set_next_array([customs4])
customs4.set_next_array([customs5])
customs5.set_next_array([customs6])
customs6.set_next_array([customs7])
customs7.set_next_array([customs8])
customs8.set_next_array([end])

# that was a lot
# softdes students if you're reading this don't write code like this
# do as i say not as i do amirite


current_text = welcome # welcome is the first passage

def main_loop():
	global current_text
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()
			pressed = pygame.key.get_pressed()

			if current_text.kind == 'game':
				# Trigger the minigame code
				os.system("python3 "+current_text.gamefile)
				current_text.kind = 'text'

			if pressed[pygame.K_1] and len(current_text.next_array)>0:
				current_text = current_text.next_array[0]
			if pressed[pygame.K_2] and len(current_text.next_array)>1:
				current_text = current_text.next_array[1]
			if pressed[pygame.K_3] and len(current_text.next_array)>2:
				current_text = current_text.next_array[2]
		current_text.blit_text()
		pygame.display.update()

main_loop()
