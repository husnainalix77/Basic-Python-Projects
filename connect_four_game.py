## Connect Four Game (Human vs AI) — Fully Intelligent AI
import random
import time
import os
import platform

def dispGrid(grid):
    'Displays the grid in Unicode format'
    cols = len(grid[0])
    rows = len(grid)
    print()
    print('╔' + '═══╦' * (cols - 1) + '═══╗')   
    for r_index, row in enumerate(grid):
        print('║' + '║'.join(f' {cell} ' for cell in row) + '║')
        if r_index < rows - 1:
            print('╠' + '═══╬' * (cols - 1) + '═══╣')
        else:
            print('╚' + '═══╩' * (cols - 1) + '═══╝')
    print('  ' + '   '.join(str(c) for c in range(cols)))
    print()
    
def clearScreen():
    'Clears the screen'
    current_system = platform.system()
    if current_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
        
def updateDisplay(grid):
    'Updates display after each valid move'
    time.sleep(0.3)
    clearScreen()
    dispGrid(grid)
                 
def getColumn(grid, col_num):
    'Returns a column of elements in grid'
    return [row[col_num] for row in grid] 
   
def isValidMove(grid, c, mark):
    'Checks validation of move and places mark'
    n = len(grid)-1
    col = getColumn(grid, c)
    for r, data in enumerate(col[::-1]):
        if data =='-':
            grid[n-r][c] = mark
            return True
    return False 

def getCriticalMove(grid, mark):
    'Returns a column where mark can win immediately, else None'
    rows = len(grid)-1
    cols = len(grid[0])
    for col_num in range(cols):
        col = getColumn(grid, col_num)
        if '-' not in col:
            continue
        row_idx = rows - col[::-1].index('-')
        grid[row_idx][col_num] = mark       
        if checkWin(grid, mark):
            grid[row_idx][col_num] = '-'            
            return col_num
        grid[row_idx][col_num] = '-'          
    return None  

def getValidColumn(grid):
    'Returns a random valid column'
    cols = len(grid[0])
    while True:
        c = random.randint(0, cols-1)
        if '-' in getColumn(grid, c):
            return c

def getBestMove(grid, mark, opponent_mark):
    'Makes AI move strategically'
    cols = len(grid[0])
    center = cols // 2
    col_order = [center] + [center + i for i in range(1, center+1)] + [center - i for i in range(1, center+1)]
    win_col = getCriticalMove(grid, mark)
    ## Immediate Win for AI
    if win_col is not None:
        return win_col
    ## Block immediate Win for Human
    block_col = getCriticalMove(grid, opponent_mark)
    if block_col is not None:
        return block_col
    ## Prefer Center columns
    for col_num in col_order:
        if '-' in getColumn(grid, col_num):
            return col_num
    return None  

def checkWin(grid, mark):
    'Checks winning Possibility'
    ## Vertical Win
    for col_num in range(len(grid[0])):
        col = getColumn(grid, col_num)
        for i in range(len(col)-3):
            if all(cell == mark for cell in col[i : i+4]):
                return True
    ## Horizontal Win        
    for row in grid:
        for j in range(len(row)-3):
            if all(cell == mark for cell in row[j : j+4]):
                return True
    ## Diagonals win        
    rows, cols = len(grid), len(grid[0])
    ## \ Diagonals
    for r in range(rows - 3):
        for c in range(cols - 3):
            if all(grid[r+i][c+i] == mark for i in range(4)):
                return True
    ## / Diagonals        
    for r in range(3, rows):
        for c in range(cols - 3):
            if all(grid[r-i][c+i] == mark for i in range(4)):
                return True
    return False 
       
def hasEmptySlot(grid):
    'Checks if any empty slot is left or not' 
    for col_num in range(len(grid[0])):
        col = getColumn(grid, col_num)
        if '-' in col:
            return True
    return False      

def playGame(rows, cols): 
    'Full Playable game with fully intelligent AI'
    grid = [['-' for _ in range(cols)] for _ in range(rows)]
    players = [('Player 1','R'), ('Player 2','Y')]
    print('Player 2(Y) is computer.')    
    dispGrid(grid)
    while True:
        choice = input('Enter F to take 1st chance and S for 2nd chance: ').strip().lower()
        if choice not in ['f', 's']:
            print('Enter F or S only!')  
            continue
        break   
    turn = 0 if choice == 'f' else 1
    while True:
        current_player, mark = players[turn % 2]
        if turn % 2 == 0:  # Human turn
            while True:    
                try:
                    user_pick = int(input(f'{current_player}({mark}), choose a column (0-{cols-1}): '))           
                    if user_pick not in range(0, cols):
                        print(f'Enter 0-{cols-1} only!')
                        continue
                    break
                except ValueError:
                    print(f'Invalid input. Enter a number between 0-{cols-1}.')
                    continue  
            if isValidMove(grid, user_pick, mark):
                updateDisplay(grid)
                if checkWin(grid, mark):
                    print(f'{current_player}({mark}) won!')
                    print('Game is over.')
                    return
                if not hasEmptySlot(grid):
                    print('All columns are full. Game is over!')
                    return
            else:
                print(f'Invalid move. Column {user_pick} is filled now.') 
                continue
        else:  # AI turn
            computer_pick = getBestMove(grid, 'Y', 'R')
            if computer_pick is None:
                computer_pick = getValidColumn(grid)
            isValidMove(grid, computer_pick, mark)
            print(f"{current_player}({mark}) chooses column {computer_pick}.")    
            time.sleep(1.5)  
            updateDisplay(grid) 
            if checkWin(grid, mark):
                print(f'{current_player}({mark}) won!')
                print('Game is over.')
                return
            if not hasEmptySlot(grid):
                print('All columns are full. Game is over!')
                return
        turn = (turn + 1) % 2

if __name__=='__main__':  
    rows, cols = 6, 7
    while True:
        op = input('Do you want to play (Y/N): ').strip().lower()
        if op not in ['y', 'n']:
            print('Enter Y or N only!')
            continue
        if op == 'y':
            playGame(rows, cols)
            print("="*40)
        else:
            print('Ok, next time.')
            break