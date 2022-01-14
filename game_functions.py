

import pygame
from mark import Mark


def draw_board(screen, board_w, block_w, y_gap, color):
	"""Draw the grid board."""
	# Draw column lines.
	for i in range(1, 3):
		pygame.draw.line(screen, color,  (block_w*i, y_gap), (block_w*i, y_gap + board_w), 4)
	# Draw row lines.
	for i in range(1, 3):
		pygame.draw.line(screen, color, (0, y_gap + block_w*i), (board_w, y_gap + block_w*i), 4)

def draw_exit(screen, sn_w):
	"""Draw the exit button."""	
	image = pygame.image.load("close.png")
	rect = image.get_rect()
	rect.topleft = sn_w-rect.width-10, 10
	screen.blit(image, rect)
	return rect
	
def draw_initial_turn_line(screen, red, score1, score2):
	"""Draw the line which show the intial ture of player."""
	if score1.mark == 1:
		pygame.draw.line(screen, red, score1.rect.bottomleft, score1.rect.bottomright, 10)
	else:
		pygame.draw.line(screen, red, score2.rect.topleft, score2.rect.topright, 10)

def get_block_numbers(sn_w, block_w, y_gap):
	"""Calculate center of board's each block"""
	centers = {}
	num = 1
	beg = int(block_w/2)
	for i in range(y_gap+beg, y_gap+sn_w, block_w):
		for j in range(beg, sn_w, block_w):
			centers[(j, i)] = num
			num += 1
	return centers

	
def get_right_block(touch, blocks, marks):
	"""Calculate distance between two coords
	Return center where distance is low
	else return -1
	"""
	for cen, block in blocks.items():
		if block not in marks.keys():
			dist = (cen[0] - touch[0]) ** 2 + (cen[1] - touch[1]) ** 2
			if dist < 10000:
				return cen
	return -1
		
def respond_touch_event(screen, touch, blocks, marks):
	"""Make new mark if touch drop in a grid."""
	block = get_right_block(touch, blocks, marks)
	if block == -1:
		return
	else:
		"""Add new mark wrt ref."""
		ref = 1
		if len(marks) % 2 != 0:
			ref = -1
		new_mark = Mark(screen, block, ref)
		new_mark.draw()
		marks[int(blocks[block])] = ref


def draw_line(screen, blocks, row, color):
	"""Draw line on row."""
	cens = []
	for r in row:
		for cen, block in blocks.items():
			if r == block:
				cens.append(cen)
	pygame.draw.lines(screen, color, False, cens, 5)

def get(marks, i):
	"""Return the refer number of particular
	mark"""
	try:
		return marks[i]
	except KeyError:
		return 0

def check_round_winner(screen, marks, blocks, color):
	"""Check the winner of game by checking
	sum of mark's refer."""
	rows = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
	for row in rows:
		sum = get(marks, row[0]) + get(marks, row[1]) + get(marks, row[2])
		# If sum is 3 then X mark is 3 in row 
		# If sum is -3 the O mark is 3 in row.
		if sum == 3 or sum == -3:
			draw_line(screen, blocks, row, color)
			return sum/3
	return 0
		
def update_score(win, score1, score2):
	"""Check score color and update the winner 	score"""
	if score1.mark == win:
		score1.score += 1
	else:
		score2.score += 1
	
	
	