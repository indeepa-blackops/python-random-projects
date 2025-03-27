import random
print("You know the rules.")

while True:
    print('Your choices are as follows:\n'+'1- Rock\n'+'2- Paper\n'+'3- Scissors\n')
    choice = int(input("What is your choice: "))

    while choice > 3 or choice < 1:
        print('It seems like you have entered a wrong choice')
        choice = int(input('check again and enter a correct choice: '))

    if choice == 1:
        choice_name = 'rock'
    elif choice ==2:
        choice_name = 'paper'
    else:
        choice_name = 'scissors'

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice ==2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    if choice == comp_choice:
        result = 'draw'
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and choice == 1) :
        result = 'paper'
    elif (choice == 1 and choice == 3) or (choice ==3 and choice == 1):
        result = 'rock'
    else:
        result = 'scissors'

    if result == 'draw':
        print('This hand was a draw!')
    elif result == choice_name:
        print('Player won this round!')
    else:
        print('Computer won this round!')

    print('Ready for round two or quit.')
    quit_command = input('if you want to continue or quit\n'+'Y - continue to next round\n'+'N - quit now\n'+'choice: ')
    if quit_command.lower() == 'n':
        print('It is a pleasure to play with you!')
        break