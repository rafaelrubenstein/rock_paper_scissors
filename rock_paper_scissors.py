import random

user_wins = 0
computer_wins = 0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbols = [rock, paper, scissors]
while user_wins < 3 and computer_wins < 3:
    users_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors\n"))
    while users_choice > 2:
        users_choice = int(input("Choose 0 for Rock, 1 for Paper, or 2 for Scissors. number entered "
                                 "must be less than 3\n"))
    computer_choice = random.randint(0, 2)
    user_move = symbols[users_choice]
    computer_move = symbols[computer_choice]
    if users_choice == computer_choice:
        print(user_move)
        print(computer_move)
        print("Its a draw")
    elif users_choice == 0 and computer_choice == 2:
        print(user_move)
        print(computer_move)
        print("You win")
        user_wins += 1
    elif users_choice == 1 and computer_choice == 0:
        print(user_move)
        print(computer_move)
        print("You win")
        user_wins += 1
    elif users_choice == 2 and computer_choice == 1:
        print(user_move)
        print(computer_move)
        print("You win")
        user_wins += 1
    else:
        print(user_move)
        print(computer_move)
        print("You lose")
        computer_wins += 1
else:
    print(f"You won {user_wins} time the computer won {computer_wins} times.\nIf you have 3 wins you won!"
          f" otherwise, better luck next time")
