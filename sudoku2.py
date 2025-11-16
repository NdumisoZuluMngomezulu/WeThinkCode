import random

def sudoku_board(textfile):
    lines = []
    with open(textfile, "r") as file:
        for line in file:
            line = line.replace("\n", " ")
            if line.strip():
                lines.append(line)
    board = []
    for i, element in enumerate(lines):
        line = [char for char in element if char != " "]
        #line = [char for char in line if char != 0 else char = " "]
        board.append(line)
    
    return board

def board_printer(board):
    array = ["0","1","2","3","4","5","6","7","8"]
    print(" ", array)
    for i, row in enumerate(board):
        print(i, row, end=" ")
        print()

def solve_sudoku(board):
    find = zero_locator(board)
    if not find:
        return True  # Puzzle solved
    else:
        row, col = find.split(",")

    for num in range(1, 10):  # Try numbers 1 to 9
        if play_validator(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True  # Solution found
            
            board[row][col] = 0  #Backtrack: reset the cell

    return False  # No solution found for this path

def zero_locator(board):
    for row in range(9):
        for column in range(9):
            if board[row][column] == 0:
                return f"{row}, {column}" #(row, column)
    return None

def play_validator(board, num, row, col):
    """
    Checks if placing 'num' at 'pos' (row, col) is valid according to Sudoku rules.
    """

    # Check row
    for column in range(9):
        if board[row][col] == num and col != column:
            return False

    # Check column
    for rows in range(9):
        if board[rows][col] == num and row != rows:
            return False

    # Check 3x3 box
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3

    for rw in range(box_row_start, box_row_start + 3):
        for clm in range(box_col_start, box_col_start + 3):
            if board[rw][clm] == num and (rw, clm) != (row, col):
                return False

    return True

# Example Usage:
if __name__ == "__main__":
    board = sudoku_board("sudoku.txt")
    board_printer(board)

    if solve_sudoku(board):
        print("Solved Sudoku:")
        board_printer(board)
    else:
        print("No solution exists for this Sudoku puzzle.")
