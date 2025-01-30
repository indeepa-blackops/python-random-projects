import  random
print("Welcome to the word guessing game!")
print("""Rules:
1. you can guess a character at once 
2. the program will show your character is located 
3. when you run out of wrong guesses you loose turns""")
print()
# name = input('Your name please: ')
# print('Hi there',name,'!')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)

print("Guess the characters")
guesses = ''
turn = 10

while turn > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('_')
            failed +=1

    if failed == 0:
        print('You win')
        print('The word is:',word)
        break

    print()
    guess = input('guess a character: ')
    guesses += guess
    if guess not in word:
        turn -+1
        print("Wrong")
        print("You have", + turn, 'more guesses')

        if turn == 0:
            print("You Loose")

# Buggy code
# Itrate uncontrolably and doesnt follow rules