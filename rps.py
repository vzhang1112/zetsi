#!/usr/bin/env python

"""Small program to simulate a game of rock paper scissors with input"""

import random 

def main(): 
    user_move = input("Input your move: ").lower()
    
    if user_move not in "rock paper scissors": 
        print("there must've been a typo")
        return 1

    randomizer = random.randint(0, 2)

    machine_move = ""

    # translate numbers to English: 
    if randomizer == 0: 
        machine_move += "rock"
    elif randomizer == 1: 
        machine_move += "paper"
    elif randomizer == 2: 
        machine_move += "scissors"
    else: 
        print("mistake with randomizer")
        return 1
    

    # algorithm for determining winner: 
    if machine_move == "rock": 
        if user_move == "scissors": 
            print(f"machine wins, {machine_move} beats {user_move}")
            return 0
        elif user_move == "paper":
            print(f"user wins, {user_move} beats {machine_move}")
            return 0
        else: 
            print("tie")
            return 0
    elif machine_move == "paper":
        if user_move == "scissors": 
            print(f"user wins, {user_move} beats {machine_move}")
            return 0
        elif user_move == "rock": 
            print(f"machine wins, {machine_move} beats {user_move}")
            return 0
        else: 
            print("tie")
            return 0
    else: 
        if user_move == "rock": 
            print(f"user wins, {user_move} beats {machine_move}")
            return 0
        elif user_move == "paper": 
            print(f"machine wins, {machine_move} beats {user_move}")
            return 0
        else: 
            print("tie")
            return 0



if __name__ == "__main__": 
    main()
