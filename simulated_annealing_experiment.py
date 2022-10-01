# import libraries
import copy
import random
from threading import local

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
            row.append(generate_value())
        # place the filled row into grid
        grid.append(row)
    # return the random grid
    return grid


# flip an unbiased coin: if it is heads treat it as a 1, 
# if it is tails, flip the coin again and if it is heads, treat it as a 2. 
# if it is tails, flip the coin again ... -- If you get five tails in a row, 
# restart the procedure
def generate_value():
    # If one head, return 1
    if random.randint(0, 1) == 1:
        return 1
    # If one tail + one head, return 2
    elif random.randint(0, 1) == 1:
        return 2
    # If one tail + two heads, return 3
    elif random.randint(0, 1) == 1:
        return 3
    # If one tail + three heads, return 4
    elif random.randint(0, 1) == 1:
        return 4
    # If one tail + four heads, return 5
    elif random.randint(0, 1) == 1:
        return 5
    # If all tails, run the algorithm again
    else:
        return generate_value()

def simulated_annealing(grid, max_number_of_steps, max_number_of_restarts=0):
    # create a copy of the grid
    copy_grid = copy.deepcopy(grid)

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

    print('CURRENT PROGRESS: ')
    print('-----------------')
    show_agent_progress(copy_grid, current_x, current_y)

    # Create variables that mark how many steps / restarts are left
    steps_remaining = max_number_of_steps
    restarts_remaining = max_number_of_restarts

    # This loop continues until no more steps are allowed
    while steps_remaining > 0:
        # Create a list of all the possible neighbors
        list = []
        find_all_neighbors(grid, current_x, current_y, list)

        # Calculate the probabilities

        # Sum up the values of the neighbors (S)
        

        # Assign the probabilities (V/S)

        # Move to the next square with the highest probability


def find_highest_value_neighbor(grid, current_x, current_y, current_value):
    
    # Initialize all successor variables to the input"
    # current x,y,value variables
    successor_x = current_x
    successor_y = current_y
    successor_value = current_value

    # Looping through all values +/- 1 of the input x,y values
    for x in [current_x - 1, current_x, current_x + 1]:
        for y in [current_y - 1, current_y, current_y + 1]:

            # If the chosen x,y values are in bounds and the value at those
            # coordinates is larger than the successor value, update the 
            # successor x, y, value values
            if(x >= 0 and x <= 7 and y >= 0 and y <= 7 and grid[x][y] > successor_value):
                successor_x = x
                successor_y = y
                successor_value = grid[x][y]
    
    # Return the highest value neighbor that is found
    return successor_x, successor_y, successor_value


def find_all_neighbors(grid, current_x, current_y, neighbors_list):

    # Looping through all values +/- 1 of the input x,y values
    for x in [current_x - 1, current_x, current_x + 1]:
        for y in [current_y - 1, current_y, current_y + 1]:

            # If the chosen x,y values are in bounds, add them to the
            # list of neighbors
            if x >= 0 and x <= 7 and y >= 0 and y <= 7:
                list = []
                list.append(x)
                list.append(y)
                list.append(grid[x][y])
                neighbors_list.append(list)
    
    # Return the highest value neighbor that is found
    return list


# Show agent on grid
def show_agent_progress(grid, current_x, current_y):
    # Represent agent with letter X
    # at point (current_x, current_y)
    grid[current_x][current_y] = 'X'
    # loop through the outer list
    for row in grid:
    	# print each inner list
        print(row)
    # print a newline
    print()

#
# Simulation code below
#

# Simulated Annealing
print('----------------------------------------------------------------------------------')
print('Simulated Annealing Experiment #1')
print()

for i in range(10):
    print('GRID {} LAYOUT: '.format(i+1))
    print('---------------')
    print()
    example_grid = random_grid()
    for row in example_grid:
        print(row)
    value = simulated_annealing(example_grid, 20)

print('Simulated Annealing - End of Simulations for Experiment #1')

print()
print('----------------------------------------------------------------------------------')
print('Simulated Annealing Experiment #2')
print()

for i in range(10):
    print('GRID {} LAYOUT: '.format(i+1))
    print('---------------')
    print()
    new_grid = random_grid()
    for row in new_grid:
        print(row)
    value = simulated_annealing(new_grid, 10, 1)

print('Simulated Annealing - End of Simulations for Experiement #2')
print()
print()