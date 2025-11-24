# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

from tkinter import *
from tkinter import messagebox, simpledialog
from datetime import datetime
import db
import re

class AddExpenseWindow:
    def __init__(self, master):
        self.master = master
        master.title("Add New Expense")
        master.geometry("400x300")

        for i in range(5):
            master.grid_rowconfigure(i, weight=1)
        master.grid_rowconfigure(5, weight=2)
        master.grid_columnconfigure(1, weight=1)

        # Expense description
        Label(master, text="Description:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.desc = Entry(master)
        self.desc.grid(row=0, column=1, sticky="ew", padx=5)

        # Used a validation command here so the amount field only accepts numbers or a decimal point.
        Label(master, text="Amount:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.amount = Entry(master)
        self.amount.grid(row=1, column=1, sticky="ew", padx=5)
        vcmd = master.register(lambda char: char.isdigit() or char == ".")
        self.amount.config(validate="key", validatecommand=(vcmd, "%S"))

        # The date field expects a specific format, so I add a label to guide the user.
        Label(master, text="Date (YYYY-MM-DD):").grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.date = Entry(master)
        self.date.grid(row=2, column=1, sticky="ew", padx=5)

        # I load the categories from the database so the user can pick from existing options.
        Label(master, text="Category:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
        self.categories = db.get_categories()
        self.category_var = StringVar(master)

        # If there are no categories yet, I add a default one so the menu still works.
        if self.categories:
            self.category_var.set(self.categories[0])
        else:
            self.categories = ["Other"]
            self.category_var.set("Other")

        self.category_menu = OptionMenu(master, self.category_var, *self.categories)
        self.category_menu.grid(row=3, column=1, sticky="ew", padx=5)

        # This lets the user add a new category without leaving the window.
        Button(master, text="Add New Category", command=self.add_category).grid(row=4, column=1, sticky="e", padx=5, pady=5)

        # Buttons to either save the expense or cancel the action.
        Button(master, text="Add Expense", command=self.save).grid(row=5, column=1, sticky="e", padx=5, pady=10)
        Button(master, text="Cancel", command=master.destroy).grid(row=6, column=1, sticky="e", padx=5, pady=5)

    def add_category(self):
        new_cat = simpledialog.askstring("New Category", "Enter new category name:")
        if new_cat and new_cat not in self.categories:
            self.categories.append(new_cat)
            menu = self.category_menu["menu"]
            menu.add_command(label=new_cat, command=lambda value=new_cat: self.category_var.set(value))
            self.category_var.set(new_cat)
            # I also save the new category in the database so it shows up next time.
            db.add_category(new_cat)


    def valid_date(self, date_text): # Validates date entry matches format
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def save(self):
        try:
            amount = float(self.amount.get())
        except ValueError:
            messagebox.showerror("Invalid Amount", "Amount must be a number")
            return

        date_text = self.date.get()
        if not self.valid_date(date_text):
            messagebox.showerror("Invalid Date", "Date must be in YYYY-MM-DD format")
            return

        # When all fields look valid, I save everything into the expenses table.
        db.add_expense(
            self.desc.get(),
            amount,
            date_text,
            self.category_var.get()
        )
        self.master.destroy()

# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan