import tkinter as tk
from tkinter import messagebox

balance = 1000

def check_balance():
    global balance
    update_label.config(text=f"Current Balance: ${balance}")

def withdraw():
    global balance, withdraw_entry, update_label
    amount = int(withdraw_entry.get())
    if amount > balance:
        update_label.config(text=f"Current Balance: ${balance}, Insufficient balance!")
    elif amount <= 0:
        messagebox.showwarning("Warning", "Enter a valid amount!")
    else:
        balance -= amount
        update_label.config(text=f"Withdrawn: ${amount}\nCurrent Balance: ${balance}")

root = tk.Tk()
root.title("Created by: John Lemar Gonzales")

tk.Label(root, text="Welcome to the ATM", font=('Arial', 18)).pack()
tk.Button(root, text="Check Balance", command=check_balance).pack()
tk.Button(root, text="Withdraw Funds", command=withdraw).pack(pady=5)
withdraw_entry = tk.Entry(root)
withdraw_entry.pack(pady=5)

update_label = tk.Label(root, text="", font=('Arial', 14))
update_label.pack(pady=10)

root.mainloop()
