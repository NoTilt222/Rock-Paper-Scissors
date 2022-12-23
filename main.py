import random

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

decisions = [rock, paper, scissors]
length = len(decisions)
random_decision = random.randint(0, length - 1)
user_input = input("What are you going to choose? Type 0 for Rock, 1 for Paper and 2 for Scissors. \n")
user_choice = int(user_input[0])
print("You chose:")
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, you lose!")
else:
    print(decisions[user_choice])

    print("System chose:")
    print(decisions[random_decision])

    if random_decision == user_choice:
        print("It's a draw!")
    elif random_decision == 0 and user_choice == 1:
        print("You won!")
    elif random_decision == 0 and user_choice == 2:
        print("You lose!")
    elif random_decision == 1 and user_choice == 0:
        print("You lose!")
    elif random_decision == 1 and user_choice == 2:
        print("You won!")
    elif random_decision == 2 and user_choice == 0:
        print("You won!")
    elif random_decision == 2 and user_choice == 1:
        print("You lose!")
