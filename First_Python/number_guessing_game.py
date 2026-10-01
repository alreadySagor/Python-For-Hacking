import random
print("Welcome to the Number Guessing Game")
print("-----------------------------------")
number = random.randint(1, 10)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 10 : "))
    print("-----------------------------------")
    attempts += 1
    if guess == number:
        print("-------------------------------------------------------------------")
        print(f"Congrates your guess is right , you guessed it in {attempts} times")
        print("-------------------------------------------------------------------")
        break
    elif guess < number:
        print("Too low, try again")
        print("------------------")
    else:
        print("Too high, try again")
        print("-------------------")