import random
import logger
import time

# sets up the grid with bombs
# n = size of grid, n x n
# k = number of bombs
def GenerateMineSweeperMap(n, k):
    #first, set up the grid
    arr = [[0 for row in range(n)] for column in range(n)]    
    
    #randomly place bombs
    for num in range(k):
        is_dupe = True
        while(is_dupe): #loop as long as it takes to get unique coords
            x = random.randint(0,n-1)
            y = random.randint(0,n-1)

            if(arr[y][x] != 'X' ): #if an X is already there, it's duplicate coords
                arr[y][x] = 'X'
                is_dupe = False    
        
        # the following wall of if-statements increments every neighboring non-bomb node by 1
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-1): 
            if arr[y][x+1] != 'X':
                arr[y][x+1] += 1 # center right        
            
        if (x >=1 and x <= n-1) and (y >= 0 and y <= n-1):
            if arr[y][x-1] != 'X':
                arr[y][x-1] += 1 # center left        
            
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x-1] != 'X':
                 arr[y-1][x-1] += 1 # top left
 
        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if arr[y-1][x+1] != 'X':
                arr[y-1][x+1] += 1 # top right        
        
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if arr[y-1][x] != 'X':
                arr[y-1][x] += 1 # top center
 
        if (x >=0 and x <= n-2) and (y >= 0 and y <= n-2):
            if arr[y+1][x+1] != 'X':
                arr[y+1][x+1] += 1 # bottom right        
        
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x-1] != 'X':
                arr[y+1][x-1] += 1 # bottom left        
        
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if arr[y+1][x] != 'X':
                arr[y+1][x] += 1 # bottom center    
    return arr

# Generates a blank map with all values covered up    
# n = size of grid, n x n        
def GeneratePlayerMap(n):
    arr = [['-' for row in range(n)] for column in range(n)]
    return arr

# Prints the current state of the board
def DisplayMap(map):
    for row in map:
        print(" ".join(str(cell) for cell in row))

# Win condition: number of "-"s == number of bombs
# k = number of bombs
def CheckWon(map, k):
    count = 0
    for row in map:
        for cell in row:
            if cell == '-':
                count= count + 1
    return count == k

# "play again" check
def CheckContinueGame():
    isContinue = input("Do you want to try again? (y/n)\n> ").lower()
    while(isContinue != 'y' and isContinue != 'n'):
        isContinue = input("Must input 'y' or 'n'\n> ").lower()
        
    if isContinue == 'n':
        return False
    return True

#validates input
def validate_x_y(input, n):
    try:
        int(input)
        if (int(input) > 0 and int(input) <= n):
            return True
        else:
            raise Exception
        
    except:
        return False

# our "main"
def run_game():
    score = 0
    GameStatus = True
    while GameStatus:

        difficulty = ""
        while (difficulty != 'b' and difficulty != 'i' and difficulty != 'e'):        
            difficulty = input("Select your difficulty: (b)eginner, (i)ntermediate, (e)xpert\n> ").lower()
            if difficulty.lower() == 'b':
                n = 5
                k = 3
            elif difficulty.lower() == 'i':
                n = 6
                k = 8
            elif difficulty.lower() == 'e':
                n = 8
                k = 12
            else:
                print("Please enter \"b\", \"i\", or \"e\".")
 
        #set up grid + timer
        minesweeper_map = GenerateMineSweeperMap(n, k)
        player_map = GeneratePlayerMap(n)   
        DisplayMap(player_map) 
        start_time = time.time() 

        while True:       
            
            if CheckWon(player_map, k) == False:                
                print("Enter the coords of the cell you want to open (top-left is 0, 0, bottom right is " + str(n) +", " + str(n) + ")")
                x = input("X (1 to " + str(n) + ") " + "> ")
                while(not validate_x_y(x, n)):
                    print("X must be greater than 0 and less than or equal to " + str(n) + ".")
                    x = input("X (1 to " + str(n) + ") " + "> ")
                
                y = input("Y (1 to " + str(n) + ") " + "> ")
                while(not validate_x_y(y, n)):
                    print("Y must be greater than 0 and less than or equal to " + str(n) + ".")
                    y = input("Y (1 to " + str(n) + ") " + "> ")

                x = int(x) - 1 # 0 based indexing
                y = int(y) - 1 # 0 based indexing                
                
                # lose condition
                if (minesweeper_map[y][x] == 'X'):                    
                    print("Game Over!")
                    print("Final score: " + str(score))
                    end_time = time.time()
                    logger.log("[Minesweeper] " + return_difficulty(difficulty) + "-difficulty game lost in " 
                               + logger.time_format(end_time - start_time) + " with score " + str(score) + "!")
                    DisplayMap(minesweeper_map)
                    GameStatus = CheckContinueGame()
                    break                
                
                else:                    
                    player_map[y][x] = minesweeper_map[y][x]
                    score = score + 1
                    DisplayMap(player_map)
 
            else:                
                print("You have Won!")
                print("Final score: " + str(score))
                end_time = time.time()
                logger.log("[Minesweeper] " + return_difficulty(difficulty) + "-difficulty game won in " 
                           + logger.time_format(end_time - start_time) + " with score " + str(score) + "!")
                GameStatus = CheckContinueGame()
                break

def return_difficulty(d):
    match d:
        case "b":
            return "Beginner"
        case "i":
            return "Intermediate"
        case e:
            return "Expert"