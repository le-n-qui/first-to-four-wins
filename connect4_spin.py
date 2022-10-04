# Connect 4 Spin Game

# size of the game board
ROW_SIZE = 8
COL_SIZE = 5

# a mapping from number to letter on left margin of board
num_to_char = {0: 'a', 1: 'b', 2: 'c', 3: 'd',
                4: 'e', 5: 'f', 6: 'g', 7: 'h'}
# a mapping from letter to number
char_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3,
                'e': 4, 'f': 5, 'g': 6, 'h': 7}

# below is a representation of the board squares
board_squares = [ ['E'] * COL_SIZE for _ in range(ROW_SIZE) ]

def board_progress():
    # corners in one horizontal border
    corners = ['+'] * (COL_SIZE+1)
    
    # print top margin
    # 2 spaces +  numbers separated by space
    print('  ' + ' '.join([ str(num) for num in range(1,COL_SIZE+1) ]))

    # print rows of board and borders between rows
    for pos in range(ROW_SIZE):
    	# letter on left margin + bar + square status separate by bar + bar
        board_row = num_to_char[pos] + '|' + '|'.join(board_squares[pos]) + '|'
        print(board_row)
        # print horizontal border
        print(' ' + '-'.join(corners))



if __name__ == "__main__":

    # Ask human: which player, Red or Yellow, do they want to play as?
    # save input into player variable
    player = input("Which player would you like to play (R/Y)? ")
    # status to continue/end while loop
    status = True
    
    # Ask again if human does not give the right input
    while player not in ['R', 'r', 'Y', 'y', 'Q', 'q']:
        player = input("Please input one of these options (R - Red, Y - Yellow, q - quit): ")
        if player.lower() == 'q':
            status = False
    
    # If human picks Red player, they go first
    if player.upper() == 'R':
        print("No moves yet")
    # otherwise, agent goes first
    # TODO
    
    # start the game
    while status:
        # show the board with human move
        board_progress()

        # TODO: program agent to make a move

        # TODO: show the board with agent move
        
        # print instruction for human's next move
        move = input("Please enter your move (format row-column-flip_column): ")

        status = False

