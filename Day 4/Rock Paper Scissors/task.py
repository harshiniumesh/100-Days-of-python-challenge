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
import random
user_choice = int(input("what do you choose? type o for Rock, 1 for Paper or 2 for Scissors"))
computer_choice = random.randint(0, 2)
print(f"computer_chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("you win!")
elif computer_choice > user_choice:
    print ("you lose!")
elif computer_choice == user_choice:
    print("its a draw!")