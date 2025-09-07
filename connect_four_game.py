## Connect Four Game (Human vs Strong AI) — by Husnain Maroof
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
    current_system = platform.system()
    if current_system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def updateDisplay(grid):
    time.sleep(0.3)
    clearScreen()
    dispGrid(grid)

def getColumn(grid, col_num):
    return [row[col_num] for row in grid]

def isValidMove(grid, c, mark):
    n = len(grid)-1
    col = getColumn(grid, c)
    for r, data in enumerate(col[::-1]):
        if data == '-':
            grid[n-r][c] = mark
            return True
    return False

def checkWin(grid, mark):
    rows, cols = len(grid), len(grid[0])
    # Vertical
    for col in range(cols):
        column = getColumn(grid, col)
        for r in range(rows-3):
            if all(column[r+i] == mark for i in range(4)):
                return True
    # Horizontal
    for row in grid:
        for c in range(cols-3):
            if all(row[c+i] == mark for i in range(4)):
                return True
    # Diagonal \
    for r in range(rows-3):
        for c in range(cols-3):
            if all(grid[r+i][c+i] == mark for i in range(4)):
                return True
    # Diagonal /
    for r in range(3, rows):
        for c in range(cols-3):
            if all(grid[r-i][c+i] == mark for i in range(4)):
                return True
    return False

def hasEmptySlot(grid):
    for c in range(len(grid[0])):
        if '-' in getColumn(grid, c):
            return True
    return False

# ----- Strong but Simple AI -----
def getBestMoveSimple(grid, ai_mark='Y', human_mark='R'):
    cols = len(grid[0])
    # 1. Immediate win
    for col in range(cols):
        if '-' not in getColumn(grid, col):
            continue
        row = len(grid)-1 - getColumn(grid, col)[::-1].index('-')
        grid[row][col] = ai_mark
        if checkWin(grid, ai_mark):
            grid[row][col] = '-'
            return col
        grid[row][col] = '-'
    # 2. Block human win
    for col in range(cols):
        if '-' not in getColumn(grid, col):
            continue
        row = len(grid)-1 - getColumn(grid, col)[::-1].index('-')
        grid[row][col] = human_mark
        if checkWin(grid, human_mark):
            grid[row][col] = '-'
            return col
        grid[row][col] = '-'
    # 3. Center preference
    center = cols // 2
    if '-' in getColumn(grid, center):
        return center
    # 4. Left/Right from center
    for offset in range(1, cols//2 + 1):
        for col in [center - offset, center + offset]:
            if 0 <= col < cols and '-' in getColumn(grid, col):
                return col
    # 5. Fallback random
    valid_cols = [c for c in range(cols) if '-' in getColumn(grid, c)]
    return random.choice(valid_cols)

# ----- Game Loop -----
def playGame(rows, cols):
    grid = [['-' for _ in range(cols)] for _ in range(rows)]
    players = [('Player','R'), ('Computer','Y')]
    print('Computer(Y) is very strong AI.')
    dispGrid(grid)

    while True:
        choice = input('Enter F to take 1st chance and S for 2nd chance: ').strip().lower()
        if choice in ['f','s']:
            break
        print('Enter F or S only!')
    turn = 0 if choice == 'f' else 1

    while True:
        current_player, mark = players[turn % 2]
        if turn % 2 == 0:  # Human
            while True:
                try:
                    user_pick = int(input(f'{current_player}({mark}), choose a column (0-{cols-1}): '))
                    if user_pick not in range(cols):
                        print(f'Enter 0-{cols-1} only!')
                        continue
                    break
                except ValueError:
                    print(f'Invalid input. Enter a number between 0-{cols-1}.')
            if isValidMove(grid, user_pick, mark):
                updateDisplay(grid)
                if checkWin(grid, mark):
                    print(f'{current_player}({mark}) won!')
                    return
                if not hasEmptySlot(grid):
                    print('All columns are full. Game over!')
                    return
            else:
                print(f'Invalid move. Column {user_pick} is filled.')
                continue
        else:  # AI
            computer_pick = getBestMoveSimple(grid, 'Y', 'R')
            isValidMove(grid, computer_pick, mark)
            print(f"{current_player}({mark}) chooses column {computer_pick}.")
            time.sleep(1)
            updateDisplay(grid)
            if checkWin(grid, mark):
                print(f'{current_player}({mark}) won!')
                return
            if not hasEmptySlot(grid):
                print('All columns are full. Game over!')
                return
        turn = (turn + 1) % 2

if __name__=='__main__':
    rows, cols = 6, 7
    while True:
        op = input('Do you want to play (Y/N): ').strip().lower()
        if op not in ['y','n']:
            print('Enter Y or N only!')
            continue
        if op == 'y':
            playGame(rows, cols)
            print("="*40)
        else:
            print('Ok, next time.')
            break
