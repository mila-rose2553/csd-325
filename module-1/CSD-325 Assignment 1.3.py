# Mariana Baker, Module 1.3 Assignment, 10/24/26
# This program demonstrates a count for bottles, a countdown, and a reminder for the user to buy more bottles.

"""
Assignment: On the Wall + Flowchart(s)
Ask for the number of bottles, count down to one, and remind the user to buy more.
"""

def countdown(bottles):
    """Print the countdown from the starting number of bottles to one."""
    while bottles > 1:
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
        bottles -= 1

    if bottles == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take it down and pass it around, no more bottles of beer on the wall.\n")


def main():
    """Get valid input, call countdown(), and print the closing reminder."""
    while True:
        try:
            bottles = int(input("How many bottles of beer are on the wall? "))
            if bottles > 0:
                break
            print("Please enter a whole number greater than zero.")
        except ValueError:
            print("Please enter a valid whole number.")

    countdown(bottles)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
