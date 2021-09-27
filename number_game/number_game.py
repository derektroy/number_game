"""
#
# File          :   number_game.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.0
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :   Random Number Guessing Game
#
"""
import random
# Input Lowest Number
lowest = int(input("Enter Lowest Number : "))

# Input Upper or Largest Number
upper = int(input("Enter Largest Number : "))

# Generate Random Number Between two Inputs
rx = random.randint(lowest, upper)
print("\n\tYou've only ",
       round(math.log(upper - lowest + 1, 2)),
      " chances to guess the integer!\n")

#Count of Guesses
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lowest + 1, 2):
    count += 1

    # taking guessing number as input
    guess = int(input("Guess a number:- "))

    # Condition testing
    if rx == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif rx > guess:
        print("You guessed too small!")
    elif rx < guess:
        print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lowest + 1, 2):
    print("\nThe number is %d" % rx)
    print("\tBetter Luck Next time!")
