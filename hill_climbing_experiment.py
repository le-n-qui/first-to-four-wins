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


def hill_climbing(grid, max_number_of_steps, max_number_of_restarts=0):
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
        
        # If the neighbor's value is larger than the current value, update 
        # all current values to the successor values and reduce step count
        # by 1
        if successor_value > current_value: 
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

            show_agent_progress(copy_grid, current_x, current_y)

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
            if restarts_remaining > 0:
                # Print statements for debugging
                print("Restarts Left")
                print(restarts_remaining)

                restarts_remaining -= 1
                # Store the maximum found from the restart into a variable
                found_max = hill_climbing(grid, max_number_of_steps, restarts_remaining)
                
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


def find_highest_value_neighbor(grid, current_x, current_y, current_value):
    
    # Initialize all successor variables to the input
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


def local_beam_search(grid, max_number_of_steps):
    # Select two pairs of random x and y values as the starting points
    # for the two beams
    current_x1 = random.randint(0, 7)
    current_y1 = random.randint(0, 7)
    current_x2 = random.randint(0, 7)
    current_y2 = random.randint(0, 7)

    # Store the value of the randomly chosen x,y into both
    # the current value and the global max
    current_value1 = grid[current_x1][current_y1]
    current_value2 = grid[current_x2][current_y2]

    # Print statements for debugging
    # print("Chosen X1")
    # print(current_x1)
    # print("Chosen Y1")
    # print(current_y1)
    # print("Current Value 1")
    # print(current_value1)
    # print("Chosen X2")
    # print(current_x2)
    # print("Chosen Y2")
    # print(current_y2)
    # print("Current Value 2")
    # print(current_value2)
    # print()

    # Create variable that marks how many steps are left
    steps_remaining = max_number_of_steps

    # This loop continues until no more steps are allowed
    while(steps_remaining > 0):
        # Create a list of all the possible neighbors
        list = []
        find_all_neighbors(grid, current_x1, current_y1, list)
        find_all_neighbors(grid, current_x2, current_y2, list)

        # If any of the neighbors have a score of 5, return 5 for the 
        # entire algorithm
        highest_value = 0
        for entry in list:
            # print(entry)
            if entry[2] > highest_value:
                highest_value = entry[2]
        if highest_value == 5:
            return highest_value

        # Else, there is no 5. Find the two best children and repeat
        
        # Print statements for debugging
        print("Looking For First Highest Child")

        # Create a variable that stores the highest variable
        highest_value1 = highest_value

        # While the highest possible score value is larger than 0
        while highest_value1 > 0:
            # Check the score values for all the children
            # If a child is found with a score matching the highest possible
            # score, update the x,y,value variables for the first local beam
            for entry in list:
                if entry[2] == highest_value1:
                    current_x1 = entry[0]
                    current_y1 = entry[1]
                    current_value1 = entry[2]

                    # Print statements for debugging
                    print("Found First Highest Child")
                    print("New X1")
                    print(current_x1)
                    print("New Y1")
                    print(current_y1)
                    print("New Value 1")
                    print(current_value1)

                    # After updating variables, break out of the loop
                    highest_value1 = 0
                    break
            
            # If we loop again, decrement the highest possible child score
            highest_value1 -= 1


        # Print statements for debugging
        print("Looking For Second Highest Child")
        
        # Create a variable that stores the highest variable
        highest_value2 = highest_value

        # While the highest possible score value is larger than 0
        while highest_value2 > 0:
            # Check the score values for all the children
            # If a child is found with a score matching the highest possible
            # score, update the x,y,value variables for the first local beam
            for entry in list:
                if entry[2] == highest_value2:
                    current_x2 = entry[0]
                    current_y2 = entry[1]
                    current_value2 = entry[2]

                    # Print statements for debugging
                    print("Found Second Highest Child")

                    # If the x,y,value variables of the second beam are different from
                    # those of the first beam, break out of the loop
                    if current_x1 != current_x2 and current_y1 != current_y2 and current_value1 != current_value2:   
                        # Print statements for debugging
                        print("New X2")
                        print(current_x2)
                        print("New Y2")
                        print(current_y2)
                        print("New Value 2")
                        print(current_value2)

                        # Breaking out of the loop
                        highest_value2 = 0
                        break

                    # If we make it to here, the second beam variables we found
                    # are invalid and cannot be used. Must loop
                    print("False Second Highest Child Found")

            # If we loop again, decrement the highest possible child score
            highest_value2 -= 1
        
        # Once two valid children are found, decrement the possible steps before
        # looping again
        steps_remaining -= 1

        # Print statements for debugging
        print("Step Taken")
        print("Steps Remaining")
        print(steps_remaining)
        print("______________________________________________________________________")


    # If we make it this far, we are out of steps

    # Print statements for debugging
    print("No More Steps")

    # Return the larger of the two current values
    if current_value1 > current_value2:
        return current_value1
    else:
        return current_value2


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
    return neighbors_list

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
# Simulation Code
#

