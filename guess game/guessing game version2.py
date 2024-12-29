import random
welcome = """Welcome to Guess the Number!!!!
in this game you have to guess the random number selected by computer and 
you will have the chance to select the range between numbers and the less guesses take to 
guess the number will win the game."""
min_bound= int(input("enter the lowest value you would guess: "))
max_bound =int(input("enter the highest value you would guess: "))
secret_number = random.randint(min_bound,max_bound)
guess = int(input("what would be your guess: "))

guesses = 1
while guess != secret_number:
    guesses +=1
    if guess < secret_number:
        print("too low bro, guess higher!")
    else:
        print("too high bro, guess low!")
    guess = int(input("try again , would ya? "))

print(f"see all it took was {guesses} guesses and the secret number is {secret_number}.")