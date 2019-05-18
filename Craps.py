import random
import time

def roll_dice():
    """Roll two dice and return their face values as a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)

def display_dice(dice):
    """Display one roll of the two dice"""
    die1, die2 = dice
    print(f'Player rolled a {die1} and a {die2} giving a total of {sum(dice)}.')
    
die_values = roll_dice()
print("Rolling the Dice")
time.sleep(1)
display_dice(die_values)

sum_of_dice = sum(die_values)

if sum_of_dice in (7, 11):
    game_status = 'WON'
elif sum_of_dice in (2, 3, 12):
    game_status = 'LOSE'
else:
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print(f'Your point is {my_point}')

while game_status == 'CONTINUE':
    die_values = roll_dice()
    print("Rolling the Dice")
    time.sleep(1)
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    
    if sum_of_dice == my_point:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status = 'LOSE'


if game_status == 'WON':
    print("YOU WON!!!")
if game_status == 'LOSE':
    print("You Lose.")