# Hill Climbing 20 Steps
print('----------------------------------------------------------------------------------')
print('Experiment #1 : Hill Climbing 20 Steps')
print()


experiment_one_number_of_successes = 0
for i in range(10):
    print('GRID {} LAYOUT: '.format(i+1))
    print('---------------')
    print()
    example_grid = random_grid()
    for row in example_grid:
        print(row)
    value = hill_climbing(example_grid, 20)
    if(value == 5):
        experiment_one_number_of_successes += 1


print('End of Simulations for Experiment #1 : Hill Climbing 20 Steps')
print()
print()




# Hill Climbing 10 Steps 1 Restart
print('----------------------------------------------------------------------------------')
print('Experiment #2 : Hill Climbing 10 Steps & 1 Restart')
print()


experiment_two_number_of_successes = 0
for i in range(10):
    print('GRID {} LAYOUT: '.format(i+1))
    print('---------------')
    print()
    new_grid = random_grid()
    for row in new_grid:
        print(row)
    value = hill_climbing(new_grid, 10, 1)
    if(value == 5):
        experiment_two_number_of_successes += 1


print('End of Simulations for Experiment #2 : Hill Climbing 10 Steps & 1 Restart')
print()
print()




# Local Beam Search With 2 Beams & 20 Steps
print('----------------------------------------------------------------------------------')
print('Experiment #3 : Local Beam Search With 2 Beams & 20 Steps')
print()


#
# Simulation Code Goes Here
#
experiment_three_number_of_successes = 0


#value = local_beam_search(example_grid, 20)
print("End of Simulations for Experiment #3 : Local Beam Search With 2 Beams & 20 Steps")
#print(value)
print()
print()




# Simulated Annealing Modification
print('----------------------------------------------------------------------------------')
print('Experiment #4 : Simulated Annealing Modification')
print()


#
# Simulation Code Goes Here
#
experiment_four_number_of_successes = 0


#value = local_beam_search(example_grid, 20)
print("End of Simulations for Experiment #4 : Simulated Annealing Modification")
#print(value)
print()
print()




# Final Results
print('----------------------------------------------------------------------------------')
print('Final Results')
print("Experiment 1 : Hill Climbing 20 Steps : # of Successes:")
print(experiment_one_number_of_successes)
print("Experiment 1 # Hill Climbing 20 Steps : Success Rate:")
print(experiment_one_number_of_successes * 10, end ="%\n")
print("Experiment 2 : Hill Climbing 10 Steps & 1 Restart : # of Successes:")
print(experiment_two_number_of_successes)
print("Experiment 2 : Hill Climbing 10 Steps & 1 Restart : # Success Rate:")
print(experiment_two_number_of_successes * 10, end ="%\n")
print("Experiment 3 : Local Beam Search With 2 Beams & 20 Steps : # of Successes:")
print(experiment_three_number_of_successes)
print("Experiment 3 : Local Beam Search With 2 Beams & 20 Steps : # Success Rate:")
print(experiment_three_number_of_successes * 10, end ="%\n")
print("Experiment 4 : Simulated Annealing Modification : # of Successes:")
print(experiment_four_number_of_successes)
print("Experiment 4 : Simulated Annealing Modification : # Success Rate:")
print(experiment_four_number_of_successes * 10, end ="%")
