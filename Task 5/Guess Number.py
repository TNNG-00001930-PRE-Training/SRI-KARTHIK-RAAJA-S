'''Guess the Number

1. The program should generate a random number within a specified range (e.g., 1-100).

2.The user should be prompted to guess the number.

3.After each guess, the program should provide feedback to the user if the guess is too high or too low.

4.The user should have a limited number of attempts (e.g., 7 or 10).

5.If the user guesses the correct number, the program should display a congratulatory message.

6. If the user runs out of attempts, the program should reveal the correct number and display a "better luck next time" message.

7. The program should allow the user to play again or exit after each game.'''


import random

def guess_the_number(min_num, max_num, max_attempts):
    secret_number = random.randint(min_num, max_num)
    print(f"\nGuess the number between {min_num} and {max_num}!")
    
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Provide a valid number.")
            continue

        attempts += 1

        if guess == secret_number:
            print("Congrats! You guessed the correct number!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    else:
        print(f"\nSorry, you've run out of attempts! The correct number was {secret_number}. Better luck next time!")

def play_again():
    return input("\nDo you wanna to play again? (yes/no): ").lower().strip() == 'yes'

def main():
    min_num = 1
    max_num = 100
    max_attempts = 10

    while True:
        guess_the_number(min_num, max_num, max_attempts)
        if not play_again():
            print("I think you are enjoying, better luck next time!")
            break

if __name__ == "__main__":
    main()
