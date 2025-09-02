## This code is written by Husnain Maroof, Machine Learning Engineer, on 2 Sep, 2025.
import random 
import os

def setUpGrid(n):
    'Initializes grid to all zeros'
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    return new_grid
    
def dispGrid(grid):
    'Displays the grid after each move'
    for row in grid:
        print(row)
        
def showCommands():
    'Shows commands to user'
    print('Commands are as follows :') 
    print("'W' or 'w' : Move Up")
    print("'S' or 's' : Move Down")
    print("'A' or 'a' : Move Left")
    print("'D' or 'd' : Move Right")
    
def updateDisplay(grid):
    'Clears the screen, shows commands and current grid'
    os.system('cls')
    showCommands()
    print()
    dispGrid(grid)
    print()    
            
def getColumn(grid, col_num):
    'Finds a column in the grid'
    col = [row[col_num] for row in grid ]
    return col
            
def compressRow(row):
    'Moves non-zero values to left'
    new_row = [n for n in row if n!=0]
    new_row += [0]*(len(row)-len(new_row))
    return new_row
     
def mergeRow(row):
    'Returns a merged row'
    for i in range(len(row)-1): 
        if row[i] == row[i+1] and row[i]!=0:
            row[i]+=row[i]
            row[i+1] = 0
    return row                              
                    
def moveUp(grid):
    'Moves tiles up with non-zero elements'
    n = len(grid)
    new_grid = [[0 for _ in range(n)] for _ in range(n)]
    for col_num in range(n):
        col = getColumn(grid, col_num)
        col = compressRow(col)
        col = mergeRow(col)
        col = compressRow(col)
        for row_num in range(n):
            new_grid[row_num][col_num] = col[row_num]
    return new_grid        

def moveDown(grid):
    'Moves tiles down with non-zero elements'
    n = len(grid)
    new_grid = setUpGrid(n)
    for col_num in range(n):
        col = getColumn(grid, col_num)
        col = col[::-1]
        col = compressRow(col)
        col = mergeRow(col)
        col = compressRow(col)
        col = col[::-1]
        for row_num in range(n):
            new_grid[row_num][col_num] = col[row_num]
    return new_grid

def moveLeft(grid):
    'Moves all tiles with non-zero elements to left'
    new_grid = []
    for row in grid:
        row = compressRow(row)
        row = mergeRow(row)
        row = compressRow(row)
        new_grid.append(row)
    return new_grid    
        
def moveRight(grid):
    'Moves all tiles with non-zero elements to right'
    new_grid = []
    for row in grid:  
        row = row [::-1]
        row = compressRow(row)
        row = mergeRow(row)
        row = compressRow(row)
        row = row [::-1]
        new_grid.append(row)
    return new_grid    
    
def addNewTile(grid):
    'Adds new tile after every valid move if empty cells are available'
    n = len(grid)
    empty_cells = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = 2
        
def checkWin(grid):
    'Checks winning possibility'
    for row in grid:
        if 2048 in row:
            return True
    return False

def checkGameOver(grid):
    'Checks game over status'
    n = len(grid)
    for row in grid:
        if 0 in row:
            return False
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] == grid[i][j+1] or grid[j][i] == grid[j+1][i]:
                return False
    return True

def playGame(n):
    'Plays full Game'
    grid = setUpGrid(n)
    empty_cells = [(i,j) for i in range(n) for j in range(n)]

    cell1 = random.choice(empty_cells)
    empty_cells.remove(cell1)
    cell2 = random.choice(empty_cells)

    grid[cell1[0]][cell1[1]] = 2
    grid[cell2[0]][cell2[1]] = 2
    updateDisplay(grid)
    while True:
        cmnd = input('Enter the command> ').strip().lower()
        if cmnd not in ['w', 's','a','d']:
            print('Enter a valid command!')
            continue
        old_grid = [row[:] for row in grid]
        
        if cmnd == 'a':
            grid = moveLeft(grid)
            if grid != old_grid:
                addNewTile(grid)

        elif cmnd == 'd':
            grid = moveRight(grid)
            if grid != old_grid:
                addNewTile(grid)
                
        elif cmnd == 'w':
            grid = moveUp(grid)
            if grid != old_grid:
                addNewTile(grid)           
       
        elif cmnd =='s':
            grid = moveDown(grid)
            if grid != old_grid:
                addNewTile(grid)

        if checkGameOver(grid):
            print('Grid is filled. No merge is left.')
            print('Game over')
            break 
             
        if checkWin(grid):
            print("You've reached 2048! Do you want to continue playing? (y/n)")
            if input().lower() == 'n':
                break
            
        updateDisplay(grid)
      
if __name__ == '__main__':  
    n=4
    playGame(n)