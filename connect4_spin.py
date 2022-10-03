# Connect 4 Spin Game

ROW_SIZE = 8
COL_SIZE = 5

def board_progress():
	# corners in one horizontal border
	corners = ['+'] * (COL_SIZE+1)
	# this is a representation of the board squares
	board_squares = [ ['E'] * COL_SIZE ] * ROW_SIZE 
	for pos in range(ROW_SIZE):
		print('|'.join(board_squares[pos]))
		print('-'.join(corners))

player = input("Which player would you like to play (R/Y)? ")

board_progress()

