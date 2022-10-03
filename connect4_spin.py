# Connect 4 Spin Game

ROW_SIZE = 8
COL_SIZE = 5

board_dict = {1: 'a', 2: 'b', 3: 'c',
			4: 'd', 5: 'e', 6: 'f', 
			7: 'g', 8: 'h'}

def board_progress():
	# corners in one horizontal border
    corners = ['+'] * (COL_SIZE+1)
	# below is a representation of the board squares
    board_squares = [ ['E'] * COL_SIZE ] * ROW_SIZE 
    # print top margin
    # 2 spaces +  numbers separated by space
    print('  ' + ' '.join([ str(num) for num in range(1,COL_SIZE+1) ]))
    for pos in range(ROW_SIZE):
    	# letter on left margin + bar + square status separate by bar + bar
        board_row = board_dict[pos+1] + '|' + '|'.join(board_squares[pos]) + '|'
        print(board_row)
        # print horizontal border
        print(' ' + '-'.join(corners))

# Ask human: which player, Red or Yellow, do they want to play as?
# save input into player variable
player = input("Which player would you like to play (R/Y)? ")

board_progress()

