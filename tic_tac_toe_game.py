## Tic Tac Toe Game
import os
import time

def dispGrid(grid): 
    'Dsiplays grid in nice format'
    ## Unicode box Drawing
    time.sleep(0.2)
    os.system('cls')
    print("╔═══╦═══╦═══╗")
    for i, row in enumerate(grid):
        print("║ " + " ║ ".join(str(x) for x in row) + " ║")
        if i < 2:
            print("╠═══╬═══╬═══╣")
    print("╚═══╩═══╩═══╝")

def fillSlot(grid, mark, slot):
    'Fills slot with player respective symbol'
    col = (slot-1) % 3 
    row = (slot-1) // 3
    if grid[row][col] not in range(1, 10):
        return False
    grid[row][col] = mark
    return True  

def isWinner(grid):
    'Checks winning possibility between two players'
    return (
        grid[0][0] == grid[0][1] == grid[0][2] or  # Row 1
        grid[1][0] == grid[1][1] == grid[1][2] or  # Row 2
        grid[2][0] == grid[2][1] == grid[2][2] or  # Row 3
        grid[0][0] == grid[1][0] == grid[2][0] or  # Col 1
        grid[0][1] == grid[1][1] == grid[2][1] or  # Col 2
        grid[0][2] == grid[1][2] == grid[2][2] or  # Col 3
        grid[0][0] == grid[1][1] == grid[2][2] or  # Diagonal 1
        grid[0][2] == grid[1][1] == grid[2][0]     # Diagonal 2
    )

## Main Program 
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# dispGrid(grid)
blanks = 9
mark1 = input("Enter Player 1's mark (e.g., X or O): ").strip()
mark2 = input("Enter Player 2's mark (different from Player 1): ").strip()

turn ='P1'
dispGrid(grid)
while True:
    if turn == 'P1':
        while True:
            print('Player 1 turn')
            slot = int(input('Enter slot to fill: '))
            if slot not in range(1, 10):
                print('Please enter 1-9 only!')
                continue 
            break       
        if fillSlot(grid, mark1, slot):
            blanks -= 1 
            dispGrid(grid)
        else:
            print('Slot is already filled!') 
        if isWinner(grid):
            print('Player 1 won') 
            break   
        if blanks == 0:
            print('All slots are filled')
            break    
        turn = 'P2'    
        
    elif turn == 'P2':
        while True:
            print('Player 2 turn')
            slot = int(input('Enter slot to fill: '))
            if slot not in range(1, 10):
                print('Please enter 1-9 only!')
                continue   
            break     
        if fillSlot(grid, mark2, slot):
            dispGrid(grid)
            blanks -= 1
        else:
            print('Slot is already filled!')
        if isWinner(grid):
            print('Player 2 won')  
            break      
        if blanks == 0:
            print('All slots are filled now.')
            break     
        turn = 'P1' 
        
if not isWinner(grid):
    print('Game ended in draw.')                          
    