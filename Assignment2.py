from random import randint

def printboard(bo):
    print(bo[7]+'|'+bo[8]+'|'+bo[9])
    print('-|-|-')
    print(bo[4]+'|'+bo[5]+'|'+bo[6])
    print('-|-|-')
    print(bo[1]+'|'+bo[2]+'|'+bo[3])

def player_input():
    choice = ''
    player1 = 'X'
    player2 = 'O'
    while choice != 'X' and choice != 'O':
        choice = input('Player 1 select (X / O): ').upper()
        player1 = choice
    if player1 == 'X':
        player2 == 'O'
        return ('X','O')
    elif player1 == 'O':
        player2 == 'X'
        return ('O','X')
    
def place_marker(bo, choice, position):
    bo[position] = choice
    
def winner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or
            (bo[9] == le and bo[5] == le and bo[1] == le))

def player_position(bo):
    position = 0
    while position not in range(1,10) or not bo[position] == '':
        position = int(input('Choose next position: '))

def computer_move():
    return random.randint(0,8)

print('TIC TAC TOE!')
while True:
    Board = ['','','','','','','','','']
    player1_choice, computer_choice = player_input()
    round = 1
    while round < 10:
        printboard(Board)
        position = player_position(Board)
        player_marker(Board, player1_choice)
        if winner(Board, player1_choice):
            display_board(Board)
    round += 1
