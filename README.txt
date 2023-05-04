#Readme
# task 1 by Jiahao

This program is designed to solve 2x2 and 3x3 Sudoku puzzles. It utilizes a recursive algorithm to exhaustively search all possible solutions to a given puzzle until a solution is found. 

Program Output

The program outputs the solved puzzle for each puzzle in the `grids` list at the bottom of the code. The output will be in the form of a nested list. 

Important Notes

- Do not change any code above the line that reads `DO NOT CHANGE CODE ABOVE THIS LINE`.
- The `grids` list contains the Sudoku puzzles to be solved. You can add your own puzzles to this list by adding a nested list of integers representing the puzzle.
- The program can only solve 2x2 and 3x3 Sudoku puzzles. Any other puzzle sizes will result in an error.
- The program will only output the first solution it finds. If a puzzle has multiple solutions, the program will not find all of them.

Task 2 - by Alper, Cameron
-> Using Flags -explain and -file INPUT OUTPUT
    + Flags can be provided in any order
    + explain flag
        Sample command
            python alper_flags.py -explain

    + file flag
        - INPUT and OUTPUT file are processed under the same folder as project
        - INPUT file must exist
        - If no OUTPUT file exists, a file is created and filled.
            Sample command
                python alper_flags.py -file easy1.txt easy1-out.txt

        - INPUT file format
            a. Each row in the input file represents a row in the game
            b. Numbers are separated by comma
            c. Empty location are represented by zero

    + More sample commands
        python alper_flags.py -explain -file abc.txt cba.txt
        python alper_flags.py -file abc.txt cba.txt -explain
        

#task 3 by Zili
Introduction

This project contains a Sudoku solver written in Python. It uses a wavefront propagation algorithm to solve Sudoku puzzles.

Usage

To use the Sudoku solver, simply provide a 2D list of integers to the function solve_sudoku(board: List[List[int]]) -> bool. The 2D list represents a Sudoku grid, where 0s represent empty cells and other integers represent pre-filled cells. This function will modify the input grid in-place and fill it with the solution, if a solution exists.

There's also a function sudoku_test(sudoku) which will print the Sudoku grid before and after solving it.

Implementation

The main algorithm is based on the concept of wavefront propagation. This algorithm iteratively determines the values for empty cells based on the remaining possible values for each cell. It also takes advantage of the dependency between cells in the same row, column, and square.

The solve_sudoku function first initializes a possible-value set for each cell. Then, for each pre-filled cell, it updates the possible-value set of every other cell in the same row, column, and square, excluding the value of the pre-filled cell.

The wavefront propagation process is then initiated. During each iteration, the algorithm checks each cell. If a cell has only one possible value left, it fills the cell with that value and updates the possible-value sets of other cells accordingly.

This process repeats until no progress can be made. If all cells have been filled, the function returns True. Otherwise, it finds an empty cell with the fewest possible values and iteratively fills it with each of its possible values. If the Sudoku can be solved with one of these values, the function returns True. If no solution is found, the function backtracks and returns False.

# crousework 3 all parts by Cameron
To run the profile flag, type into terminal: ./coursework_3_all_parts.py --profile. 
You can change the grids that the flag works for by going into the code, and changing/adding to the grids.

To run the hint flag, type into the terminal./coursework_3_all_parts.py --hint N 
N can be any number of hints. To change the grid the hint is for, you can change the grid passed into the function in the function titled 'main'.
