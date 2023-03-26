# Project One:- Guess the number

import random
# Creation of random number using random module.
computer_turn=random.randint(1,100)
# print(random_number)
player_turn=0
guesses=0
while computer_turn!=player_turn:
    guesses+=1
    player_turn=int(input("Enter the number guess:-\n"))
    if computer_turn==player_turn:
        print(f'Congratulations. You guess the number in {guesses} turn.')
    elif computer_turn<player_turn:
        print("Ooops! Your guess is wrong. Smaller number please.")
    elif computer_turn>player_turn:
        print("Ooops! Your guess is wrong. Bigger number please.")

# Writing the number of turn in the file.
with open("highest_score.txt", "r") as f:
    highest_score=int(f.read())

if guesses<highest_score:
    print("Yeah... You have break the highest score record.")
    with open("highest_score.txt", "w") as f:
        f.write(str(guesses))

print("Good Luck Buddy...!!!")