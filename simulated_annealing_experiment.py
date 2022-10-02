# import libraries
import copy
import random
from threading import local

from hill_climbing_experiment import random_grid
from hill_climbing_experiment import generate_value
from hill_climbing_experiment import find_all_neighbors
from hill_climbing_experiment import find_highest_value_neighbor

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
        # Grab the x, y, value variables of the highest value neighbor
        successor_x, successor_y, successor_value = find_highest_value_neighbor(grid, current_x, current_y, current_value)


        # If the neighbor's value is 0,
        # return the current state
        if successor_value == 0:
            global_max = current_value


        # If the neighbor's value is larger than the current value, update 
        # all current values to the successor values and reduce step count
        # by 1
        elif successor_value > current_value: 
            # Create a list of all the possible neighbors
            neighbors_list=[]
            find_all_neighbors(grid, current_x, current_y, neighbors_list)

            # Random

            # if (DeltaE < 0):
            current_x = successor_x
            current_y = successor_y
            current_value = successor_value
            global_max = successor_value
            steps_remaining -= 1


        # Else, we are out of steps
        else:
            # Print statements for debugging
            print("No More Steps")
            print("Local Max")
            print(current_value)

            # If we have restarts remaining, reduce the number of remaining
            # restarts by 1 and call the hill climbing algorithm again with
            # 1 less restart
            if restarts_remaining > 0:
                # Print statements for debugging
                print("Restarts Left")
                print(restarts_remaining)

                restarts_remaining -= 1
                # Store the maximum found from the restart into a variable
                found_max = simulated_annealing(grid, max_number_of_steps, restarts_remaining)
                
                # If the value found from the restart is higher than the found max of the 
                # pre-reset run, update the value
                if found_max > global_max:
                    global_max = found_max
                else:
                    pass
            else:
                # Print statements for debugging
                print("No More Restarts")
            # Else, we have no more steps and no more restarts
            # Return the highest found value from all runs   
            return global_max



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