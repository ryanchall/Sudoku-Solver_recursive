import numpy as np

# Edit this 2D array to match the puzzle you wish to solve
sudoku_data = np.array([
    [7, 0, 0, 6, 0, 0, 8, 0, 0],
    [0, 0, 0, 2, 5, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 7, 0, 3],
    [0, 0, 0, 0, 4, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 8, 0, 3, 0, 0, 0, 0, 0],
    [0, 4, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 4, 0]
]).astype(int)

# Create an array of 1's/0's based on whether or not the corresponding sudoku number started as 0 (is editable)
editable_data = np.array([]).astype(int)
for row in sudoku_data:
    for colm in row:
        if colm == 0:
            editable_data = np.append(editable_data, True)
        else:
            editable_data = np.append(editable_data, False)
# Transform to a 9x9
editable_data = np.reshape(editable_data, (-1, 9))
