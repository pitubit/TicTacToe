
import pygame
from pygame.sprite import Sprite


class Mark(Sprite):
	"""Tic tac toe mark class"""
	def __init__(self, screen, center, refer):
		"""Initailize the attributes"""
		super().__init__()
		self.screen = screen
		
		self.load_image(refer)
		self.rect = self.image.get_rect()
		self.rect.center = center
		
	def load_image(self, r):
		"""Load image according to refer number.
		if refer is 1 then load cross
		else load circle
		"""
		if r == 1:
			self.image = pygame.image.load("cross.png")
		else:
			self.image = pygame.image.load("circle.png")
		
	def draw(self):
		"""Display the mark image."""
		self.screen.blit(self.image, self.rect)


class Score:
	"""A class to show players score"""
	def __init__(self, screen, font, color, mark, center):
		"""Initialize attributes."""
		self.screen = screen
		self.font = font
		self.color = color
		self.center = center
		self.mark = mark
		
		self.score = 0
		self.text = self.font.render(str(self.score), True, self.color)
		self.rect = self.text.get_rect()
		self.rect.center = self.center
	
	def update(self, flip=False):
		"""Update score, flip, center it."""
		self.text = self.font.render(str(self.score), True, self.color)
		if self.score % 10 == 0:
			self.rect = self.text.get_rect()
			self.rect.center = self.center
		if flip:
			self.text = pygame.transform.flip(self.text, True, True)

	
	def draw(self, flip=False):
		"""Draw the score on screen"""
		self.update(flip)	
		self.screen.blit(self.text, self.rect)

	
	