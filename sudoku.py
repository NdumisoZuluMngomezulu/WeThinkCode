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

def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" "),
        print()

def zero_locator(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False

def check_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

def check_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# Returns a boolean which indicates
# whether any assigned entry
# within the specified 3x3 box
# matches the given number

def check_subgrid(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

def check_location_is_safe(arr, row, col, num):

    return (not check_row(arr, row, num) and
            (not check_col(arr, col, num) and
             (not check_subgrid(arr, row - row % 3,
                              col - col % 3, num))))
    # box_row_start = (row // 3) * 3
    # box_col_start = (col // 3) * 3

    # for rw in range(box_row_start, box_row_start + 3):
    #     for clm in range(box_col_start, box_col_start + 3):
    #         if board[rw][clm] == num and (rw, clm) != (row, col):
    #             return False

def solve_sudoku(arr):
    l = [0, 0] 

    # If there is no unassigned
    # location, we are done
    if(not zero_locator(arr, l)):
        return True

    # Assigning list values to row and col
    # that we got from the above Function
    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 10):

        # if looks promising
        if(check_location_is_safe(arr,
                                  row, col, num)):

            # make tentative assignment
            arr[row][col] = num

            # return, if success,
            # ya !
            if(solve_sudoku(arr)):
                return True

            # failure, unmake & try again
            arr[row][col] = 0

    # this triggers backtracking
    return False

if __name__ == "__main__":
    board = sudoku_board("sudoku.txt")
    print(board)

    if (solve_sudoku(board)):
        board_printer(board)
    else:
        print("Solution Does Not Exist")
