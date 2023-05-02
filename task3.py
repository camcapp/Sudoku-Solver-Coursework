from typing import List
import random

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

grid7 = [
        [9, 0, 6, 0, 0, 1, 0, 4, 0],
        [7, 0, 1, 2, 9, 0, 0, 6, 0],
        [4, 0, 2, 8, 0, 6, 3, 0, 0],
        [0, 0, 0, 0, 2, 0, 9, 8, 0],
        [6, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 9, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 3, 7, 0, 8, 4, 0, 9],
        [0, 4, 0, 0, 1, 3, 7, 0, 6],
        [0, 6, 0, 9, 0, 0, 1, 0, 8]]

grid8 = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0]]

grid9 = [
        [0, 3, 0, 4, 0, 0],
        [0, 0, 5, 6, 0, 3],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 3, 0, 5],
        [0, 6, 4, 0, 3, 1],
        [0, 0, 1, 0, 4, 6]]

grid10 = [
         [0, 2, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 6, 0, 4, 0, 0, 0, 0],
         [5, 8, 0, 0, 9, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 3, 0, 0, 4],
         [4, 1, 0, 0, 8, 0, 6, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 9, 5],
         [2, 0, 0, 0, 1, 0, 0, 8, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 3, 1, 0, 0, 8, 0, 5, 7]]

grid11 = [
         [0, 0, 0, 6, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 5, 0, 1],
         [3, 6, 9, 0, 8, 0, 4, 0, 0],
         [0, 0, 0, 0, 0, 6, 8, 0, 0],
         [0, 0, 0, 1, 3, 0, 0, 0, 9],
         [4, 0, 5, 0, 0, 9, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 3, 0, 0],
         [0, 0, 6, 0, 0, 7, 0, 0, 0],
         [1, 0, 0, 3, 4, 0, 0, 0, 0]]

grid12 = [
         [8, 0, 9, 0, 2, 0, 3, 0, 0],
         [0, 3, 7, 0, 6, 0, 5, 0, 0],
         [0, 0, 0, 4, 0, 9, 7, 0, 0],
         [0, 0, 2, 9, 0, 1, 0, 6, 0],
         [1, 0, 0, 3, 0, 6, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0, 3],
         [7, 0, 0, 0, 0, 0, 0, 0, 8],
         [5, 0, 0, 0, 0, 0, 0, 1, 4],
         [0, 0, 0, 2, 8, 4, 6, 0, 5]]



# Main function: Solve Sudoku
def solve_sudoku(board: List[List[int]]) -> bool:
    n = len(board)  # Size of the Sudoku
    m = int(n ** 0.5)  # Size of each small square in the Sudoku
    # Initialize all possible numbers
    possible = [[set(range(1, n + 1)) for _ in range(n)] for _ in range(n)]

    # Update possible values for cell (i, j)
    def update_possible(i: int, j: int, k: int) -> bool:
        conflict = False
        possible[i][j] = set([k])
        # Update other cells in the same row and column
        for x in range(n):
            if k in possible[i][x]:
                possible[i][x].remove(k)
                if len(possible[i][x]) == 0:
                    conflict = True
            if k in possible[x][j]:
                possible[x][j].remove(k)
                if len(possible[x][j]) == 0:
                    conflict = True
        # Update other cells in the same small square
        si, sj = m * (i // m), m * (j // m)
        for x in range(si, si + m):
            for y in range(sj, sj + m):
                if k in possible[x][y]:
                    possible[x][y].remove(k)
                    if len(possible[x][y]) == 0:
                        conflict = True
        return conflict

    # Wavefront propagation algorithm
    def wavefront_propagation() -> bool:
        while True:
            progress = False
            # Traverse each cell, find determined values and update
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 0 and len(possible[i][j]) == 1:
                        k = possible[i][j].pop()
                        board[i][j] = k
                        update_possible(i, j, k)
                        progress = True

            # If there is no progress, break the loop
            if not progress:
                break

        # If all cells have values, return True
        if all(board[i][j] != 0 for i in range(n) for j in range(n)):
            return True

        # Find the cell with the fewest optional values
        min_possible = float('inf')
        next_cell = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    num_possible = len(possible[i][j])
                    if num_possible < min_possible:
                        min_possible = num_possible
                        next_cell = (i, j)

        # If not found, return False
        if next_cell is None:
            return False

        # Traverse all possible values and try
        i, j = next_cell
        for k in random.sample(possible[i][j], len(possible[i][j])):
            if not update_possible(i, j, k):
                board[i][j] = k
                if wavefront_propagation():
                    return True
                board[i][j] = 0
            possible[i][j].add(k)

        return False

    # Update possible values based on initial board state
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                update_possible(i, j, board[i][j])

    return wavefront_propagation()

def sudoku_test(sudoku):
    if solve_sudoku(sudoku):  # This function accepts the variable name of the sudoku
        print("Solve successfully:")
        for row in sudoku:
            print(row)
    else:
        print("No solution")
    return sudoku

print(sudoku_test(grid1))
print(sudoku_test(grid2))
print(sudoku_test(grid3))
print(sudoku_test(grid4))
print(sudoku_test(grid5))
print(sudoku_test(grid6))
print(sudoku_test(grid7))
print(sudoku_test(grid8))
print(sudoku_test(grid9))
print(sudoku_test(grid10))
print(sudoku_test(grid11))
print(sudoku_test(grid12))
