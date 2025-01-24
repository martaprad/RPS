from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)

# Turn that random number into the computer's RPS move
computer_move = num
if computer_move == 1:
    computer_move = "rock"
elif computer_move == 2:
    computer_move = "paper"
elif computer_move == 3:
    computer_move = "scissors"

# Ask a user to enter their move
user_move = input("Enter your move: (rock, paper or scissors)").lower()
# We put lower() at the end in case the user introduces the string in upper case

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("YOUR MOVE: ")
if user_move == "rock":
    print(rock)
    print("COMPUTER MOVE: ")
    if computer_move == "rock":
        print(rock)
        print("It's a tie!")
    elif computer_move == "paper":
        print(paper)
        print("You lose! :(")
    else:
        print(scissors)
        print("You win! :)")
elif user_move == "paper":
    print(paper)
    print("COMPUTER MOVE: ")
    if computer_move == "rock":
        print(rock)
        print("You win! :)")
    elif computer_move == "paper":
        print(paper)
        print("It's a tie!")
    else:
        print(scissors)
        print("You lose! :(")
elif user_move == "scissors":
    print(scissors)
    print("COMPUTER MOVE: ")
    if computer_move == "rock":
        print(rock)
        print("You lose! :(")
    elif computer_move == "paper":
        print(paper)
        print("You win! :)")
    else:
        print(scissors)
        print("It's a tie!")
else:
    print("That's not a valid move!")
