#Mariana Baker, Assignment 3.2, 11/7/26
#Changes made to the cho-han dice game.
"""
Cho-Han dice game
Original program by Al Sweigart.

Module 3 assignment changes:
1. Changed both input prompts to "MB:".
2. Changed the house fee from 10% to 12%.
3. Added an introduction notice explaining the 10 mon bonus for totals of 2 or 7.
4. Added bonus logic after revealing the dice: display the roll total and bonus,
   then add 10 mon to the player's purse when the total is 2 or 7.
"""

import random
import sys

JAPANESE_NUMBERS = {
    1: "ICHI", 2: "NI", 3: "SAN",
    4: "SHI", 5: "GO", 6: "ROKU"
}

print("""Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS: If the total of the dice roll is 2 or 7, you receive a 10 mon bonus.
""")

purse = 5000

while True:  # Main game loop.
    print("You have", purse, "mon. How much do you bet? (or QUIT)")

    # Keep asking until the player enters a valid bet or quits.
    while True:
        pot = input("MB: ")
        if pot.upper() == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > purse:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            break

    # Roll two six-sided dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    print("The dealer swirls the cup and you hear the rattle of dice.")
    print("The dealer slams the cup on the floor, still covering the")
    print("dice and asks for your bet.")
    print()
    print("    CHO (even) or HAN (odd)?")

    # Keep asking until the player chooses CHO or HAN.
    while True:
        bet = input("MB: ").upper()
        if bet != "CHO" and bet != "HAN":
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    # Reveal the dice.
    print("The dealer lifts the cup to reveal:")
    print("  ", JAPANESE_NUMBERS[dice1], "-", JAPANESE_NUMBERS[dice2])
    print("    ", dice1, "-", dice2)

    # Award the 10 mon bonus for a total of 2 or 7.
    roll_total = dice1 + dice2
    if roll_total == 2 or roll_total == 7:
        print("The total of your roll was", roll_total, ". You got a 10 mon bonus!")
        purse += 10

    # Determine whether the roll is even (CHO) or odd (HAN).
    roll_is_even = roll_total % 2 == 0
    if roll_is_even:
        correct_bet = "CHO"
    else:
        correct_bet = "HAN"

    player_won = bet == correct_bet

    # Apply the bet result and collect the 12% house fee on a win.
    if player_won:
        print("You won! You take", pot, "mon.")
        purse += pot
        house_fee = int(pot * 0.12)
        print("The house collects a", house_fee, "mon fee (12%).")
        purse -= house_fee
    else:
        purse -= pot
        print("You lost!")

    # End the game if the player has no money left.
    if purse == 0:
        print("You have run out of money!")
        print("Thanks for playing!")
        sys.exit()
