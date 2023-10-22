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

"""
Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
"""
while True:
    import random
    game_choice = [rock,paper,scissors]
    choice = len([rock,paper,scissors])

    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
    print(f"Player chose : {player_choice}")
    img_player = print(game_choice[player_choice])

    computer_choice = random.randint(0,choice - 1)
    print(f"Computer chose :{computer_choice}")
    img_computer = print(game_choice[computer_choice])
    if player_choice >= 3 or player_choice < 0:
        print("Wrong inputed number")
    elif player_choice == 0 and computer_choice == 2:
        print("Player wins")
    elif computer_choice == 0 and player_choice == 2:
        print("Player wins")
    elif player_choice > computer_choice:
        print("Player wins")
    elif computer_choice > player_choice:
        print("Computer wins")
    elif player_choice == computer_choice:
        print("Draw")
