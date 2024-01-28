def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    
def instructions():
    print("The grid is 1-9, from left to right with 1-3 as the bottom row")
    print("When indicated to do so, put a number between 1-9")
    print("Type ""stop"" at any point to stop")
    

def won(player, theBoard):
    printBoard(theBoard)
    print("\nGame Over.\n")
    print(f"!!!! {player} won !!!!".upper())
    
def game():
    
    theBoard = {"7": "⁷", "8": "⁸", "9": "⁹",
            "4": "⁴", "5": "⁵", "6": "⁶",
            "1": "¹", "2": "²", "3": "³",
}


    Board_keys = []

    for key in theBoard.keys():
        Board_keys.append(key)
    
    player = "X"
    count = 0
    
    for turn in range(10):
        printBoard(theBoard)
        print(f"It's your turn {player}. Where do you want to go?")
        
        move = input().upper()
        
        if move == "STOP":
            break
        
        if move.isdigit():
            if theBoard[move] != "X" or "O":
                theBoard[move] = player
                count += 1
            else:
                print("The place is already filled. Choose again")
                continue
        else:
            continue
        
        if count >= 5:
            if theBoard["7"] == theBoard["8"] == theBoard["9"]:
                won(player, theBoard)
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"]:
                won(player, theBoard)
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"]:
                won(player, theBoard)
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"]:
                won(player, theBoard)
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"]:
                won(player, theBoard)
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"]:
                won(player, theBoard)
                break
            elif theBoard["1"] == theBoard["5"] == theBoard["9"]:
                won(player, theBoard)
                break
            elif theBoard["7"] == theBoard["5"] == theBoard["3"]:
                won(player, theBoard)
                break
            
        if count == 9:
            printBoard(theBoard)
            print("\nGame Over.\n")
            print("It is a tie :( ")
            break
            
        if player == "X":
            player = "*"
        else:
            player = "X"
        
    restart = input("Do you want to play again? (Y/N) ").upper()
    
    if restart == "Y":
        game()

if __name__ == "__main__":
    instructions()
    game()
            
                