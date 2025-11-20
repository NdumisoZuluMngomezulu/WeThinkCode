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

def locate_zeroes(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False

def possible_candidates(board, row, col):

    if board[row][col] != 0:
        return []
    
    possible_values = set([x for x in range(1,10)])
    #row
    for num in range(1, 9):
        if num in board[row]:
            if len(possible_values) > 0:
                possible_values.remove(num)
    #column
    for i in range(1, 9):
        num = board[i][col]
        if num in possible_values:
            if len(possible_values) > 0:
                possible_values.remove(num)
    #sub grid
    start_row = (row//3)*3
    start_col = (col//3)*3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            num = board[r][c]
            if num in possible_values:
                if len(possible_values) > 0:
                    possible_values.remove(num)

    return sorted(list(possible_values))
        
# board = sudoku_board("sudoku1.txt")
# print_grid(board)

def solve_iteration(textfile):
    board = sudoku_board(textfile)
    print_grid(board)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                set_values = possible_candidates(board, i, j)
                print(f"This zero {i, j}: {set_values}")
                if len(set_values) > 0:
                    board[i][j] = set_values[0]

    return board

board = solve_iteration("sudoku.txt")
print_grid(board)
print("+++++++++")
board = solve_iteration("sudoku.txt")
print_grid(board)
