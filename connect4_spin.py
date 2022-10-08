# Connect 4 Spin Game

# libraries
import sys
import random

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
board_squares = [['E'] * COL_SIZE for _ in range(ROW_SIZE)]

# save player who wins
winner = None

# This function displays
# the board. It will
# reflect the changes made
# by players making moves
def print_board_progress():
    # corners in one horizontal border
    corners = ['+'] * (COL_SIZE+1)

    # print top margin
    # 2 spaces +  numbers separated by space
    print('  ' + ' '.join([str(num) for num in range(1, COL_SIZE+1)]))

    # print rows of board and borders between rows
    for pos in range(ROW_SIZE):
        # letter on left margin + bar + square status separate by bar + bar
        board_row = num_to_char[pos] + '|' + '|'.join(board_squares[pos]) + '|'
        print(board_row)
        # print horizontal border
        print(' ' + '-'.join(corners))

# This function starts
# the input verification
# process
def check_user_input(user_input):
    correct_user_format = False
    valid_move = False
    if is_user_input_format_correct(user_input):
        correct_user_format = True
        user_move = user_input.split("-")
        if is_move_valid(user_move[0], user_move[1], user_move[2]):
            valid_move = True
    return correct_user_format, valid_move

# This function verifies
# whether user input
# follows the desired format
def is_user_input_format_correct(user_input):
    if len(move) == 5 and move[1] == "-" and move[3] == "-":
        return True
    else:
        return False

# This function checks
# to see if the user/machine
# can make a move
# given what they provide
# and the current open
# squares on the board
def is_move_valid(row_to_change, column_to_change, column_to_spin):
    if are_inputs_valid(row_to_change, column_to_change, column_to_spin):
        row, column, spin = convert_user_move_to_function_variables(
            row_to_change, column_to_change, column_to_spin)
        if is_target_tile_empty(row, column):
            return True
        else:
            return False
    else:
        return False

# This function verifies
# whether each component
# of the user input
# are in the set of 
# valid characters
def are_inputs_valid(row_to_change, column_to_change, column_to_spin):
    if row_to_change in ["a", "b", "c", "d", "e", "f", "g", "h"] and column_to_change in ["1", "2", "3", "4", "5"] and column_to_spin in ["1", "2", "3", "4", "5", "n"]:
        return True
    else:
        return False

# This function verifies
# whether a board square
# is empty or not
def is_target_tile_empty(row_to_change, column_to_change):
    if board_squares[row_to_change][column_to_change] == "E":
        return True
    else:
        return False

# This function accepts
# the correctly-formatted 
# user input and translate
# it into the corresponding
# position in the board
# and confirms whether user
# wants to flip any column
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

# This function, after checks are done,
# will finally go through with
# changing the board given
# the move provided by the player
def process_move(row_to_change, column_to_change, column_to_spin, player_color):
    add_color(row_to_change, column_to_change, player_color)
    spin_column(board_squares, column_to_spin)

# This function changes
# the status of the square
# from empty to the disk
# used by the player, R or Y
def add_color(row_to_change, column_to_change, player_color):
    # Change the target tile to R or Y depending on 
    # if it's the red or yellow player's move
    if player_color == "R":
        board_squares[row_to_change][column_to_change] = "R"

    if player_color == "Y":
        board_squares[row_to_change][column_to_change] = "Y"
    

# This function determines
# if a column should be flipped
# and, when verified, flips
# the desired column
def spin_column(board, column_to_spin):
    # This method will only work if a valid value is put in.
    # This should ignore "n" and other illegal numbers
    if not column_to_spin == "n":
        # Swap the values to mimic a spin
        swap(board, 0, column_to_spin, 7, column_to_spin)
        swap(board, 1, column_to_spin, 6, column_to_spin)
        swap(board, 2, column_to_spin, 5, column_to_spin)
        swap(board, 3, column_to_spin, 4, column_to_spin)
    return board

# This function is 
# a helper function
# which supports the
# the spin_column in
# its job of flipping
# a column
def swap(board, x1, y1, x2, y2):
    temp = board[x1][y1]
    board[x1][y1] = board[x2][y2]
    board[x2][y2] = temp


