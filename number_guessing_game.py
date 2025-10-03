# The program picks a random number between 1-100,
# and you have 7 attempts to guess it.
# Get hints if you’re too high,or too low 

import random # to genrate random number
secret_nber=random.randint(1,100)
attempts=7
print("Welcome to the number guessing game!")
print("Try to guess the number I am thinking about, it is between 1 and 100")
print(f"You have {attempts} attempts to guess it right")

guess_list = []
for i in range(attempts):
    guess = int(input("What is your guess? "))
    guess_list.append(guess)
    if guess < secret_nber:
        print("No, my secret number is higher")
    elif guess > secret_nber:
        print("No, my secret number is lower")
    else:
        print(f"Congrats! My secret number is indeed {secret_nber}")
        break
else:
    print(f"Game over, you did not guess my secret number after {attempts} attempts")
    print(f"My secret number was {secret_nber}")
    print(f"Your guesses were : {guess_list}")
    
