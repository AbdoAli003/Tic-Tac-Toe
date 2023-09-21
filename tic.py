from random import randrange
def draw_board(board):
    for i in range(3):
        for j in range(3):
            if j<2:
             print(board[i][j],"| ",sep=" ",end="")
            else:
             print(board[i][j],end="")
            
        print("\n",end="")    
        print("-"*11)
def comp_order():
    return str(randrange(1,10))
def Draw(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X" or board[i][j] == "O":
                count = count + 1
    if count == 9:
        return True
    else:
        return False
def Winner(board,sgn):
     count = 0
     for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == sgn:
            return True
        elif board[0][i] == board[1][i] == board[2][i] == sgn:
            return True
     if board[0][0] == board[1][1] == board[2][2] == sgn:
        return True
     elif board[0][2] == board[1][1] == board[2][0] == sgn:
        return True
     return False
    
def check_valid(num):
    if num.isdigit()==True and int(num) < 10 and int(num) > 0:
        return True
    else:
        return False
def horder(board,num):
    for i in range(3):
        for j in range(3):
            if num == board[i][j]:
                board[i][j]="O"
                return True
    return False
def morder(board,chosed):
    for i in range(3):
        for j in range(3):
            if chosed == board[i][j]:
                board[i][j]="X"
                return True
    return False

    
board = [['1','2','3'],['4','5','6'],['7','8','9']]
draw_board(board)
name = input("Enter your name : ")
print("Ok!",name,"The Computer will start first")
board[1][1]="X"
draw_board(board)
while True:
    num = input("Enter a valid number : ")
    while True:
            if check_valid(num)==False:
             num = input("Wrong Input..Please enter a valid number : ")
            elif check_valid(num) == True and horder(board,num)==True:
                horder(board,num)    
                draw_board(board)
                break
            else: num = input("Wrong Input..Please enter a valid number : ")
            
    if Winner(board,"O") == True:
            print(name,"Is The Winner !")
            break
    elif Draw(board) == True:
            print("Draw")
            break
    print("Computer's Turn ! ",end="\n")
    while True:
            chosed = comp_order()
            if morder(board,chosed) == True:
                morder(board,chosed)
                draw_board(board)
                break
            else:
                continue
    if Winner(board,"X") == True:
            print("Computer Is The Winner !")
            break
    elif Draw(board) == True:
            print("Draw")
            break
        
        
            
    