# FOR CALCULATING A BOARD'S SCORE
#
# This function (Utility function)
# assesses how much the current board
# is worth to the players involved
# 10 -- R player wins
# -10 -- Y player wins
# 0 -- a draw game
def evaluate():

    score = 0
    four_in_a_row_found = False

    # verify winner in row
    for row in board_squares:
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check from column at position col
            if row[col] == row[col+1] == row[col+2] == row[col+3]:
                if row[col] == 'R':
                    score += 10
                    four_in_a_row_found = True

                if row[col] == 'Y':
                    score -= 10
                    four_in_a_row_found = True

    # Verify winner in column
    # loop through the columns of a row
    for pos in range(5):
        # look for 4 in a column, starting at position temp_row
        for temp_row in range(5):
            # check for 4 in a column at temp_row
            if board_squares[temp_row][pos] == board_squares[temp_row+1][pos] == board_squares[temp_row+2][pos] == board_squares[temp_row+3][pos]:
                if board_squares[temp_row][pos] == 'R':
                    score += 10
                    four_in_a_row_found = True

                if board_squares[temp_row][pos] == 'Y':
                    score -= 10
                    four_in_a_row_found = True

    # Verify winner in diagonal
    # from upper left to lower right
    for pos in range(5):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos+1][col+1] == board_squares[pos+2][col+2] == board_squares[pos+3][col+3]:
                if board_squares[pos][col] == 'R':
                    score += 10
                    four_in_a_row_found = True

                if board_squares[pos][col] == 'Y':
                    score -= 10
                    four_in_a_row_found = True

    # Verify winner in diagonal
    # from lower left to upper right
    for pos in range(3, 8):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos-1][col+1] == board_squares[pos-2][col+2] == board_squares[pos-3][col+3]:
                if board_squares[pos][col] == 'R':
                    score += 10
                    four_in_a_row_found = True

                if board_squares[pos][col] == 'Y':
                    score -= 10
                    four_in_a_row_found = True

    # if four_in_a_row_found == False:
    #     score = calculate_score()
    return score, four_in_a_row_found


# FOR CALCULATING A BOARD'S SCORE
#
#
# STATUS: In Progress -- TODO
def calculate_score():
    number_of_colors_in_a_row = 0

    # Checking every row
    for row in board_squares:
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # Only continue if

            # Grab the four elements in a line and store them in a list
            elements = []
            elements.append(row[col])
            elements.append(row[col+1])
            elements.append(row[col+2])
            elements.append(row[col+3])

            # Count the number of squares that are red / yellow
            number_of_red_squares, number_of_yellow_squares = 0
            number_of_red_squares = elements.count("R")
            number_of_yellow_squares = elements.count("Y")

            # R R R Y
            # Y R R R
            # Y R R R Y
            # R R Y R

    # Checking every row
    # loop through the columns of a row
    for pos in len(board_squares[row]):
        # look for 4 in a column, starting at position temp_row
        for temp_row in list(range(5)):
            # check for 4 in a column at temp_row
            if board_squares[temp_row][pos] == board_squares[temp_row+1][pos] == board_squares[temp_row+2][pos] == board_squares[temp_row+3][pos]:
                if board_squares[temp_row][pos] == 'R':
                    score += 10

                if board_squares[temp_row][pos] == 'Y':
                    score -= 10

    # Verify winner in diagonal
    # from upper left to lower right
    for pos in range(5):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos+1][col+1] == board_squares[pos+2][col+2] == board_squares[pos+3][col+3]:
                if board_squares[pos][col] == 'R':
                    score += 10

                if board_squares[pos][col] == 'Y':
                    score -= 10

    # Verify winner in diagonal
    # from lower left to upper right
    for pos in range(3, 8):
        # 4 in a row can only be found at column 0 and 1
        for col in [0, 1]:
            # check for 4 in a diagonal at position col
            if board_squares[pos][col] == board_squares[pos-1][col+1] == board_squares[pos-2][col+2] == board_squares[pos-3][col+3]:
                if board_squares[pos][col] == 'R':
                    score += 10

                if board_squares[pos][col] == 'Y':
                    score -= 10


# This function implements
# the minimax algorithm
# as well as the alpha-beta
# pruning technique
def minimax(board, depth, player, alpha, beta):
    # calculate the score of the current board
    score, four_in_a_row_found = evaluate()

    # if MAX wins
    if score >= 10 and four_in_a_row_found:
        return score, -1, -1, "z"
    # if MIN wins
    if score <= -10 and four_in_a_row_found:
        return score, -1, -1, "z"
    # if both players obtain an equal number of 4 in a rows
    # OR if no more moves can be made, game is a draw
    if (score == 0 and four_in_a_row_found) or not any_possible_moves():
        return score, -1, -1, "z"


    if player == "R":
        # create children for R --> Y's next move
        bestValue = -sys.maxsize - 1
        # Look at each square (look at all possibilities) at
        # row number
        return_row, return_col = 0
        return_flip_col = None

        for row in range(len(board)):
            # column number
            for col in range(len(board[0])):
                # choose a column to flip
                for flip_col in [0,1,2,3,4,"n"]:
                    return_row, return_col, return_flip_col = row, col, flip_col
                    # if square at row and col is empty
                    if board[row][col] == 'E':
                        # Let MAX make that move at row and col
                        board[row][col] = 'R'
                        # spin column at flip_col
                        board = spin_column(board, flip_col)
                        # choose the best value by picking the maximum of
                        # current best value and what is returned by minimax
                        calculated_value, calculated_row, calculated_column, calculated_spin_column = minimax(board, depth+1, "Y", alpha, beta)
                        bestValue = max(bestValue, calculated_value)
                        alpha = max(alpha, bestValue)
                        if beta <= alpha:
                            break
                        # reverse the spin
                        board = spin_column(board, flip_col)
                        # mark this current square 'E' again
                        board[row][col] = 'E'
        return bestValue, return_row, return_col, return_flip_col
    else:
        bestValue = sys.maxsize
    # Look at each square (look at all possibilities) at
    # row number
        return_row, return_col = 0
        return_flip_col = None

        for row in range(len(board)):
            # column number
            for col in range(len(board[0])):
                # choose a column to flip
                for flip_col in [0,1,2,3,4,"n"]:
                    return_row, return_col, return_flip_col = row, col, flip_col
                    # if square at row and col is empty
                    if board[row][col] == 'E':
                        # let MIN make that move at row and col
                        board[row][col] = 'Y'
                        # let MIN spin a column at flip col
                        board = spin_column(board, flip_col)
                        # choose the best value by picking the minimum of
                        # current best value and what is returned by minimax
                        calculated_value, calculated_row, calculated_column, calculated_spin_column = minimax(board, depth+1, "R", alpha, beta)
                        bestValue = min(bestValue, calculated_value)
                        beta = min( beta, bestValue)
                        if beta <= alpha:
                            break
                        # reverse the spin
                        board = spin_column(board, flip_col)
                        # mark this current square empty
                        board[row][col] = 'E'
        return bestValue, return_row, return_col, return_flip_col



