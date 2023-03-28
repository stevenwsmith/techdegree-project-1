"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

"""

import random
import time

def start_game():
    print("Hello, Gamer!")
    answer = random.randint(1,20)
    answer_not_solved = True
    guesses = 1
    while answer_not_solved:
        user_guess = int(input("Guess the number 1-20: "))
        if user_guess < answer:
            print(f"{user_guess} is too low!")
            guesses += 1
        elif user_guess > answer:
            print(f"{user_guess} is too high!")
            guesses += 1
        else:
            answer_not_solved = False
    print("\n----------------------------")
    print(f"You got it!!\n")
    if guesses == 1:
        print(f"It took you {guesses} attempt to guess the number {answer}.")
    else:
        print(f"It took you {guesses} attempts to guess the number {answer}.")
    keep_playing = input("Would you like to play again? [y/n]: ")
    if keep_playing == 'y':
        start_game()
    else:
        print("Shutting down")
        time.sleep(1)
        print("Shutting down.")
        time.sleep(1)
        print("Shutting down..")
        time.sleep(1)
        print("Shutting down...")
        time.sleep(1)
        print("Shutting down")
        time.sleep(1)
        print("Shutting down.")
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.



# Kick off the program by calling the start_game function.
start_game()