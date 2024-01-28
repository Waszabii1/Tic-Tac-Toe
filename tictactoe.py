theBoard = {"7": "7", "8": "8", "9": "9",
            "4": "4", "5": "5", "6": "6",
            "1": "1", "2": "2", "3": "3",
}

Board_keys = []

for key in theBoard:
    Board_keys.append(key)
    
def printBoard(board):
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    
def instructions():
    print("The grid is 1-9, from left to right with 1-3 as the bottom row")
    print("When indicated to do so, put a number between 1-9")
    

def won(player):
    printBoard(theBoard)
    print("\nGame Over.\n")
    print(f"!!!! {player} won !!!!".upper())
    
def game():
    
    player = "X"
    count = 0
    
    for turn in range(10):
        printBoard(theBoard)
        print(f"It's your turn {player}. Where do you want to go?")
        
        move = input()
        
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
                won(player)
                break
            elif theBoard["4"] == theBoard["5"] == theBoard["6"]:
                won(player)
                break
            elif theBoard["1"] == theBoard["2"] == theBoard["3"]:
                won(player)
                break
            elif theBoard["1"] == theBoard["4"] == theBoard["7"]:
                won(player)
                break
            elif theBoard["2"] == theBoard["5"] == theBoard["8"]:
                won(player)
                break
            elif theBoard["3"] == theBoard["6"] == theBoard["9"]:
                won(player)
                break
            elif theBoard["1"] == theBoard["5"] == theBoard["9"]:
                won(player)
                break
            elif theBoard["7"] == theBoard["5"] == theBoard["3"]:
                won(player)
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
        for key in Board_keys:
            theBoard[key] = " "
                
        game()

if __name__ == "__main__":
    instructions()
    game()
            
                