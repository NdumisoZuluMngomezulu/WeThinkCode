from collections import namedtuple

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
    print("\t"*13)
    for row in range(0, 9):
        formatted_str = "|" + "\t"
        for col in range(0, 9):
            if col in [3, 6]:
                formatted_str += "|\t"
            formatted_str += str(board[row][col]) + "\t"
        formatted_str += "|"
        print(formatted_str)
        if row in [2, 5]:
            print("-\t" * 13)
        print("\t"*13)

board = sudoku_board("sudoku.txt")
board_printer(board)

def insert_sorted(zone, zones):
    if len(zones) == 0:
        zones.append(zone)
    else:
        insert = False
        for i in range(0, len(zones)):
            if zone["len"] > zones[i]["len"]:
                zones.insert(i, zone)
                inserted = True
                break
            else:
                continue
        if not insert:
            zones.append(zone)

def generate_square_coords():
    square_coordinates = []
    row_begin = 0
    row_end = 2
    col_begin = 0
    col_end = 2

    while len(square_coordinates) < 9:
        square_coordinates.append(
            {"row_begin" : row_begin,
            "row_end" : row_end,
            "col_begin" : col_begin,
            "col_end" : col_end}
        )
        if col_begin < 6 and col_end < 8:
            col_begin += 3
            col_end += 3
        else:
            col_begin = 0
            col_end = 2
            row_begin += 0
            row_end += 2
    
    return tuple(square_coordinates)

def extract_zones(board):
    zones = []
    #extract rows
    for row in range(0, 9):
        zone = {}
        zone["type"] = "row"
        zone["len"] = len(board[row]) - board[row].count(0)
        zone["coord"] = row
        insert_sorted(zone, zones)
    #extract columns
    for col in range(0, 9):
        nonzero_elements = 0
        for row in range(0, 9):
            if board[row][col] != 0:
                nonzero_elements += 1
        zone = {}
        zone["type"] = "col"
        zone["len"] = nonzero_elements
        zone["coord"] = col
        insert_sorted(zone, zones)
    #extract squares info
    for square in generate_square_coords():
        nonzero_elements = 0
        for row in range(square["row_begin"], square["row_end"]+1):
            for col in range(square["col_begin"], square["col_end"]+1):
                if board[row][col] != 0:
                    nonzero_elements += 1
        zone = {}
        zone["type"] = "square"
        zone["len"] = nonzero_elements
        zone["coord"] = tuple(square.values())
        insert_sorted(zone, zones)
    
    return zones

def get_zone_elements(key, row, col, puzzle):
    elements = []
    if key == "row":
        elements = puzzle[row]
    elif key == "col":
        for i in range(9):
            elements.append(puzzle[i][col])
    else:
        row_start = (row//3)*3
        col_start = (col//3)*3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                elements.append(puzzle[i][j])
    return elements
    

def insert_possibilities(puzzle, row, col):
    if puzzle[row][col] == 0:
        row_elements = get_zone_elements("row", row, col, puzzle)
        col_elements = get_zone_elements("col", row, col, puzzle)
        square_elements = get_zone_elements("square", row, col, puzzle)
        numbers = [num for num in range(1, 10)]
        possibilities = [i for i in range(1, 10)]
        for possibility in numbers:
            if (possibility in row_elements) or (possibility in col_elements) or (possibility in square_elements):
                possibilities.remove(possibility)
        if len(possibilities) == 1:
            puzzle[row][col] = possibilities[0]

if __name__ == "__main__":
    puzzle = sudoku_board("sudoku.txt")
    for itirations in range(0, 3):
        zones = extract_zones(puzzle)
        for zone in zones:
            if zone["type"] == "row":
                row = zone["coord"]
                for col in range(0, 9):
                    insert_possibilities(puzzle, row, col)
            elif zone["type"] == "row":
                col = zone["coord"]
                for row in range(0, 9):
                    insert_possibilities(puzzle, row, col)
            else:
                row_begin = zone["coord"][0]
                row_end = zone["coord"][1]
                col_begin =zone["coord"][2]
                col_end = zone["coord"][3]
                for row in range(row_begin, row_end+1):
                    for col in range(col_begin, col_end+1):
                        insert_possibilities(puzzle, row, col)
    
    print("-"*50)
    board_printer(puzzle)
