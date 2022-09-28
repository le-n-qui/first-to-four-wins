# import libraries
import random

random.seed(42)

# Grid size
# Row size
ROW_SIZE = 8
# Column size
COL_SIZE = 8

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
		row.append(random.randint(1, 5))
	# place the filled row into grid
	grid.append(row)

print('GRID STATUS: ')
print('-----------')
print(grid)

