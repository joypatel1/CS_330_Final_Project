#paddle object for Multiplayer Pong
#Blake Niebrugge, CS 330, Fall 2021

# Code for basic single-player Pong game has been adapted and optimized from 101Computing,net
# https://www.101computing.net/pong-tutorial-using-pygame-getting-started/

#import pygame for sprite usage
import pygame
Black = (0,0,0)

#create paddle objects that will be overlayed 
class Paddle(pygame.sprite.Sprite):

	#define the package function and also call the pygame sprite constructor using super()
	def __init__(self, color, width, height):
		super().__init__()
		
		#now prep the padde object (setting coordinates, width and height)
		self.y = None
		self.x = None
		self.image = pygame.Surface([width,height])
		self.image.fill(Black)
		self.image.set_colorkey(Black)
		
		#draw paddles
		pygame.draw.rect(self.image, color, [0,0,width,height])
		
		#get rectangle object
		self.rect = self.image.get_rect()
		
	#move up function
	def mUp(self, pixels):
		self.rect.y -= pixels
		#dont go off screen
		if self.rect.y < 0:
			self.rect.y = 0
			
	#move down function, alike above function
	def mDown(self, pixels):
		self.rect.y += pixels
		if self.rect.y > 400:
			self.rect.y = 400