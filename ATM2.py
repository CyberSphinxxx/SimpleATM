import tkinter as tk
from tkinter import messagebox

def create_atm():
    root = tk.Tk()
    root.title('ATM')
    balance = 0
    root.geometry('280x250')
    root.resizable(False, False)

    tk.Label(root, text='Welcome to ATM', font=("Arial", 16)).pack(pady=10)

    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    selected_action = tk.StringVar(value='')

    def activate():
        nonlocal balance
        action = selected_action.get()
        try:
            amount = float(input_box.get())
            if action == 'deposit':
                balance += amount
                messagebox.showinfo('Deposit', 'Money Deposit Successful')
            elif action == 'withdraw':
                if amount > balance:
                    messagebox.showerror('Withdrawal Error', 'Not enough balance')
                else:
                    balance -= amount
                    messagebox.showinfo('Withdrawal', 'Money Withdrawal Successful')
            else:
                messagebox.showerror('Action Error', 'Please select an action')
        except ValueError:
            messagebox.showerror('Input Error', 'Please enter a valid amount')

    def select_deposit():
        selected_action.set('deposit')
        activate()

    def select_withdraw():
        selected_action.set('withdraw')
        activate()

    tk.Label(button_frame, text='Deposit Money', font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
    tk.Button(button_frame, text='Activate', command=select_deposit).grid(row=0, column=1, padx=5, pady=5)
    tk.Label(button_frame, text='Withdraw Money', font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(button_frame, text='Activate', command=select_withdraw).grid(row=1, column=1, padx=5, pady=5)
    tk.Button(root, text='Check Balance', command=lambda: messagebox.showinfo('Balance', f'Current Balance: {balance}')).pack(pady=5)

    input_box = tk.Entry(root, font=("Arial", 16))
    input_box.pack(pady=10)
    return root


atm = create_atm()

atm.mainloop()
