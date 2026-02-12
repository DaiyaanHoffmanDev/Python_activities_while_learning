#this activity is about making a random number guessing game
import random

guesses = 0
low = 1
high = 10
number_to_guess = random.randint(low, high)


while True:
    user_guess = input("Enter a number between 1 and 10: ")
    guesses = guesses + 1
    if not user_guess.isdigit():
        print("guess has to be a number")
        continue
    user_guess = int(user_guess)
        
    if user_guess == number_to_guess:
            print("you guessed correct",)
            break
    elif user_guess < 1 or user_guess > 10:
         print("number must be between 1 and 10")
    elif user_guess < number_to_guess:
        print("too low")
    elif user_guess > user_guess:
        print("too high")
    else:
        print("you guessed incorrect")
        
print(guesses)



