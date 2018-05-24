"""
Author: Hannah Twigg-Smith
Cactus game file for cheepcheep
"""

import pygame
from pygame.locals import *
import sys
import random

pygame.init()

X_SIZE = 620
Y_SIZE = 480
GRAY = (119,136,153)
PINK = (255,0,144)
RED = (255, 0, 0)

SCREEN = pygame.display.set_mode((X_SIZE, Y_SIZE))

ENEMY_SIZE = (30, 10)
ENEMY_IMAGE = pygame.transform.scale(pygame.image.load('images/spike.bmp').convert(), ENEMY_SIZE)


background = pygame.image.load('images/background.bmp').convert()


class Spike(pygame.sprite.Sprite):
	def __init__(self, color, width, height, speed):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.speed = speed

	def update(self):
		self.rect.x -= self.speed

class Player(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = Y_SIZE//2

	def update(self, movement):
		self.rect.x += movement[0]
		self.rect.y += movement[1]

class Flower(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.x = 500
		self.rect.y = Y_SIZE//2

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

SCREEN.blit(background, (0, 0))

spike_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
flower_list = pygame.sprite.Group()

pygame.key.set_repeat(5,5)
player = Player(RED, 20, 20)
all_sprites_list.add(player)

flower = Flower(PINK, 30, 30)
all_sprites_list.add(flower)
flower_list.add(flower)

dead_text = myfont.render('YOU DIED! r to restart', False, (0, 0, 0))
win_text = myfont.render('YOU WIN! r to restart', False, (0, 0, 0))
global state
state = "running"

def generate_spikes():
	for x in range(15):
		spike = Spike(GRAY, 20, 5, random.choice(range(1,6)))
		spike.rect.x = X_SIZE
		spike.rect.y = random.randrange(Y_SIZE)
		spike_list.add(spike)
		all_sprites_list.add(spike)


def main_loop():
	global state
	while True:
		if state == "running":
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				pressed = pygame.key.get_pressed()
				if pressed[pygame.K_w]:
				   player.update((0, -5))
				if pressed[pygame.K_s]:
				   player.update((0, 5))
				if pressed[pygame.K_a]:
				   player.update((-5, 0))
				if pressed[pygame.K_d]:
				   player.update((5, 0))

			spike_list.update()
			SCREEN.blit(background, (0, 0))
			all_sprites_list.draw(SCREEN)

			if (pygame.sprite.spritecollide(player, spike_list, True)):
				state = "dead"

			if (pygame.sprite.spritecollide(player, flower_list, True)):
				state = "win"

			pygame.display.update()
			pygame.time.delay(5)

		if state == "dead":
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				pressed = pygame.key.get_pressed()
				if pressed[pygame.K_r]:
					for sprite in spike_list.sprites():
						sprite.kill()

					player.rect.x = 0
					player.rect.y = Y_SIZE//2
					generate_spikes()
					state = "running"

			SCREEN.blit(dead_text,(100, 200))
			pygame.display.update()

		if state == "win":
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()
				pressed = pygame.key.get_pressed()
				if pressed[pygame.K_r]:
					for sprite in spike_list.sprites():
						sprite.kill()

					player.rect.x = 0
					player.rect.y = Y_SIZE//2
					generate_spikes()
					state = "running"

			SCREEN.blit(win_text,(100, 200))
			pygame.display.update()


generate_spikes()
main_loop()