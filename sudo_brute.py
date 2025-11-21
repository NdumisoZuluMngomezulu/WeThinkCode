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

def solve_iteration(board):
    dictionary = {}
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                dictionary[(i, j)] = possible_candidates(board, i, j)
                
        
    # dictionary = sorted(dictionary.items(), key=lambda x: len(x[1]))
    # first_entry = next(iter(dictionary))
    # board[first_entry[0]][first_entry[1]] = dictionary[first_entry]
    # dictionary = list(dictionary.items())
    # del dictionary[0]
    # dictionary = dict(dictionary)

    #return print_grid(board)
board = sudoku_board("sudoku.txt")
# print_grid(board)

# print(solve_iteration(board))
dictionary = {(0, 3): [3, 4], (0, 7): [1, 4, 9], (1, 2): [2,5,8,9]}
dictionary = sorted(dictionary.items(), key=lambda x: len(x[1]))
first_entry = next(iter(dictionary))[0]
print(first_entry)
print(dictionary[(0, 3)])
#board[first_entry[0]][first_entry[1]] = dictionary[first_entry]
# dictionary = list(dictionary.items())
# del dictionary[0]
# dictionary = dict(dictionary)



