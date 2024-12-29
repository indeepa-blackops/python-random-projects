import random

lower_bound = 1
upper_bound = 100
max_attempts = 10

secret_number = random.randint(lower_bound,upper_bound)

def get_guess():
    while True:
        try:
            guess = int(input(f"Enter your guess between {lower_bound} and {upper_bound} : "))
            if lower_bound<= guess<= upper_bound:
                return guess
            else:
                print("Invalid number, try agian")
        except ValueError:
            print("Invalid Input, check and try again.")

def check_guess(guess,secret_number):
    if guess == secret_number:
        return "correct"
    elif guess <= secret_number:
        return "too low"
    else:
        return "too high"

def play_game():
    attempts = 0
    won =False

    while attempts < max_attempts:
        attempts+=1
        guess = get_guess()
        result = check_guess(guess,secret_number)

        if result == "correct":
            print(f"congrats, you guessed the secret number {secret_number} in {attempts} attempts")
            won =True
            break
        else:
            print(f"{result}, Try again!")
    if not won:
        print(f"sorry , you ran out of attempts! The secret number is {secret_number}.")

if __name__ == "__main__":
    print("Welcome to the guessing game, be ready with your numbers")
    play_game()