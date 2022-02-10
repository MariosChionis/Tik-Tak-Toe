from random import shuffle


def display_board(board):
    print("\t",board[0]+" ","|"+board[1]+" ","|"+board[2])
    print("\t","--------")
    print("\t",board[3]+" ","|"+board[4]+" ","|"+board[5])
    print("\t","--------")
    print("\t",board[6]+" ","|"+board[7]+" ","|"+board[8])
    


def symbol_choice():
    print("You will have to choose 1 or 2 and whoever picks the symbol picks character and starts first")
    ls1=["","$"]
    shuffle(ls1)
    pl1=-1
    pl2=-1
    while (pl1!=0 and pl1!=1) or (pl2!=0 and pl2!=1):
        pl1=int(input("Player 1 pick a number from 0 and 1: "))
        pl2=int(input("Player 2 pick a number from 0 and 1: "))

        if pl1!=0 and pl1!=1:
            print("Player 1 Wrong number.")
        if pl2!=0 and pl2!=1:
            print("Player 2 Wrong number.")
    if ls1[pl1]=="$":
        pl1=True
        pl2=False
        s1=input("Player 1 starts first.Pick your symbol, X or O: ")
        if s1=="X":
            s2="O"
        else:
            s2="X"
    elif ls1[pl2]=="$":
        pl2=True
        pl1=False
        s2=input("Player 2 starts first.Pick your symbol, X or O: ") 
        if s2=="X":
            s1="O"
        else:
            s1="O"
    return s1,pl1,s2,pl2

def player_one_choice():
    position=-1
    while position not in range(9):
        position=int(input("Select position for your symbol (0-8): "))
    return int(position)

def player_two_choice():
    position=-1
    while position not in range(9):
        position=int(input("Select position for your symbol (0-8): "))
    return int(position)

def vertical_win(board):
    if board[0]=="X" and board[3]=="X" and board[6]=="X":
        return True,"X"
    elif board[1]=="X" and board[4]=="X" and board[7]=="X":
        return True,"X"
    elif board[2]=="X" and board[5]=="X" and board[8]=="X":
        return True,"X"
    elif board[0]=="O" and board[3]=="O" and board[6]=="O":
        return True,"O"
    elif board[1]=="O" and board[4]=="O" and board[7]=="O":
        return True,"O"
    elif board[2]=="O" and board[5]=="O" and board[8]=="O":
        return True,"O"
    else:
        return False,""


def horizontal_win(board):
    if board[0]=="X" and board[1]=="X" and board[2]=="X":
        return True,"X"
    elif board[3]=="X" and board[4]=="X" and board[5]=="X":
        return True,"X"
    elif board[6]=="X" and board[7]=="X" and board[8]=="X":
        return True,"X"
    elif board[0]=="O" and board[1]=="O" and board[2]=="O":
        return True,"O"
    elif board[3]=="O" and board[4]=="O" and board[5]=="O":
        return True,"O"
    elif board[6]=="O" and board[7]=="O" and board[8]=="O":
        return True,"O"
    else:
        return False,""

def diagonal_win(board):
    if board[0]=="X" and board[4]=="X" and board[8]=="X":
        return True,"X"
    elif board[2]=="X" and board[4]=="X" and board[6]=="X":
        return True,"X"
    elif board[0]=="O" and board[4]=="O" and board[8]=="O":
        return True,"O"
    elif board[2]=="O" and board[4]=="O" and board[6]=="O":
        return True,"O"
    else:
        return False,""
    
def win_type(board):
    diag_win,symbol1=diagonal_win(board)
    hor_win,symbol2=horizontal_win(board)
    ver_win,symbol3=vertical_win(board)
    if diag_win==True:
        if symbol1=="X":
            return "X"
        elif symbol1=="O":
            return "O"
    elif hor_win==True:
        if symbol2=="X":
            return "X"
        elif symbol2=="O":
            return "O"
    elif ver_win==True:
        if symbol3=="X":
            return "X"
        elif symbol3=="O":
            return "O"
    else:
        return ""

    






print("Welcome to Tic Tak Toe")
pl1_symbol,s1,pl2_symbol,s2=symbol_choice()
game_on="WRONG"
while game_on!="S" and game_on!="s":
    board=["" for i in range(10)]
    display_board(board)
    print("The board is ordered like this: 0-1-2 the upper row, 3-5-6 the middle row, 6-7-8 the lower row ")
    boardfilled=False
    win=""
    while boardfilled==False and win=="":
        if s1==True:
            board[player_one_choice()]=pl1_symbol
            display_board(board)
            win=win_type(board)
            if win!=pl1_symbol:
                board[player_two_choice()]=pl2_symbol
                display_board(board)
            win=win_type(board)
        elif s2==True:
            board[player_two_choice()]=pl2_symbol
            display_board(board)
            win=win_type(board)
            if win!=pl2_symbol:
                board[player_one_choice()]=pl1_symbol
                display_board(board)
            win=win_type(board)
        if win==pl1_symbol:
            print("Player 1 won!")
        elif win==pl2_symbol:
            print("Player 2 won!")
        if "" not in board:
            boardfilled=True
            print("There is no winner: Draw")
    game_on=input("If you want to play again press any button.If you want to stop playing press 'S' or 's':  ")
print("game is over")

    
    

    
