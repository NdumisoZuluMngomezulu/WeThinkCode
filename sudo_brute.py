import random
import sys

def solve_sudoku(board):
    # Initialize possibilities for each empty cell
    possibilities = {}
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                possible_nums = set(range(1, 10))
                # Eliminate numbers already in row, column, and 3x3 block
                for i in range(9):
                    if board[r][i] != 0:
                        possible_nums.discard(board[r][i])
                    if board[i][c] != 0:
                        possible_nums.discard(board[i][c])
                
                start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        if board[i][j] != 0:
                            possible_nums.discard(board[i][j])
                
                possibilities[(r, c)] = possible_nums

    def sudoku_board(textfile):
    
    lines = []
    with open(textfile, "r") as file:
        for line in file:
            line = line.replace("\n", " ")
            if line.strip():
                lines.append(line)
    board = []
    for i, element in enumerate(lines):
        line = [int(char) for char in element if char != " "]
        #line = [char for char in line if char != 0 else char = " "]
        board.append(line)
    
    return board

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" "),
        print()

    changed = True
    while changed:
        changed = False
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    current_possibilities = possibilities[(r, c)]
                    if len(current_possibilities) == 1:
                        # Single Position found
                        num_to_place = current_possibilities.pop()
                        board[r][c] = num_to_place
                        changed = True
                        
                        # Update possibilities of affected cells
                        for i in range(9):
                            if (r, i) in possibilities and board[r][i] == 0:
                                possibilities[(r, i)].discard(num_to_place)
                            if (i, c) in possibilities and board[i][c] == 0:
                                possibilities[(i, c)].discard(num_to_place)
                        
                        start_row, start_col = 3 * (r // 3), 3 * (c // 3)
                        for i in range(start_row, start_row + 3):
                            for j in range(start_col, start_col + 3):
                                if (i, j) in possibilities and board[i][j] == 0:
                                    possibilities[(i, j)].discard(num_to_place)
    
    return board # Returns the solved or partially solved board

board = sudoku_board("sudoku.txt")
print_grid(board)
print("\n")
print_grid(solve_sudoku(board))



