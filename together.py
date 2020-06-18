import numpy as np
import os

  ###############
 ## Ryan Hall ##
###############

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

# Create an array of 1's/0's based on whether or not the corresponding sudoku number started as 0 (1 = is editable/started as 0)
editable_data = np.array([]).astype(int)
for row in sudoku_data:
    for colm in row:
        if colm == 0:
            editable_data = np.append(editable_data, True)
        else:
            editable_data = np.append(editable_data, False)
# Transform to a 9x9
editable_data = np.reshape(editable_data, (-1, 9))


blocks = ([1, 2, 3], [4, 5, 6], [7, 8, 9]) # blocks are ordered left to right, top to bottom

def main():
    global num
    backtracking = False

    row_num = 0
    while row_num <= 8:
        col_num = 0

        while col_num <= 8:
            if editable_data[row_num, col_num] == 1:
                num = sudoku_data[row_num, col_num]
                
                if backtracking == True:
                    if num < 9:
                        if add_num(row_num, col_num) == True:
                            backtracking = False
                        else:
                            sudoku_data[row_num, col_num] = 0
                            row_num, col_num = backtrack_one_coor(row_num, col_num)
                            continue
                    else:
                        sudoku_data[row_num, col_num] = 0
                        row_num, col_num = backtrack_one_coor(row_num, col_num)
                        continue
                
                else:
                    if add_num(row_num, col_num) == False:
                        backtracking = True
                        row_num, col_num = backtrack_one_coor(row_num, col_num)
                        continue

            elif backtracking == True:
                row_num, col_num = backtrack_one_coor(row_num, col_num)
                continue

            col_num += 1
        row_num += 1
    print(sudoku_data)
    os.system('pause')


def add_num(row_num, col_num):
    # Depending on the row, select options for block 1,2,3 or 4,5,6 or 7,8,9 (respectively in code)
    if row_num in range(0, 3):
        block = blocks[0]
    elif row_num in range(3, 6):
        block = blocks[1]
    elif row_num in range(6, 9):
        block = blocks[2]

    # Depending on the column, select the first, second, or third option (respectively in code)
    if col_num in range(0, 3):
        block = block[0]
    elif col_num in range(3, 6):
        block = block[1]
    elif col_num in range(6, 9):
        block = block[2]
    
    # With block established, trim the data to include the correct block
    if block == 1:
        block = sudoku_data[0:3, 0:3]
    elif block == 2:
        block = sudoku_data[0:3, 3:6]
    elif block == 3:
        block = sudoku_data[0:3, 6:9]
    elif block == 4:
        block = sudoku_data[3:6, 0:3]
    elif block == 5:
        block = sudoku_data[3:6, 3:6]
    elif block == 6:
        block = sudoku_data[3:6, 6:9]
    elif block == 7:
        block = sudoku_data[6:9, 0:3]
    elif block == 8:
        block = sudoku_data[6:9, 3:6]
    elif block == 9:
        block = sudoku_data[6:9, 6:9]
    
    for i in range(1, 10):
        if i in sudoku_data[row_num] or i in sudoku_data[:, col_num] or i in block:
            if i == 9:
                added_number = False
        elif i > num:
            sudoku_data[row_num, col_num] = i
            added_number = True
            break
    return added_number

def backtrack_one_coor(row_num, col_num):
    if col_num > 0:
        col_num -= 1
    else:
        col_num = 8
        row_num -= 1
    return row_num, col_num


main()
