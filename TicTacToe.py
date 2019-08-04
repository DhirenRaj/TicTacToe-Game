# -*- coding: utf-8 -*-
import random

#Randomly choosing player1 or player2
def choose_first():
    val = random.randint(0,1)
    if val == '0':
        return 'Player2'
    else:
        return 'Player1'

# displaying the game board 
def display_board(board):
    for i in range(0,len(board)+1,3):
        if i+2<=len(board):
            print("   "'|'"   "'|'"   ")
            print(' {} ''|'' {} ''|'' {} '.format(board[i],board[i+1],board[i+2]))
            if i<=3:
                print("___"'|'"___"'|'"___")
                
#function to take player input 'X' or 'O'
def player_input():
    val= ''

    while val!='X' and val !='O': 
        try:
            val = input("Please pick a marker 'X' or 'O': ")
        except:
            print("Invalid Entry, Try Again")
    
    if val == 'X':
        return ('X','O')
    else:
        return ('O','X')
        
#function to place the player's mark in the selected position
def place_marker(board, marker, pos):
    board[pos-1]=marker

#Checking the win condition 
def win_check(board, mark):
    for i in range(0,len(board)+1,3):
        if i+2<=len(board):
            if board[i]==mark and board[i+1]==mark and mark==board[i+2]:
                return True
    for i in range(0,3):
        if board[i]==mark and mark==board[i+3] and board[i+6]==mark:
                return True
            
    if board[0]==mark and mark==board[4] and mark==board[8]:
        return True
    if board[2]==mark and mark==board[4] and mark==board[6]:
        return True
    else: 
        return False

# To check for free slots in the board
def space_check(board, position):
    if board[position-1]==" ":
        return True
    else: 
        return False

#To check if the board is full or not
def full_board_check(board):
    c=0
    for x in board:
        if x=='X'or x =='O':
            c=c+1
    if c==len(board):
        return True
    else:
        return False

#Letting the player choose his mark
def player_choice(board,pname):
    
    pos =0
    while pos not in range(1,10) or not space_check(board,pos):
        try:
            pos = int(input('In which position you wanna mark {} (1-9)?'.format(pname)))
        except:
            print("Postion not vacant, please choose any other position.")
    return pos

def replay():
    x = input("Press 'Y' for New Game or Press 'N' to Quit")
    if x=='Y':
        return True
    else:
        return False
    
##############################################################
        
print('Welcome to Tic Tac Toe game!')

p = True
while p:
    # Set the game board
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    p2=''
    p1=''
    S = choose_first()
    print(S + ' Gets to play first !!!!!!!')
    
    #Get the player input
    if S == 'Player1':
        p1,p2 = player_input()
    else:
        p2,p1 = player_input()
    
    while full_board_check(board)== False:
        #The game begins with player who was chosen first randomly
        if S  == 'Player1':
            pos = player_choice(board,S)
            place_marker(board,p1,pos)
            display_board(board)
            #print(board)
            #checking win conditioner 
            if win_check(board,p1) == True:
                display_board(board)
                print('Player 1 is the Winner!!!')
                break
            #checkong draw condition
            elif full_board_check(board) == True:
                display_board(board)
                print('Its a Tie, Everybody Wins!!!!')
                break
            #Giving turn to player2
            else:
                S = 'Player2'
                
        else:
            pos = player_choice(board,S)
            place_marker(board,p2,pos)
            display_board(board)
            #print(board)
            #checking win condition
            if win_check(board,p2) == True:
                display_board(board)
                print('Player 2 is the Winner!!!')
                break
            #checkong draw condition
            elif full_board_check(board) == True:
                display_board(board)
                print('Its a Tie, Everybody Wins!!!!')
                break
            #Giving turn to Palyer1
            else:
                S = 'Player1'

    p = replay()




