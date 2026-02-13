import random

options = ("rock", "paper", "scissors")
player = None
running = True


while running:
    player = input("enter a choice (rock, paper, scissors): ").lower()
    if player not in options:
        print("must be rock,paper or scissors")
        continue
    
    computer = random.choice(options)
    if player == computer:
        print("draw")
        print(f"player = {player} and computer = {computer}")
    elif player == "rock" and computer == "paper":
        print("you loose")
        print(f"player = {player} and computer = {computer}")
    elif player == "paper" and computer == "scissors":
        print("you loose")
        print(f"player = {player} and computer = {computer}")
    elif player == "scissors" and computer == "rock":
        print("you loose")
        print(f"player = {player} and computer = {computer}")
    else:
        print(f"you win")
        print(f"player = {player} and computer = {computer}")
        
    continue_playing = input("do you want to continue playing y/n: ").lower()
    if continue_playing != "y":
        running = False
    
    else:
        continue
    print("bye thank you for playing")
        
