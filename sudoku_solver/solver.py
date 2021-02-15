import numpy as np
import time

grid = [[8,0,0,0,0,0,0,0,0],
        [0,0,3,6,0,0,0,0,0],
        [0,7,0,0,9,0,2,0,0],
        [0,5,0,0,0,7,0,0,0],
        [0,0,0,0,4,5,7,0,0],
        [0,0,0,1,0,0,0,3,0],
        [0,0,1,0,0,0,0,6,8],
        [0,0,8,5,0,0,0,1,0],
        [0,9,0,0,0,0,4,0,0]]



def sudoku_possibilites(initial_sudoku_grid, y, x, n):
    for i in range(0,9):
        if initial_sudoku_grid[y][i] == n:
            return False
    for i in range(0,9):
        if initial_sudoku_grid[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0,3):
        for j in range(0,3):
            if initial_sudoku_grid[y0+i][x0+j] == n:
                return False       
    return True

start = time.time()

def sudoku_solver(sudoku_grid):
    
    for y in range(9):
        for x in range(9):
            if sudoku_grid[y][x] == 0:
                for n in range(1,10):
                    if sudoku_possibilites(sudoku_grid, y, x, n):
                        sudoku_grid[y][x] = n
                        sudoku_solver(sudoku_grid) 
                        sudoku_grid[y][x] = 0
                return 

    print(np.matrix(sudoku_grid))
    
    print('Solved in %0.2f seconds' % (time.time() - start))
    
    input('More?')

print(sudoku_solver(grid))