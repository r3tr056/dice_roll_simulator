import tkinter as tk
import random

# Function to simulate rolling the dice
def roll_dice():
    result = random.randint(1, 6)
    result_label.config(text=f'Result: {result}')

# Create the main window
root = tk.Tk()
root.title("Dice Simulator")

# Create a label to display the result
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 20))
result_label.pack(pady=20)

# Create a button to roll the dice
roll_button = tk.Button(root, text="Roll Dice", font=("Helvetica", 16), command=roll_dice)
roll_button.pack(pady=20)

# Run the application
root.mainloop()
