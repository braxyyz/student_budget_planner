# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

from tkinter import *
from tkinter import messagebox, Toplevel
from tkinter import ttk
import db
from edit_expense_window import EditExpenseWindow


class ViewAllExpensesWindow:
    def __init__(self, master):
        self.master = master
        master.title("View All Expenses")
        master.geometry("700x400")

        # Different weights so the table area takes more space than the buttons.
        master.grid_columnconfigure(0, weight=3)
        master.grid_columnconfigure(1, weight=1)
        for i in range(7):
            master.grid_rowconfigure(i, weight=1)

        # Treeview acts like the main table where all the expenses are displayed.
        columns = ("Description", "Amount", "Date", "Category")
        self.tree = ttk.Treeview(master, columns=columns, show="headings")
        self.tree.grid(row=0, column=0, rowspan=7, sticky="nsew", padx=(10, 0), pady=10)

        # I loop through the columns so I don’t have to write the heading code four times.
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=W, width=150)

        # Scrollbar so the user can scroll when there are many expenses.
        scrollbar = Scrollbar(master, orient="vertical", command=self.tree.yview)
        scrollbar.grid(row=0, column=0, rowspan=7, sticky="nse", padx=(0, 10), pady=10)
        self.tree.config(yscrollcommand=scrollbar.set)

        # Buttons for edit, delete, and closing the window.
        Button(master, text="Edit Selected", command=self.edit_selected).grid(row=0, column=1, sticky="ew", padx=5,
                                                                              pady=5)
        Button(master, text="Delete Selected", command=self.delete_selected).grid(row=1, column=1, sticky="ew", padx=5,
                                                                                  pady=5)
        Button(master, text="Close", command=master.destroy).grid(row=6, column=1, sticky="ew", padx=5, pady=10)

        self.load_expenses()

    def load_expenses(self):
        # Clear the table first so I don't accidentally duplicate the rows every time it refreshes.
        for row in self.tree.get_children():
            self.tree.delete(row)

        self.expenses = db.get_all_expenses()

        # Each record from the database is inserted into the table.
        for e in self.expenses:
            _id, desc, amt, date, category = e
            self.tree.insert("", "end", iid=_id, values=(desc, f"${amt:.2f}", date, category))

    def get_selected_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select an item first.")
            return None

        # The treeview uses the expense id as the item identifier, so I can match it directly.
        exp_id = int(selected[0])
        for e in self.expenses:
            if e[0] == exp_id:
                return e
        return None

    def edit_selected(self):
        exp = self.get_selected_expense()
        if not exp:
            return

        # Create a new window for editing so the user doesn't lose the main table view.
        top = Toplevel(self.master)
        EditExpenseWindow(top, exp)
        top.grab_set()  # This makes the edit window act like a modal window.
        top.wait_window()  # The table only refreshes after the edit window is closed.
        self.load_expenses()

    def delete_selected(self):
        exp = self.get_selected_expense()
        if not exp:
            return

        # Confirmation so the user doesn’t delete something by accident.
        if messagebox.askyesno("Confirm", "Delete this expense?"):
            db.delete_expense(exp[0])
            self.load_expenses()

# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan