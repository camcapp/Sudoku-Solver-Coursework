import random
import copy
import time

# Grids 1-4 are 2x2
grid1 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 3, 4],
    [3, 4, 2, 1]]

grid2 = [
    [1, 0, 4, 2],
    [4, 2, 1, 3],
    [2, 1, 0, 4],
    [3, 4, 2, 1]]

grid3 = [
    [1, 0, 4, 2],
    [4, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid4 = [
    [1, 0, 4, 2],
    [0, 2, 1, 0],
    [2, 1, 0, 4],
    [0, 4, 2, 1]]

grid5 = [
    [1, 0, 0, 2],
    [0, 0, 1, 0],
    [0, 1, 0, 4],
    [0, 0, 0, 1]]

grid6 = [
    [0, 0, 6, 0, 0, 3],
    [5, 0, 0, 0, 0, 0],
    [0, 1, 3, 4, 0, 0],
    [0, 0, 0, 0, 0, 6],
    [0, 0, 1, 0, 0, 0],
    [0, 5, 0, 0, 6, 4]]

grids = [(grid1, 2, 2), (grid2, 2, 2), (grid3, 2, 2), (grid4, 2, 2), (grid5, 2, 2)]
'''
===================================
DO NOT CHANGE CODE ABOVE THIS LINE
===================================
'''


def check_section(section, n):
    if len(set(section)) == len(section) and sum(section) == sum([i for i in range(1, n + 1)]):
        return True
    return False


def get_squares(grid, n_rows, n_cols):
    squares = []
    for i in range(n_cols):
        rows = (i * n_rows, (i + 1) * n_rows)
        for j in range(n_rows):
            cols = (j * n_cols, (j + 1) * n_cols)
            square = []
            for k in range(rows[0], rows[1]):
                line = grid[k][cols[0]:cols[1]]
                square += line
            squares.append(square)
    return squares


# To complete the first assignment, please write the code for the following function

def find_empty(grid):
    '''
	This function returns the index (i, j) to the first zero element in a sudoku grid
	If no such element is found, it returns None

	args: grid
	return: A tuple (i,j) where i and j are both integers, or None
	'''
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                return (i, j)
    return None


def get_potential_values(grid, row, col, n_rows, n_cols):
    n = n_rows * n_cols
    used_nums = set(grid[row]) | set(grid[i][col] for i in range(n))
    square_col = col // n_cols
    square_row = row // n_rows
    square_start_col = square_col * n_cols
    square_start_row = square_row * n_rows
    used_nums |= set(grid[i][j] for i in range(square_start_row, square_start_row + n_rows) for j in
                     range(square_start_col, square_start_col + n_cols))
    return set(range(1, n + 1)) - used_nums


def recursive_solve(grid, n_rows, n_cols):
    '''
	This function uses recursion to exhaustively search all possible solutions to a grid
	until the solution is found

	args: grid, n_rows, n_cols
	return: A solved grid (as a nested list), or None
	'''
    n = n_rows * n_cols
    empty_cell = find_empty(grid)
    if not empty_cell:
        return grid
    row, col = empty_cell
    potential_values = get_potential_values(grid, row, col, n_rows, n_cols)
    if not potential_values:
        return None
    for val in sorted(potential_values, key=lambda x: len(get_potential_values(grid, row, col, n_rows, n_cols))):
        grid[row][col] = val
        result = recursive_solve(grid, n_rows, n_cols)
        if result is not None:
            return result
        grid[row][col] = 0
    return None


def check_solution(grid, n_rows, n_cols):
    '''
	This function is used to check whether a sudoku board has been correctly solved

	args: grid - representation of a suduko board as a nested list.
	returns: True (correct solution) or False (incorrect solution)
	'''
    n = n_rows * n_cols
    rows = grid
    columns = [[grid[i][j] for i in range(n)] for j in range(n)]
    squares = get_squares(grid, n_rows, n_cols)
    for section in rows + columns + squares:
        if not check_section(section, n):
            return False
    return True


def random_solve(grid, n_rows, n_cols, max_tries=50000):
    '''
	This function uses random trial and error to solve a Sudoku grid

	args: grid, n_rows, n_cols, max_tries
	return: A solved grid (as a nested list), or the original grid if no solution is found
	'''

    for i in range(max_tries):
        possible_solution = fill_board_randomly(grid, n_rows, n_cols)
        if check_solution(possible_solution, n_rows, n_cols):
            return possible_solution

    return grid


def fill_board_randomly(grid, n_rows, n_cols):
    '''
	This function will fill an unsolved Sudoku grid with random numbers

	args: grid, n_rows, n_cols
	return: A grid with all empty values filled in
	'''
    n = n_rows * n_cols
    # Make a copy of the original grid
    filled_grid = copy.deepcopy(grid)

    # Loop through the rows
    for i in range(len(grid)):
        # Loop through the columns
        for j in range(len(grid[0])):
            # If we find a zero, fill it in with a random integer
            if grid[i][j] == 0:
                filled_grid[i][j] = random.randint(1, n)

    return filled_grid


def solve(grid, n_rows, n_cols):
    '''
	Solve function for Sudoku coursework.
	Comment out one of the lines below to either use the random or recursive solver
	'''

    # return random_solve(grid, n_rows, n_cols)
    return recursive_solve(grid, n_rows, n_cols)


'''
===================================
DO NOT CHANGE CODE BELOW THIS LINE
===================================
'''


def get_diff(prev_grid, grid):
    dif_found = False
    value = location = None
    for row in range(len(prev_grid)):
        for col in range(len(prev_grid[0])):
            if prev_grid[row][col] != grid[row][col]:
                dif_found = True
                value = grid[row][col]
                location = (row, col)
                break
        if dif_found:
            break
    return [value, location]


def print_command(prev_grid, grid):
    [value, location] = get_diff(prev_grid, grid)
    print("Put", value, "in location", location)


def main(args: list):
    explain_flag = 'explain' in args
    points = 0

    print("Running test script for coursework 1")
    print("====================================")

    for (i, (grid, n_rows, n_cols)) in enumerate(grids):
        print("Solving grid: %d" % (i + 1))
        start_time = time.time()
        prev_grid = copy.deepcopy(grid)
        solution = solve(grid, n_rows, n_cols)
        elapsed_time = time.time() - start_time
        print("Solved in: %f seconds" % elapsed_time)
        if explain_flag:
            print_command(prev_grid, grid)
        print(solution)
        if check_solution(solution, n_rows, n_cols):
            print("grid %d correct" % (i + 1))
            points = points + 10
        else:
            print("grid %d incorrect" % (i + 1))

    print("====================================")
    print("Test script complete, Total points: %d" % points)


if __name__ == "__main__":
    args = ['explain']
    main(args)
