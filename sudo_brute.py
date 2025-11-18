import random
import sys
from collections import Counter

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

def board_printer(board):
    array = ["0","1","2","3","4","5","6","7","8"]
    print(" ", array)
    for i, row in enumerate(board):
        print(i, row, end=" ")
        print()

def check_play(board, row, column, choice):
    if 0 <= row < 9 and 0 <= column < 9 and choice not in board[row] and choice not in [rows[column] for rows in board]:
        first_grid = [rows[0:3] for rows in board[0:3]]
        second_grid = [rows[3:6] for rows in board[0:3]]
        third_grid = [rows[6:9] for rows in board[0:3]]
        fourth_grid = [rows[0:3] for rows in board[3:6]]
        fifth_grid = [rows[3:6] for rows in board[3:6]]
        sixth_grid = [rows[6:9] for rows in board[3:6]]
        seventh_grid = [rows[0:3] for rows in board[6:8]]
        eight_grid = [rows[3:6] for rows in board[6:8]]
        nineth_grid = [rows[6:9] for rows in board[6:8]]

        #x = random.randint(0,9), y = random.randint(0, 9)
        x = row
        y = column
        #x is the row, y is the column
        if x in range(0, 3) and y in range(0, 3):
            if choice not in first_grid:
                board[x][y] = choice 
                return board
        if x in range(0, 3) and y in range(3, 6):
            if choice not in second_grid:
                board[x][y] = choice 
                return board
        if x in range(0, 3) and y in range(6, 9):
            if choice not in third_grid:
                board[x][y] = choice 
                return board
        if x in range(3, 6) and y in range(3, 6):
            if choice not in fourth_grid:
                board[x][y] = choice 
                return board
        if x in range(3, 6) and y in range(0, 3):
            if choice not in fifth_grid:
                board[x][y] = choice 
                return board
        if x in range(3, 6) and y in range(3, 6):
            if choice not in sixth_grid:
                board[x][y] = choice 
                return board
        if x in range(6, 8) and y in range(0, 3):
            if choice not in seventh_grid:
                board[x][y] = choice 
                return board
        if x in range(6, 8) and y in range(3, 6):
            if choice not in eight_grid:
                board[x][y] = choice 
                return board
        if x in range(6, 8) and y in range(6, 9):
            if choice not in nineth_grid:
                board[x][y] = choice 
                return board
    return None

def get_random(start, end, exclude):
    while True:
        num = random.randint(start, end)
        if num not in exclude:
            return num

def locate_zeroes(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
def zero_loop_condition(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return True
    return False
#brute force method

board = sudoku_board("sudoku1.txt")
board_printer(board)
print(f"""
        Hi There dummy🙋🏾👋🏾.
        I hear you can't solve a simple sudoku puzzle
        I will teach you how to solve sudoku as i solve it
        This is the brute force method
        I will simply search from the first index [0][0] to the last [8][8]
        When i find an empty space i will generate a random number
        I will then check if the number does not already exist in the row and column
        While also checking if it does not already exist in it's 3x3 sub-grid
        All this will be done by calling the 'check_play' method to validate if it's a valid choice
        This will be repeated until the puzzle is solved
""")
print("""    I am iterating by rows first, then iterating by the columns in each row. This is a nested For Loop 
    I set a variable called playable to the boolean value False\n       I'll now enter a while with playable as the condition
    Once i find a suitable choice for the position i am in using the function check_play, i will add it to the board""")

while zero_loop_condition(board):
    location = locate_zeroes(board)
    if check_play(board, row, column,choice)
