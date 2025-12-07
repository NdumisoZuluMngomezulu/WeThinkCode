import sys

def make_ways(textfile):
    grid = []
    with open(textfile) as file:
        for line in file:
            row = []
            for char in line:
                if char != ' ' and char != '\n':
                    row.append(char)
            row = [int(x) for x in row]
            grid.append(row)
    
    return grid

def display_grid(grid):
    for line in grid:
        for char in line:
            print(char, end=" ")
        print()

path = make_ways('pathways.txt')

def move_toy(grid):
    print(f"""Hi There 👋🏾
        Congratulations on your new purchase 🚘
        This is your first driving lesson
        =========COMMAND LIST===========
        L x for Left (x being the numbers of units to travel horizontally)
        R x for Right (x being the numbers of units to travel horizontally)
        D y for Down (y being the number of units to travel vertically)
        U y for Up (y being the number of units to travel vertically)
        Zeroes represent an open path
        Ones represent an obstacle  """)
    
    count = 0
    row , col = 0, 0
    grid[row][col] = "🚘"
    
    game_state = True
    while game_state:
        count += 1
        print("This is your current position")
        display_grid(grid)
        command = input("Enter command: ").lower().split()
        match command[0]:
            case "r":
                if grid[row][col + int(command[1])] == 0 and (col + int(command[1])) < 13 :
                    grid[row][col + int(command[1])] = "🚘"
                    grid[row][col] = 0
                    col += int(command[1])
                else:
                    sys.exit("Invalid move")
            case "l":
                if grid[row][col - int(command[1])] == 0 and (col - int(command[1])) >= 0 :
                    grid[row][col - int(command[1])] = "🚘"
                    grid[row][col] = 0
                    col -= int(command[1])
                else:
                    sys.exit("Invalid move")
            case "u":
                if grid[row - int(command[1])][col] == 0 and (row - int(command[1])) >= 0 :
                    grid[row - int(command[1])][col] = "🚘"
                    grid[row][col] = 0
                    row -= int(command[1])
                else:
                    sys.exit("Invalid move")
            case "d":
                if grid[row + int(command[1])][col] == 0 and (row + int(command[1])) < 8 :
                    grid[row + int(command[1])][col] = "🚘"
                    grid[row][col] = 0
                    row += int(command[1])
                else:
                    sys.exit("Invalid move")
        game_state = True
        if count > 100:
            game_state = False

    return grid

display_grid(move_toy(path))
#map
"""
0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 0 0 0 1 1 1 1
1 1 1 1 1 1 0 0 0 1 1 1 1 
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 
0 0 0 1 1 1 0 0 0 1 1 1 1  
0 0 0 1 1 1 0 0 0 1 1 1 1 
0 0 0 0 0 0 0 0 0 0 0 0 0  
"""
