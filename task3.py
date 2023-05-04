from typing import List, Tuple
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

def solve_sudoku(board: List[List[int]]) -> bool:
    n = len(board)
    m = int(n ** 0.5)
    possible = [[set(range(1, n + 1)) for _ in range(n)] for _ in range(n)]

    def update_possible(i: int, j: int, k: int) -> bool:
        conflict = False
        possible[i][j] = set([k])
        for x in range(n):
            if k in possible[i][x]:
                possible[i][x].remove(k)
                if len(possible[i][x]) == 0:
                    conflict = True
            if k in possible[x][j]:
                possible[x][j].remove(k)
                if len(possible[x][j]) == 0:
                    conflict = True
        si, sj = m * (i // m), m * (j // m)
        for x in range(si, si + m):
            for y in range(sj, sj + m):
                if k in possible[x][y]:
                    possible[x][y].remove(k)
                    if len(possible[x][y]) == 0:
                        conflict = True
        return conflict

    def wavefront_propagation() -> bool:
        while True:
            progress = False
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 0 and len(possible[i][j]) == 1:
                        k = possible[i][j].pop()
                        board[i][j] = k
                        update_possible(i, j, k)
                        progress = True

            if not progress:
                break

        if all(board[i][j] != 0 for i in range(n) for j in range(n)):
            return True

        min_possible = float('inf')
        next_cell = None
        for i in range(n):
            for j in range(n):
                if board[i][j] == 0:
                    num_possible = len(possible[i][j])
                    if num_possible < min_possible:
                        min_possible = num_possible
                        next_cell = (i, j)

        if next_cell is None:
            return False

        i, j = next_cell
        for k in random.sample(possible[i][j], len(possible[i][j])):
            if not update_possible(i, j, k):
                board[i][j] = k
                if wavefront_propagation():
                    return True
                board[i][j] = 0
            possible[i][j].add(k)

        return False

    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                update_possible(i, j, board[i][j])

    return wavefront_propagation()

if solve_sudoku(grid1):
    print("Solve successfully：")
    for row in grid1:
        print(row)
else:
    print("No solution")
