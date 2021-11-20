#Chp 3. Rock,Paper, Scissors

import random

item = ['rock', 'paper','scissors']
cpu_pick = random.choice(item)

user_input = ' '
while user_input != 'rock' and user_input != 'scissors' and user_input != 'paper':
    user_input = input("rock, paper, scissors? ")

if user_input == cpu_pick:
    print("We both chose", cpu_pick,"play again!")
elif user_input == 'paper' and cpu_pick == 'scissors':
    print("Computer wins, I chose",cpu_pick)
elif user_input == 'rock' and cpu_pick == 'paper':
    print("Computer wins, I chose", cpu_pick)
elif user_input == 'scissors' and cpu_pick == 'rock':
    print("Computer wins, I chose", cpu_pick)
else:
    print("User won, I chose", cpu_pick)
