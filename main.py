# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

from tkinter import Tk, Button, Toplevel
import create_expenses_table
from add_expense_window import AddExpenseWindow
from view_all_expenses import ViewAllExpensesWindow

def open_add():
    # Opens a new top-level window so the add expense form appears separately from the main window.
    top = Toplevel(root)
    AddExpenseWindow(top)

def open_view_all():
    # This creates another top-level window that displays all the expenses stored in the database.
    top = Toplevel(root)
    ViewAllExpensesWindow(top)

def main():
    global root
    root = Tk()
    root.title("Student Budget Planner")
    root.geometry("300x180")

    # Row and column weights so the buttons stretch evenly when the window is resized.
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)

    # This makes sure the database table exists before the user interacts with anything.
    create_expenses_table.create_table()

    Button(root, text="Add New Expense", command=open_add).grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    Button(root, text="View All Expenses", command=open_view_all).grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
    # Added a quit button so the user can close the program directly from the interface.
    Button(root, text="Quit", command=root.destroy).grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan