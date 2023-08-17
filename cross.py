#!usr/bin/python3
import sys
import random

def choosing(answer):
    """
    It is for mode choosing
    """
    game = None
    if answer == "1":
        game = "comp"
    if answer == "2":
        game = "oponent"
    return game

def icons(answer):
    """
    It is for icon choosing
    """
    if answer == "oponent":
        choose = input("First player, choose your icon: X or O: ")
        if choose.lower() == "x":
            player1, player2 = "X", "O"
        elif choose.lower() == "o":
            player1, player2 = "O", "X"
    else:
        player1, player2 = "X", "O"
    return player1,player2

def displayGrid(grid):
    """
    It is for grid displaying
    """
    print(" " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2])
    print("-----------")
    print(" " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2])
    print("-----------")
    print(" " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2])

def checkGrid(grid):
    """
    It is for checking combinations
    """
    #Checking the first row
    if grid[0][0]=="X" and grid[0][1]=="X" and grid[0][2]=="X":
        print("Three Xs in a row.")
        sys.exit()
    elif grid[0][0]=="O" and grid[0][1]=="O" and grid[0][2]=="O":
        print("Three Os in a row.")
        sys.exit()
    #Checking the second row
    if grid[1][0]=="X" and grid[1][1]=="X" and grid[1][2]=="X":
        print("Three Xs in a row.")
        sys.exit()
    elif grid[1][0]=="O" and grid[1][1]=="O" and grid[1][2]=="O":
        print("Three Os in a row.")
        sys.exit()
    #Checking the third row
    if grid[2][0]=="X" and grid[2][1]=="X" and grid[2][2]=="X":
        print("Three Xs in a row.")
        sys.exit()
    elif grid[2][0]=="O" and grid[2][1]=="O" and grid[2][2]=="O":
        print("Three Os in a row.")
        sys.exit()
    #Checking the first column
    if grid[0][0]=="X" and grid[1][0]=="X" and grid[2][0]=="X":
        print("Three Xs in a column.")
        sys.exit()
    elif grid[0][0]=="O" and grid[1][0]=="O" and grid[2][0]=="O":
        print("Three Os in a column.")
        sys.exit()
    #Checking the second column
    if grid[0][1]=="X" and grid[1][1]=="X" and grid[2][1]=="X":
        print("Three Xs in a column.")
        sys.exit()
    elif grid[0][1]=="O" and grid[1][1]=="O" and grid[2][1]=="O":
        print("Three Os in a column.")
        sys.exit()
    #Checking the third column
    if grid[0][2]=="X" and grid[1][2]=="X" and grid[2][2]=="X":
        print("Three Xs in a column.")
        sys.exit()
    elif grid[0][2]=="O" and grid[1][2]=="O" and grid[2][2]=="O":
        print("Three Os in a column.")
        sys.exit()
    #Checking the first diagonale
    if grid[0][0]=="X" and grid[1][1]=="X" and grid[2][2]=="X":
        print("Three Xs in a diagonale.")
        sys.exit()
    elif grid[0][0]=="O" and grid[1][1]=="O" and grid[2][2]=="O":
        print("Three Os in a diagonale.")
        sys.exit()
    #Checking the second diagonale
    if grid[0][2]=="X" and grid[1][1]=="X" and grid[2][0]=="X":
        print("Three Xs in a diagonale.")
        sys.exit()
    elif grid[0][2]=="O" and grid[1][1]=="O" and grid[2][0]=="O":
        print("Three Os in a diagonale.")
        sys.exit()

def game(grid,answer,icon1,icon2):
    """
    It is the main code of the game
    """
    if answer == "oponent":
        for i in range(0,9):
            if i%2==0:
                print("Player %s: Your Turn!" %icon1)
                row = int(input("Enter the row index: 1 , 2 or 3: "))
                col = int(input("Enter the col index: 1 , 2 or 3: "))
                while grid[row-1][col-1]!=" ":
                    print("Sorry this cell is already taken... Try again!")
                    row = int(input("Enter the row index: 1 , 2 or 3: "))
                    col = int(input("Enter the col index: 1 , 2 or 3: "))
                grid[row-1][col-1] = icon1
                displayGrid(grid)
                checkGrid(grid)
            else:
                print("Player %s: Your Turn!" %icon2)
                row = int(input("Enter the row index: 1 , 2 or 3: "))
                col = int(input("Enter the col index: 1 , 2 or 3: "))
                while grid[row-1][col-1]!=" ":
                    print("Sorry this cell is already taken... Try again!")
                    row = int(input("Enter the row index: 1 , 2 or 3: "))
                    col = int(input("Enter the col index: 1 , 2 or 3: "))
                grid[row-1][col-1] = icon2
                displayGrid(grid)
                checkGrid(grid)
    else:
        for i in range(0,9):
            if i%2==0:
                print("Player: Your Turn!")
                row = int(input("Enter the row index: 1 , 2 or 3: "))
                col = int(input("Enter the col index: 1 , 2 or 3: "))
                while grid[row-1][col-1]!=" ":
                    print("Sorry this cell is already taken... Try again!")
                    row = int(input("Enter the row index: 1 , 2 or 3: "))
                    col = int(input("Enter the col index: 1 , 2 or 3: "))
                grid[row-1][col-1] = icon1
                displayGrid(grid)
                checkGrid(grid)
            else:
                print("Computor's Turn!")
                row = random.randint(0,2)
                col = random.randint(0,2)
                while grid[row][col]!=" ":
                    row = random.randint(0,2)
                    col = random.randint(0,2)
                grid[row][col] = icon2
                displayGrid(grid)
                checkGrid(grid)

def main():
    board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    criteria = input("""Please enter the criteria of gaming:
                            1. Computer
                            2. Oponent
                    """)
    conclusion = choosing(criteria)
    if conclusion == False:
        exit()
    p1,p2 = icons(conclusion)
    displayGrid(board)
    game(board,conclusion,p1,p2)
main()
