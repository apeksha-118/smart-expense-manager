
import sqlite3

def connect():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            description TEXT NOT NULL,
            category TEXT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def insert_expense(amount, description, category, date):
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (amount, description, category, date) VALUES (?, ?, ?, ?)",
                   (amount, description, category, date))
    conn.commit()
    conn.close()
