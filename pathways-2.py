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

def move(grid):
    print(f"""Hi There 👋🏾
        Congratulations on your new purchase 🚘
        This is your first driving lesson
        =========COMMAND LIST===========
        L x for Left (x being the numbers of units to travel horizontally)
        R x for Right (x being the numbers of units to travel horizontally)
        D y for Down (y being the number of units to travel vertically)
        U y for Up (y being the number of units to travel vertically)
        Zeroes represent an open path to the East
        Ones represent an open path to the West
        Eight's represent an openpath to the North
        Nine's represent an open path to the South """)
    
    count = 0
    row , col = 0, 0
    grid[row][col] = "🚔"
    dupli_grid = make_ways('second_pathways.txt')
    game_running = True
    while game_running:
        print("This is your current position")
        display_grid(grid)
        command = input("Enter your command(direction distance e.g l 5)").lower().split()
        match command[0]:
            case 'e':
                unoccupied = dupli_grid[row][col]
                if grid[row][col+int(command[1])] not in [0, 8, 9]:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 1 else sys.exit("This is an obstacle")
                elif (col+int(command[1])) > 18:
                    raise ValueError("You've reached road limits")  
                grid[row][col+int(command[1])] = "🚔"
                grid[row][col] = unoccupied
                col += int(command[1])
            case 'w':
                unoccupied = dupli_grid[row][col]
                if grid[row][col+int(command[1])] not in [1, 8, 9]:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 0 else sys.exit("This is an obstacle")
                elif (col+int(command[1])) < 0:
                    raise ValueError("You've reached road limits")  
                grid[row][col-int(command[1])] = "🚔"
                grid[row][col] = unoccupied
                col -= int(command[1])
            case 'n':
                unoccupied = dupli_grid[row][col]
                if unoccupied == 0 and grid[row-int(command[1])][col] != 8:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 9 else sys.exit("This is an obstacle")
                elif (row-int(command[1])) < 0:
                    raise ValueError("You've reached road limits")  
                elif unoccupied == 1 and grid[row-1][col] != 0 and grid[row-int(command[1])][col] != 8:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 9 else sys.exit("This is an obstacle")
                grid[row-int(command[1])][col] = "🚔"
                grid[row][col] = unoccupied
                row -= int(command[1])
            case 's':
                #print(f"{col+int(command[1])}====>")
                unoccupied = dupli_grid[row][col]
                if unoccupied == 1 and grid[row+int(command[1])][col] != 9:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 8 else sys.exit("This is an obstacle")
                elif (row+int(command[1])) > 9:
                    raise ValueError("You've reached road limits")  
                elif unoccupied == 0 and grid[row+1][col] != 1 and grid[row-int(command[1])][col] != 8:
                    sys.exit("Wrong Direction ") if grid[row][col+int(command[1])] == 9 else sys.exit("This is an obstacle")
                grid[row+int(command[1])][col] = "🚔"
                grid[row][col] = unoccupied
                row += int(command[1])
            case 'nw':
                unoccupied = dupli_grid[row][col]
                if unoccupied != 8:
                    raise ValueError("Invalid move")
                elif unoccupied == 8 and dupli_grid[row+1][col] not in [1, 8]:
                    raise ValueError("Invalid move")
                grid[row + 1][col - 1] = "🚔"
                row +=1
                col -= 1
            case 'ne':
                unoccupied = dupli_grid[row][col]
                if unoccupied != 8:
                    raise ValueError("Invalid Move")
                if unoccupied == 8 and dupli_grid[row+1][col] != 1 and dupli_grid[row+2][col+1] != 0:
                    raise ValueError("Invalid Move")
                else:
                    grid[row + 2][col + 1] = "🚔"
                    grid[row][col] = unoccupied
                    row += 1
                    col -= 1
                if unoccupied == 8 and dupli_grid[row+1][col+1] != 9 and dupli_grid[row+1][col+2] != 9 and dupli_grid[row+1][col+3] != 0:
                    raise ValueError("Invalid Move")
                else:
                    grid[row+1][col+3] = "🚔"
                    grid[row][col] = unoccupied
                    row += 1
                    col += 3
        count += 1
        if count > 100:
            sys.exit("That's enough")
        game_running = True

path = make_ways('second_pathways.txt')
move(path)
#map
"""
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
7 4 2 5 3 2 8 8 9 9 7 6 3 2 5 4 2 8 9
6 7 2 5 3 2 8 8 9 9 7 6 3 2 5 4 2 8 9  
0 0 0 0 0 0 8 8 9 9 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 8 8 9 9 1 1 1 1 1 1 1 1 1
8 9 2 5 3 2 8 8 9 9 7 6 3 2 5 4 2 8 9
8 9 2 5 3 2 8 8 9 9 7 6 3 2 5 4 2 8 9
0 0 0 0 0 0 8 8 9 9 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 8 8 9 9 1 1 1 1 1 1 1 1 1
  
"""
