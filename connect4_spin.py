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

# save player who wins
winner = None

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


def check_user_input(user_input):
    correct_user_format = False
    valid_move = False
    if is_user_input_format_correct(user_input):
        correct_user_format = True
        user_move = user_input.split("-")
        if is_move_valid(user_move[0], user_move[1], user_move[2]):
            valid_move = True
    return correct_user_format, valid_move
        

def is_user_input_format_correct(user_input):
    if len(move) == 5 and move[1] == "-" and move[3] == "-":
        return True
    else:
        return False


def is_move_valid(row_to_change, column_to_change, column_to_spin):
    if are_inputs_valid(row_to_change, column_to_change, column_to_spin):
        row, column, spin = convert_user_move_to_function_variables(row_to_change, column_to_change, column_to_spin)
        if is_target_tile_empty(row, column):
            return True
        else:
            return False
    else:
        return False


def are_inputs_valid(row_to_change, column_to_change, column_to_spin):
    if row_to_change in ["a", "b", "c", "d", "e", "f", "g", "h"] and column_to_change in ["1", "2", "3", "4", "5"] and column_to_spin in ["1", "2", "3", "4", "5", "n"]:
        return True
    else:
        return False


def is_target_tile_empty(row_to_change, column_to_change):
    if board_squares[row_to_change][column_to_change] == "E":
        return True
    else:
        return False


def convert_user_move_to_function_variables(row_to_change, column_to_change, column_to_spin):
    # Use the num to char mapping to change between
    # letters and integers for the row index
    row = char_to_num[row_to_change]

    # Subtract 1 from the column index to match the format
    # shown on the printed grid to the appropriate column index
    column = int(column_to_change) - 1
    
    spin = "n"
    if not column_to_spin == "n":

        # Subtract 1 from the spin index to match the format
        # shown on the printed grid to the appropriate column index
        spin = int(column_to_spin) - 1
    
    return row, column, spin


def process_move(row_to_change, column_to_change, column_to_spin, player_color):
    add_color(row_to_change, column_to_change, player_color)
    spin_column(column_to_spin)


def add_color(row_to_change, column_to_change, player_color):
    # Change the target tile to R or Y depending on if 
    # it's the red or yellow player's move
    if player_color == "R":
        board_squares[row_to_change][column_to_change] = "R"
    elif player_color == "Y":
        board_squares[row_to_change][column_to_change] = "Y"
    else:
        board_squares[row_to_change][column_to_change] = "E"


def spin_column(column_to_spin):
    # This method will only work if a valid value is put in.
    # This willshould ignore "n" and other illegal numbers
    if not column_to_spin == "n":
        # Swap the values to mimic a spin
        swap(0, column_to_spin, 7, column_to_spin)
        swap(1, column_to_spin, 6, column_to_spin)
        swap(2, column_to_spin, 5, column_to_spin)
        swap(3, column_to_spin, 4, column_to_spin)


def swap(x1, y1, x2, y2):
    temp = board_squares[x1][y1]
    board_squares[x1][y1] = board_squares[x2][y2]
    board_squares[x2][y2] = temp


# This function (Utility function)
# assesses how much the current board
# is worth to the players involved
# 10 -- R player wins
# -10 -- Y player wins
# 0 -- a draw game
def evaluate():
    # verify winner in row
    for row in board_squares:
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check from column at position col
            if row[col] == row[col+1] == row[col+2] == row[col+3]:
                if row[col] == 'R':
                    return 10

                if row[col] == 'Y':
                    return -10

    # Verify winner in column
    # loop through the columns of a row
    for pos in len(board_squares[row]):
        # look for 4 in a column, starting at position temp_row
        for temp_row in list(range(5)):
            # check for 4 in a column at temp_row
            if board_squares[temp_row][pos] == board_squares[temp_row+1][pos] == board_squares[temp_row+2][pos] == board_squares[temp_row+3][pos]:
                if board_squares[temp_row][pos] == 'R':
                    return 10

                if board_squares[temp_row][pos] == 'Y':
                    return -10

    # Verify winner in diagonal 
    # from upper left to lower right
    for pos in range(5):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos+1][col+1] == board_squares[pos+2][col+2] == board_squares[pos+3][col+3]: 
                if board_squares[pos][col] == 'R':
                    return 10 

                if board_squares[pos][col] == 'Y':
                    return -10

    # Verify winner in diagonal
    # from lower left to upper right
    for pos in range(3, 8):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos-1][col+1] == board_squares[pos-2][col+2] == board_squares[pos-3][col+3]:
                if board_squares[pos][col] == 'R':
                    return 10 

                if board_squares[pos][col] == 'Y':
                    return -10 

    return 0

def minimax(board):
    # evaluate the board
    score = evaluate(board)

    # if MAX wins
    if score == 10:
        return score
    # if MIN wins
    if score == -10:
        return score

    # check to see if player 
    # can make a move
    if not anyPossibleMove(board):
        # no more move to make, draw game
        return 0 



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

        correct_user_format, valid_move = check_user_input(move)
        while valid_move == False:
            if correct_user_format == False:
                print("Illegal input format")
            else:
                print("Valid input format. Illegal move")
            move = input("Please enter your move (format row-column-flip_column): ")
            correct_user_format, valid_move = check_user_input(move)

        # If we made it this far, the user input move is valid
        # Convert the user input into values our program can use
        user_move = move.split("-")
        user_row_to_move, user_column_to_move, user_column_to_spin = convert_user_move_to_function_variables(user_move[0], user_move[1], user_move[2])

        # Print statements for debugging
        print(user_row_to_move)
        print(user_column_to_move)
        print(user_column_to_spin)
        
        # Algorithm calculating the best move goes here
        # algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin = 0


        # Process the moves of the player and algorithm, depending on which color
        # the player is
        if player.upper() == "R":
            process_move(user_row_to_move, user_column_to_move, user_column_to_spin, "R")
            # process_move(algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin, "Y")
        else:
            process_move(user_row_to_move, user_column_to_move, user_column_to_spin, "Y")
            # process_move(algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin, "R")

        
        # status = False

