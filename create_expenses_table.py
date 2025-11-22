# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan

import sqlite3

def create_table():
    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()

    # Creates the expenses table if it does not already exist so the app has a place to store every new expense.
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            date TEXT NOT NULL,
            category TEXT NOT NULL
        );
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    # This lets me run the file by itself to  check that the table got created properly.
    create_table()
    print("Table created.")

# CCT211 Project #2
# Name: Ariba Saleem & Braxton Rayan