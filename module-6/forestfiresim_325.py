#Mariana Baker, Kaile Vallejo, Leon Truong, and Yulia Mostovoi
# Module 6.2 Assignment
#11/22/26
"""Forest Fire Simulation - Module 6.2 Assignment
A permanent blue lake in the center of the forest acts as a firebreak.
Press Ctrl-C to stop the simulation.
"""

import random
import sys
import time

try:
    import bext
except ImportError:
    print("This program requires the bext module.")
    print("Install it with: pip install bext")
    sys.exit(1)

# Display dimensions.
WIDTH = 79
HEIGHT = 22

TREE = "A"
FIRE = "@"
LAKE = "~"       # Permanent blue water; it never changes.
EMPTY = " "

INITIAL_TREE_DENSITY = 0.20
GROW_CHANCE = 0.01
FIRE_CHANCE = 0.01
PAUSE_LENGTH = 0.5

# Fixed oval lake, roughly centered in the display.
LAKE_CENTER_X = WIDTH // 2
LAKE_CENTER_Y = HEIGHT // 2
LAKE_RADIUS_X = 7
LAKE_RADIUS_Y = 3


def is_lake_cell(x, y):
    """Return True if the coordinates are inside the permanent lake."""
    dx = (x - LAKE_CENTER_X) / LAKE_RADIUS_X
    dy = (y - LAKE_CENTER_Y) / LAKE_RADIUS_Y
    return dx * dx + dy * dy <= 1


def createNewForest():
    """Create the forest grid and place the permanent lake."""
    forest = {"width": WIDTH, "height": HEIGHT}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            if is_lake_cell(x, y):
                forest[(x, y)] = LAKE
            elif random.random() <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY

    return forest


def displayForest(forest):
    """Display trees, fire, empty spaces, and the blue lake."""
    bext.goto(0, 0)

    for y in range(forest["height"]):
        for x in range(forest["width"]):
            cell = forest[(x, y)]

            if cell == TREE:
                bext.fg("green")
                print(TREE, end="")
            elif cell == FIRE:
                bext.fg("red")
                print(FIRE, end="")
            elif cell == LAKE:
                bext.fg("blue")
                print(LAKE, end="")
            else:
                bext.fg("reset")
                print(EMPTY, end="")
        print()

    bext.fg("reset")
    print("Grow chance: {}%  ".format(GROW_CHANCE * 100), end="")
    print("Lightning chance: {}%  ".format(FIRE_CHANCE * 100), end="")
    print("Press Ctrl-C to quit.")


def runSimulationStep(forest):
    """Return the next grid; lake cells remain unchanged and block fire."""
    nextForest = {
        "width": forest["width"],
        "height": forest["height"],
    }

    for x in range(forest["width"]):
        for y in range(forest["height"]):
            # Skip cells already assigned by an earlier fire-spread event.
            if (x, y) in nextForest:
                continue

            current_cell = forest[(x, y)]

            # The lake is permanent: never grow, ignite, or spread through it.
            if current_cell == LAKE:
                nextForest[(x, y)] = LAKE
                continue

            if current_cell == EMPTY and random.random() <= GROW_CHANCE:
                nextForest[(x, y)] = TREE

            elif current_cell == TREE and random.random() <= FIRE_CHANCE:
                nextForest[(x, y)] = FIRE

            elif current_cell == FIRE:
                # Flames can spread only to tree cells, never to lake cells.
                for ix in range(-1, 2):
                    for iy in range(-1, 2):
                        neighbor = (x + ix, y + iy)
                        if forest.get(neighbor) == TREE:
                            nextForest[neighbor] = FIRE

                # The burning tree is consumed.
                nextForest[(x, y)] = EMPTY

            else:
                nextForest[(x, y)] = current_cell

    return nextForest


def main():
    """Run the forest fire simulation until the user stops it."""
    forest = createNewForest()
    bext.clear()

    while True:
        displayForest(forest)
        forest = runSimulationStep(forest)
        time.sleep(PAUSE_LENGTH)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
