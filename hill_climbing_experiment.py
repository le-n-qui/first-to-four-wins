# import libraries
import random

# set a seed value
# so random values
# do not change each
# time the script runs
random.seed(42)

# Grid size
# Row size
ROW_SIZE = 8
# Column size
COL_SIZE = 8


def random_grid():
    # create a ROW x COL grid
    # i.e. a list of 
    # of ROW lists which
    # will contain COL elements
    grid = []

    # Populate grid with
    # random values from
    # 1 - 5
    for row_pos in range(ROW_SIZE):
        # create a list for row_i
        row = [] 
        # column by column
        for col_pos in range(COL_SIZE):
            # Fill in at each column position 
            # with a random value
            
            # row.append(random.randint(1, 5))
            row.append(generate_value())
        # place the filled row into grid
        grid.append(row)

    return grid


# flip an unbiased coin, if its heads treat it as a 1, 
# it is tails, flip the coin again and if its heads treat it as a 2, 
# if its tails flip the coin again ... -- If you get five tails in a row, 
# restart the procedure
def generate_value():
    # If one head, return 1
    if(random.randint(0, 1) == 1):
        return 1
    # If one tail + one head, return 2
    elif(random.randint(0, 1) == 1):
        return 2
    # If one tail + two heads, return 3
    elif(random.randint(0, 1) == 1):
        return 3
    # If one tail + three heads, return 4
    elif(random.randint(0, 1) == 1):
        return 4
    # If one tail + four heads, return 5
    elif(random.randint(0, 1) == 1):
        return 5
    # If all tails, run the algorithm again
    else:
        return generate_value()


def hill_climbing(grid, max_number_of_steps, max_number_of_restarts):
    # Select a random x and y as the starting point
    current_x = random.randint(0, 7)
    current_y = random.randint(0, 7)

    # Store the value of the randomly chosen x,y into both
    # the current value and the global max
    current_value = grid[current_x][current_y]
    global_max = current_value

    # Print statements for debugging
    print("Chosen X")
    print(current_x)
    print("Chosen Y")
    print(current_y)
    print("Current Value")
    print(current_value)

    # Create variables that mark how many steps / restarts are left
    steps_remaining = max_number_of_steps
    restarts_remaining = max_number_of_restarts
    

    # This loop continues until no more steps are allowed
    while(steps_remaining > 0):
        # Grab the x, y, value variables of the highest value neighbor
        successor_x, successor_y, successor_value = find_highest_value_neighbor(grid, current_x, current_y, current_value)
        
        # If the neighbor's value is larger than the current value, update 
        # all current values to the successor values and reduce step count
        # by 1
        if(successor_value > current_value): 
            # Print statements for debugging
            print("Step Made")
            print("Old Value")
            print(current_value)
            print("New Value")
            print(successor_value)
            
            current_x = successor_x
            current_y = successor_y
            current_value = successor_value
            global_max = successor_value
            steps_remaining -= 1

            # Print statements for debugging
            print("Steps Remaining")
            print(steps_remaining)

        # Else, we are out of steps
        else:
            # Print statements for debugging
            print("No More Steps")
            print("Local Max")
            print(current_value)

            # If we have restarts remaining, reduce the number of remaining
            # restarts by 1 and call the hill climbing algorithm again with
            # 1 less restart
            if(restarts_remaining > 0):
                # Print statements for debugging
                print("Restarts Left")
                print(restarts_remaining)

                restarts_remaining -= 1
                # Store the maximum found from the restart into a variable
                found_max = hill_climbing(grid, max_number_of_steps, restarts_remaining)
                
                # If the value found from the restart is higher than the found max of the 
                # pre-reset run, update the value
                if(found_max > global_max):
                    global_max = found_max
                else:
                    pass
            else:
                # Print statements for debugging
                print("No More Restarts")
            # Else, we have no more steps and no more restarts
            # Return the highest found value from all runs   
            return global_max


def find_highest_value_neighbor(grid, current_x, current_y, current_value):
    
    # Initialize all successor variables to the input
    # current x,y,value variables
    successor_x = current_x
    successor_y = current_y
    successor_value = current_value

    # Looping through all values +/- 1 of the input x,y values
    for x in ([current_x - 1, current_x, current_x + 1]):
        for y in ([current_y - 1, current_y, current_y + 1]):

            # If the chosen x,y values are in bounds and the value at those
            # coordinates is larger than the successor value, update the 
            # successor x, y, value values
            if(x >= 0 and x <= 7 and y >= 0 and y <= 7 and grid[x][y] > successor_value):
                successor_x = x
                successor_y = y
                successor_value = grid[x][y]
    
    # Return the highest value neighbor that is found
    return successor_x, successor_y, successor_value




# Running code
print('GRID STATUS: ')
print('-----------')
print()
example_grid = random_grid()
for row in example_grid:
	print(row)

# Number of steps / restarts are changed by changing the input values
value = hill_climbing(example_grid, 10, 2)
print("Final Value")
print(value)