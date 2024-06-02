# ATM Simulation using Tkinter

This is an activity for a Computer Programming 2 Subject in USTP, ```Submitted by: John Lemar L. Gonzales```

This project is a simple ATM simulation created using the Tkinter library in Python. It allows users to check their balance and withdraw funds through a graphical user interface.

## Features

- **Check Balance**: Displays the current balance.
- **Withdraw Funds**: Allows the user to withdraw a specified amount, updating the balance accordingly.
- **Input Validation**: Ensures the user cannot withdraw more than the available balance or enter invalid amounts.

## How It Works

### Components

- **Balance**: A global variable that stores the user's current balance, initialized to $1000.
- **Entry Widget**: Allows the user to input the amount they wish to withdraw.
- **Buttons**: Two buttons, one for checking the balance and another for withdrawing funds.
- **Labels**: Used to display messages and updates on the user's balance.

### Functions

1. **check_balance()**: Updates the label to display the current balance.
2. **withdraw()**: Handles the withdrawal process. It:
   - Retrieves the amount entered by the user.
   - Checks if the entered amount is valid and whether sufficient funds are available.
   - Updates the balance and the label accordingly.
   - Displays a warning message if the entered amount is invalid.

## Code

```python
import tkinter as tk
from tkinter import messagebox

# Initialize balance
balance = 1000

def check_balance():
    """Function to display the current balance"""
    global balance
    update_label.config(text=f"Current Balance: ${balance}")

def withdraw():
    """Function to withdraw a specified amount from the balance"""
    global balance, withdraw_entry, update_label
    try:
        amount = int(withdraw_entry.get())
        if amount > balance:
            update_label.config(text=f"Current Balance: ${balance}, Insufficient balance!")
        elif amount <= 0:
            messagebox.showwarning("Warning", "Enter a valid amount!")
        else:
            balance -= amount
            update_label.config(text=f"Withdrawn: ${amount}\nCurrent Balance: ${balance}")
    except ValueError:
        messagebox.showwarning("Warning", "Enter a valid number!")

# Set up the main application window
root = tk.Tk()
root.title("Created by: John Lemar Gonzales")

# Application Widgets
tk.Label(root, text="Welcome to the ATM", font=('Arial', 18)).pack()
tk.Button(root, text="Check Balance", command=check_balance).pack()
tk.Button(root, text="Withdraw Funds", command=withdraw).pack(pady=5)
withdraw_entry = tk.Entry(root)
withdraw_entry.pack(pady=5)

update_label = tk.Label(root, text="", font=('Arial', 14))
update_label.pack(pady=10)

# Start the main event loop
root.mainloop()
