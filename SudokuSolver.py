# Created by George Calderon for CPSC 351
import threading
import copy

puzzle = [[6, 2, 4, 5, 3, 9, 1, 8, 7],  # valid solution
          [5, 1, 9, 7, 2, 8, 6, 3, 4],
          [8, 3, 7, 6, 1, 4, 2, 9, 5],
          [1, 4, 3, 8, 6, 5, 7, 2, 9],
          [9, 5, 8, 2, 4, 7, 3, 6, 1],
          [7, 6, 2, 3, 9, 1, 4, 5, 8],
          [3, 7, 1, 9, 5, 6, 8, 4, 2],
          [4, 9, 6, 1, 8, 2, 5, 7, 3],
          [2, 8, 5, 4, 7, 3, 9, 1, 6]]
'''
puzzle = [[6, 2, 4, 5, 3, 9, 1, 8, 7],  # invalid solution
          [5, 1, 9, 7, 2, 8, 6, 3, 4],
          [8, 3, 7, 6, 1, 4, 2, 9, 5],
          [1, 4, 3, 8, 6, 5, 7, 2, 9],
          [9, 5, 8, 2, 5, 7, 3, 6, 1],
          [7, 6, 2, 3, 9, 1, 4, 5, 8],
          [3, 7, 1, 9, 5, 6, 8, 4, 2],
          [4, 9, 6, 1, 8, 2, 5, 7, 3],
          [2, 8, 5, 4, 7, 3, 9, 1, 6]]
'''

checkNums = {1, 2, 3, 4, 5, 6, 7, 8, 9}
valid = True


def check_row(row):
    global checkNums
    global valid
    copy_nums = copy.copy(checkNums)
    for x in range(9):
        for i in range(9):  # this loops removes nums 1-9 from the list
            if puzzle[row][x] in copy_nums:
                copy_nums.remove(puzzle[row][x])  # removes element from the list to check solution later
                break
    if copy_nums:  # if the list is not empty, then we have a wrong solution
        print("invalid row solution at row %d" % (row + 1))  # left ambiguous to allow person to fix puzzle on their own
        valid = False


def check_column(column):
    global checkNums
    global valid
    copy_nums = copy.copy(checkNums)
    for x in range(9):
        for i in range(9):  # this loops removes nums 1-9 from the list
            if puzzle[x][column] in copy_nums:
                copy_nums.remove(puzzle[x][column])  # removes element from the list to check solution later
                break
    if copy_nums:  # if the list is not empty, then we have a wrong solution
        print("invalid column solution at column %d" % (column + 1))  # left ambiguous to allow person to fix puzzle
        valid = False


def check_grid(grid):  # grids numbered from left to right
    global checkNums
    global valid
    copy_nums = copy.copy(checkNums)
    grid_x = grid // 3 * 3  # this deals with the x offset
    grid_y = grid % 3 * 3  # this deals with the y offset
    for x in range(grid_x, grid_x + 3):
        for y in range(grid_y, grid_y + 3):
            for i in range(9):  # this loops removes nums 1-9 from the list
                if puzzle[x][y] in copy_nums:
                    copy_nums.remove(puzzle[x][y])  # removes element from the list to check solution later
                    break

    if copy_nums:  # if the list is not empty, then we have a wrong solution
        print("invalid grid solution at grid %d" % (grid + 1))  # left ambiguous to allow person to fix puzzle on own
        valid = False


threads = []
for index in range(9):
    t = threading.Thread(target=check_row(index))
    t1 = threading.Thread(target=check_column(index))
    threads.append(t)
    threads.append(t1)
    t.start()
    t1.start()
    check_grid(index)

# all printed errors are regular numbers, not index numbers. so column 1 will be column[0]

if valid:
    print("Sudoku solution is valid!")
