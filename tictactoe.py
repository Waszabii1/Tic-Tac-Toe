def board(): #board creator
    theBoard = {"7": "⁷", "8": "⁸", "9": "⁹",
            "4": "⁴", "5": "⁵", "6": "⁶",
            "1": "¹", "2": "²", "3": "³",
}


    Board_keys = []

    for key in theBoard.keys():
        Board_keys.append(key)
    game(theBoard)

def printBoard(board): #function to print the board
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    
def instructions(): #instructions on how to play
    print("The grid is 1-9, from left to right with 1-3 as the bottom row")
    print("When indicated to do so, put a number between 1-9")
    print("Type ""stop"" at any point to stop")
    

def won(player, theBoard): #prints when player wins
    printBoard(theBoard)
    print("\nGame Over.\n")
    print(f"!!!! {player} won !!!!".upper())
    
def game(theBoard):

    player_1_symbol = str(input("Player 1 please choose your symbol: ")).upper()
    print(f"Player 1 your symbol is {player_1_symbol}")
    player_2_symbol = str(input("Player 2 please choose your symbol: ")).upper()
    print(f"Player 2 your symbol is {player_2_symbol}")
    player = player_1_symbol
    count = 0
    
    for turn in range(10): #turn counter
        printBoard(theBoard)
        print(f"It's your turn {player}. Where do you want to go?")
        
        move = input().upper()
        
        if move == "STOP": #stops the current game
            break
        
        if move.isdigit(): #replaces board tile with player symbol
            if theBoard[move] != player_1_symbol or player_2_symbol:
                theBoard[move] = player
                count += 1
            else:
                print("The place is already filled. Choose again")
                continue
        else:
            continue
        
        if count >= 5: #win conditions
            if (theBoard["7"] == theBoard["8"] == theBoard["9"] or 
                theBoard["4"] == theBoard["5"] == theBoard["6"] or 
                theBoard["1"] == theBoard["2"] == theBoard["3"] or 
                theBoard["1"] == theBoard["4"] == theBoard["7"] or 
                theBoard["2"] == theBoard["5"] == theBoard["8"] or 
                theBoard["3"] == theBoard["6"] == theBoard["9"] or 
                theBoard["1"] == theBoard["5"] == theBoard["9"] or 
                theBoard["7"] == theBoard["5"] == theBoard["3"]):
                won(player, theBoard)
                break
            
        if count == 9: #tie
            printBoard(theBoard)
            print("\nGame Over.\n")
            print("It is a tie :( ")
            break
            
        if player == player_1_symbol:
            player = player_2_symbol
        else:
            player = player_1_symbol
        
    restart = input("Do you want to play again? (Y/N) ").upper()
    
    if restart == "Y": #restart
        board()
        

if __name__ == "__main__":
    instructions()
    board()
    
            
                