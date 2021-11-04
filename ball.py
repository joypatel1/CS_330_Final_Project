#ball class for multiplayer pong
#Blake Niebrugge, CS 330, Fall 2021

# Code for basic single-player Pong game has been adapted and optimized from 101Computing,net
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/
import pygame
#need random integers for velocity changes
from random import randint
Black = (0,0,0)

#create ball object for the game, wil be a sprite object
class Ball(pygame.sprite.Sprite):

	#define the package function and also call the pygame sprite constructor using super()
	def __init__(self, color, width, height):
		super().__init__()
		
		
		self.image = pygame.Surface([width, height])
		self.image.fill(Black)
		self.image.set_colorkey(Black)
		
		#draw the ball
		pygame.draw.rect(self.image, color, [0, 0, width, height])
		
		#set velocity
		self.velocity = [randint(4,8), randint(-8,8)]
		
		#get rectangle object from image package
		self.rect = self.image.get_rect()
		
	
	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]
	
	#reverse velocity path of ball hits paddle
	def bounce(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-8,8)