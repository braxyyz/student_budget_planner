# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

from tkinter import *
import db

class EditExpenseWindow:
    def __init__(self, master, expense):
        self.master = master
        master.title("Edit Expense")
        master.geometry("400x250")

        # Store the expense id so I know which specific record to update in the database.
        self.expense_id = expense[0]

        # Set the layout weights so the entries stretch properly when the window resizes.
        for i in range(4):
            master.grid_rowconfigure(i, weight=1)
        master.grid_rowconfigure(4, weight=2)
        master.grid_columnconfigure(1, weight=1)

        Label(master, text="Description:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.desc = Entry(master)
        self.desc.grid(row=0, column=1, sticky="ew", padx=5)
        # I pre-fill the entry so the user can see the current values before editing.
        self.desc.insert(0, expense[1])

        Label(master, text="Amount:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.amount = Entry(master)
        self.amount.grid(row=1, column=1, sticky="ew", padx=5)
        self.amount.insert(0, expense[2])

        Label(master, text="Date:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.date = Entry(master)
        self.date.grid(row=2, column=1, sticky="ew", padx=5)
        self.date.insert(0, expense[3])

        Label(master, text="Category:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.category = Entry(master)
        self.category.grid(row=3, column=1, sticky="ew", padx=5)
        self.category.insert(0, expense[4])

        # Clicking save calls the function that updates the database with the new values.
        Button(master, text="Save Changes", command=self.save).grid(row=4, column=1, sticky="e", pady=10)
        Button(master, text="Cancel", command=master.destroy).grid(row=5, column=1, sticky="e", pady=5)

    def save(self):
        # Update the expense using the values from the entry fields.
        db.update_expense(
            self.expense_id,
            self.desc.get(),
            float(self.amount.get()),
            self.date.get(),
            self.category.get()
        )
        # Close the edit window after saving because the main table will reload the new data.
        self.master.destroy()


# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan