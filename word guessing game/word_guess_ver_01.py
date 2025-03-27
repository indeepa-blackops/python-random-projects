import  random
print("Welcome to the word guessing game!")
print("""Rules:
1. you can guess a character at once 
2. the program will show your character is located 
3. when you run out of wrong guesses you loose turns""")
print()
name = input('Your name please: ')
print('Hi there',name,'!')

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)


guesses = input("Enter a character to begin with: ")
turn = len(word) + 2

while turn > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=' ')
        else:
            print('_',end=' ')
            failed +=1

    if failed == 0:
        print()
        print('You win')
        print('The word is:',word)
        break

    print()
    guess = input('enter another character: ')
    guesses += guess
    if guess not in word:
        turn -=1
        print("Wrong")
        print("You have", + turn, 'more guesses')

        if turn == 0:
            print("You Loose")