# Returns true if the player can make a move or not
# This is determined by checking if the board has an
# empty square remaining and returning True if yes and
# False if no
def any_possible_moves():
    for row in board_squares:
        if "E" in row:
            return True
    return False


if __name__ == "__main__":

    # Ask human: which player, Red or Yellow, do they want to play as?
    # save input into player variable
    player = input("Which player would you like to play (R/Y)? ")
    # save type of player for machine
    algorithm_player = None
    # status to continue/end while loop
    status = True


    # Ask again if human does not give the right input
    while player not in ['R', 'r', 'Y', 'y', 'Q', 'q']:
        player = input("Please input one of these options (R - Red, Y - Yellow, q - quit): ")
    
        if player.lower() == 'q':
            status = False

    # If human picks Red player, they go first
    if player.upper() == 'R':
        algorithm_player = 'Y'
        print("No moves yet")
    # otherwise, AI goes first and makes a random move
    else:
        algorithm_player = 'R'
        random_row = random.randint(0,7)
        random_column = random.randint(0,4)
        process_move(random_row, random_column, "n", algorithm_player)
        printed_row = num_to_char[random_row]
        printed_column = random_column + 1
        print("Red moves", "{}-{}-n".format(printed_row, printed_column))

    # start the game
    while status:
        # show the board with human move
        print_board_progress()

        # TODO: program agent to make a move

        # TODO: show the board with agent move

        # print instruction for human's next move
        move = input(
            "Please enter your move (format row-column-flip_column): ")

        correct_user_format, valid_move = check_user_input(move)

        while valid_move == False:
            if correct_user_format == False:
                print("Illegal input format")
            else:
                print("Valid input format. Illegal move")
                
            move = input("Please enter your move (format row-column-flip_column): ")
                
            
            correct_user_format, valid_move = check_user_input(move)

        # If we made it this far, the user input move is valid

        # Print statements for debugging
        # player_color = ""
        # if player.upper() == "R":
        #     player_color = "Red"
        # else:
        #     player_color = "Yellow"
        # print(player_color, "moves", move)

        # Algorithm calculating the best move goes here
        # algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin = 0

        # Process the moves of the player and algorithm, 
        # depending on which color the player is

        move_list = move.split("-")

        user_row_to_move, user_column_to_move, user_column_to_spin = convert_user_move_to_function_variables(
        move_list[0], move_list[1], move_list[2])

        if player.upper() == "R":
            process_move(user_row_to_move, user_column_to_move,
                                 user_column_to_spin, "R")
                # process_move(algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin, "Y")
        else:
            process_move(user_row_to_move, user_column_to_move,
                                 user_column_to_spin, "Y")
                # process_move(algorithm_row_to_move, algorithm_column_to_move, algorithm_column_to_spin, "R")

        # evaluate the board
        score, four_in_a_row_found = evaluate()

        # if Red wins
        if score >= 10 and four_in_a_row_found:
            print_board_progress()
            print("Red wins")
            status = False
        
        # if Yellow wins
        elif score <= -10 and four_in_a_row_found:
            print_board_progress()
            print("Yellow wins")
            status = False
                
        # if both players obtain an equal number of 4 in a rows
        # OR if no more moves can be made, game is a draw
        elif (score == 0 and four_in_a_row_found) or not any_possible_moves():
            print_board_progress()
            print("Draw")
            status = False

        if not status:
            depth = 1
            if player.upper() == "Y":
                depth += 1
                    
            score, calculated_row, caluclated_column, calculated_spin = minimax(board_squares, depth, algorithm_player, -sys.maxsize - 1, sys.maxsize)
            process_move(calculated_row, caluclated_column, calculated_spin, algorithm_player)
