import random
import time

# ASCII Art for each side of the dice
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
}

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def display_dice(dice):
    dice_faces = [DICE_ART[die] for die in dice]
    for line in zip(*dice_faces):
        print("   ".join(line))

def main():
    print("Welcome to the Dice Roll Simulator!")
    while True:
        num_dice = input("How many dice would you like to roll? (1-5) or 'q' to quit: ")
        if num_dice.lower() == 'q':
            break
        if not num_dice.isdigit() or not 1 <= int(num_dice) <= 5:
            print("Please enter a number between 1 and 5.")
            continue

        num_dice = int(num_dice)
        print("\nRolling the dice...")
        time.sleep(1)  # Adding a short delay for effect
        dice = roll_dice(num_dice)
        display_dice(dice)
        print("\n")

if _name_ == "_main_":
    main()
