

import pygame
from mark import Mark, Score
import game_functions as gf



class TicTacToe:
	"""Tic tac toe game model"""
	def __init__(self):
		"""Initialize attributes and apply settings"""
		pygame.init()
		
		self.apply_settings()
		self.screen = pygame.display.set_mode((self.sn_width, self.sn_height), pygame.SCALED)
		self.flag = True
		# Creating all the UI components of game.
		self.clock = pygame.time.Clock()
		self.marks = {}
		self.score1 = Score(self.screen, self.font, self.black, 1, (self.sn_width/2, self.sn_height-self.y_gap/2))
		self.score2 = Score(self.screen, self.font, self.black, -1, (self.sn_width/2, self.y_gap/2))
		
		# Fill color to screen and draw board.
		self.render()
		
	def apply_settings(self):
		"""All the settings of the game"""
		# Color settings.
		self.white = (255, 255, 255)
		self.black = (0, 0, 0)
		self.red = (255, 0, 0)
		
		# Screen settings.
		self.sn_width = 720
		self.sn_height = 1280
		self.sn_fps = 20
		
		# Board settings.
		self.block_width = int(self.sn_width / 3)
		self.y_gap = int((self.sn_height / 2) - (self.sn_width / 2))
		self.blocks = gf.get_block_numbers(self.sn_width, self.block_width, self.y_gap)
		self.win = 0
		self.isTouch = False
		
		# Score settings.
		self.font = pygame.font.Font("AllerDisplay.ttf", 130)
		
	def check_events(self):
		"""Response to touch events and draw mark."""
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				self.isTouch = True
				gf.respond_touch_event(self.screen, event.pos, self.blocks, self.marks)
				if self.exit.collidepoint(event.pos):
					self.flag = False
	
	def render(self):
		"""Render the components of game."""
		self.screen.fill(self.white)
		gf.draw_board(self.screen, self.sn_width, self.block_width, self.y_gap, self.black)
		self.exit = gf.draw_exit(self.screen, self.sn_width)
		self.score1.draw()
		self.score2.draw(True)
		gf.draw_initial_turn_line(self.screen, self.red, self.score1, self.score2)
	
	def new_round(self):
		"""Redraw all the components of the game"""
		self.marks = {}
		self.score1.mark, self.score2.mark = self.score2.mark, self.score1.mark
		self.render()
		
	def update(self):
		"""Update the score."""
		if self.win:
			pygame.time.wait(1000)
			gf.update_score(self.win, self.score1, self.score2)
			self.new_round()
			self.win = 0
		if len(self.marks.values()) == 9:
			self.new_round()
		
	def run(self):
		"""Start the game loop."""
		while self.flag:
			self.check_events()
			self.update()
			if self.isTouch:
				# Check which mark wins.
				self.win =  gf.check_round_winner(self.screen, self.marks, self.blocks, self.black)
				self.isTouch = False
			
			self.clock.tick(self.sn_fps)
			pygame.display.update()


		
		

# Run the game.
if __name__ == "__main__":
	game = TicTacToe()
	game.run()
	
	
	