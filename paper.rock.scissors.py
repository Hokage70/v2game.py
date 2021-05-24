import random


random_number = random.randint(1, 3)
if random_number == 1:
    answer = 'rock'
elif random_number == 2:
    answer = 'paper'
elif random_number == 3:
    answer = 'scissors'
player_choice = input('Pick either rock, paper, or  scissors: ')
if player_choice == 'rock':
    print(answer)
elif player_choice == 'paper':
    print(answer)
elif player_choice == 'scissors':
    print(answer)
else:
    print('Sorry that is not a choice.')
