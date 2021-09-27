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

lowest = int(input("Enter Lowest Number : -"))

upper = int(input("Enter Largest Number : -"))

rndmnmbr = random.randint(lower, upper)

