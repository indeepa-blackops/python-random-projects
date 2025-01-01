# expected to had a game where the win score determines the end
# in this version of the game players choose no of rounds they want to play
#they would roll and if got 1 the round of that player terminated and get a 0 scores for the round
#they would get a chance to either to continue or terminate the round in the beginning of each round
#the score of that round returns and add to toal score
#the winner is determined by the highest score at the end of the all rounds


import random

player_name1 = input("player 1 name: ")
player_name2 = input("player 2 name: ")
player_score1 = 0
player_score2 = 0
rounds = int(input("number of rounds you wanna have: "))

def roll():
    roll_score = 0
    while True:
        agree = input("Do you agree to roll the dice: (y/n) ")
        if agree.lower() != 'y':
            print("gottach terminating your turn. ")
            break
        else:
            number = random.randint(1,6)

        if number == 1:
            print("sorry, bad luck. you rolled a one")
            return 0
        else:
            print(f"You rolled a {number}")
            roll_score += number

    return roll_score




for i in range(rounds):
    print(f"Player 1 turn , {player_name1}")
    roll_score = roll()
    player_score1 += roll_score
    print(f"your current score is {player_score1}")  #have to upgrade to showing current score in the roll itself
    print(f"Player 2 turn , {player_name2}" )
    roll_score = roll()
    player_score2 += roll_score
    print(f"your current score is {player_score2}")

if player_score1 >= player_score2 :
    print(f"congrats {player_name1} , you won.")
    print(f"try again next time {player_name2}")
else:
    print(f"congrats {player_name2} , you won.")
    print(f"try again next time {player_name1}")





