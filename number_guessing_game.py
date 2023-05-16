#number guessing game
import random

def guess_number():
    python_number = random.randint(1, 100) # generate random number between 1, 100
    attempts = 0

    print("Welcome to guess Pythons number!")
    
    while True:
        user_guess = int(input("Guess the number Python chose (between 1 and 100) Enter guess: ")) #user inputs guess int() converts string to interger
        attempts += 1 #short for attempts = attempts + 1 increase by 1 each guess

    
        if user_guess < python_number:
            print("Your guess is lower than Pythons number! Try again.")
        elif user_guess > python_number:
            print("Your guess is higher than Pythons number! Try again.")
        else:
            print(f"Well done! you guessed {user_guess} and pythons number was {python_number}. You guessed in {attempts} attempts!")
            break
guess_number()