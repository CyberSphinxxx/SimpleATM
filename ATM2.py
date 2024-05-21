from tkinter import *

balance = 1000
def withdraw():
    amount_entry.pack()
    withdraw_button.config(text="Submit Withdraw", command=submit_withdrawal)

def submit_withdrawal():
    amount = int(amount_entry.get())
    if amount <= balance_label.balance:
        balance_label.balance -= amount
        result_label.config(text=f"You withdraw PHP {amount}.")
        balance_label.config(text=f"Your current balance is PHP {balance_label.balance}.")
    else:
        result_label.config(text=f"Insufficient Balance")

def check_balance():
    result_label.config(text=f"Your current balance is PHP {balance_label.balance}.")

root = Tk()

Label(root, text="Welcome to ATM").pack()
Button(root, text="Check Balance", command=check_balance).pack()

withdraw_button = Button(root, text="Withdraw", command=withdraw)
withdraw_button.pack()

amount_entry = Entry(root)

result_label = Label(root, text="")
result_label.pack()

balance_label = Label(root, text="")
balance_label.balance = balance
balance_label.pack()

root.mainloop()
