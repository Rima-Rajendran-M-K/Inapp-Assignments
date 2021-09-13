from random import randint

choices = ["rock", "paper", "scissors"]
outcomes_and_points = {
  # 0 := draw, 1 := Player won, -1 := Computer won
  "rock-rock": 0,
  "rock-paper": 1,
  "rock-scissors": -1,
  "paper-rock": -1,
  "paper-paper": 0,
  "paper-scissors": 1,
  "scissors-rock": 1,
  "scissors-paper": -1,
  "scissors-scissors": 0
  }

history = {}
player_points = 0
computer_points = 0
d = 'y'

for round in range(1, 11):
    computer_choice = choices[randint(0, 2)]
    player_choice = input("\nChoose between rock, paper, scissors: ")
    outcome = computer_choice + "-" + player_choice

    if outcome in outcomes_and_points:
        print("Player choice: ", player_choice)
        print("Computer choice: ", computer_choice)

        if outcomes_and_points[outcome] == 0:
            print(f"Round %s is draw" % round)
            history[round] = [player_choice, computer_choice, 0]
          
        elif outcomes_and_points[outcome] == 1:
            print(f"Player won round %s" % round)
            player_points += 1
            history[round] = [player_choice, computer_choice, 1]

        elif outcomes_and_points[outcome] == -1:
            print(f"Computer won round %s" % round)
            computer_points += 1
            history[round] = [player_choice, computer_choice, -1]
    
print("\nPlayer: ", player_points)
print("Computer: ", computer_points)
if player_points > computer_points:
  print('Player wins!')
elif player_points == computer_points:
  print('Draw!')
else:
  print('Computer wins!')


while (d == 'y'):
  try:
    x = int(input('\nEnter the round for which you need the information: '))
    print('Player choice = {}'.format(history[x][0]))
    print('Computer choice = {}'.format(history[x][1]))
    if (history[x][2] == -1):
      print(f'Computer won Round %s' % x)
    elif (history[x][2] == 1):
      print(f'Player won Round %s' % x )
    else:
      print('Draw')
  except:
    print('Invalid input')
  d = input('\nDo you want to continue(y/n): ')