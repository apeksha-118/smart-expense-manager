 # Smart Expense Manager

A simple Python-based expense tracker that uses AI-powered categorization and SQLite for persistent storage. This project helps you manage daily expenses by automatically categorizing them based on descriptions you provide.

---

## Features

- Add, view, and manage expenses via a command-line interface (CLI).
- AI-driven expense categorization using rule-based keyword matching.
- Persistent storage using SQLite database (`expenses.db`).
- Easily extendable for web UI integration (e.g., Streamlit or Flask).

---

## How It Works

1. User inputs expense amount, description, and optionally date.
2. The AI module scans the description for keywords and assigns a relevant category.
3. The expense is stored in an SQLite database.
4. Users can view all expenses or filter by category/date using built-in functions.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
2. (Optional) Create and activate a virtual environment:
   On macOS/Linux:
   ```bash
   python -m venv env
   source env/bin/activate
  On Windows:
  ```powershell
  python -m venv env
  .\env\Scripts\activate




 
