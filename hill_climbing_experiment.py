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
    if(random.randint(0, 1) == 1):
        return 1
    elif(random.randint(0, 1) == 1):
        return 2
    elif(random.randint(0, 1) == 1):
        return 3
    elif(random.randint(0, 1) == 1):
        return 4
    elif(random.randint(0, 1) == 1):
        return 5
    else:
        return generate_value()


print('GRID STATUS: ')
print('-----------')
print()
example_grid = random_grid()
for row in example_grid:
	print(row)

