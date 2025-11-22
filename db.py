# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

import sqlite3

DB_NAME = "expenses.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Create the categories table if it doesn’t already exist so the app can store custom categories.
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
    """)

    # This table stores all the actual expenses the user enters in the app.
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Database and tables get created as soon as the program runs.
init_db()

def get_categories():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # I fetch only the category names because that’s all I need for dropdown menus.
    cur.execute("SELECT name FROM categories ORDER BY name")
    rows = [row[0] for row in cur.fetchall()]

    conn.close()
    return rows

def add_category(name):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # INSERT OR IGNORE stops errors if the user tries to add the same category twice.
    cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (name,))

    conn.commit()
    conn.close()

def get_all_expenses():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Return all expenses so the table in the GUI can display them.
    cur.execute("SELECT id, description, amount, date, category FROM expenses")
    rows = cur.fetchall()

    conn.close()
    return rows

def add_expense(description, amount, date, category):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # This adds a new expense record based on what the user enters in the form.
    cur.execute("""
        INSERT INTO expenses (description, amount, date, category)
        VALUES (?, ?, ?, ?)
    """, (description, amount, date, category))

    conn.commit()
    conn.close()

def update_expense(expense_id, description, amount, date, category):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Update the row that matches the expense id the user selected in the GUI.
    cur.execute("""
        UPDATE expenses
        SET description=?, amount=?, date=?, category=?
        WHERE id=?
    """, (description, amount, date, category, expense_id))

    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # This removes the selected expense completely from the database.
    cur.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()

# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan