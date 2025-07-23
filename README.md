Smart Expense Manager
A simple Python-based expense tracker that uses AI-powered categorization and SQLite for persistent storage. This project helps you manage daily expenses by automatically categorizing them based on descriptions you provide.
Features
Add, view, and manage expenses via a command-line interface (CLI).

AI-driven expense categorization using rule-based keyword matching.

Persistent storage using SQLite database (expenses.db).

Easily extendable for web UI integration (e.g., Streamlit or Flask).

How It Works
User inputs expense amount, description, and optionally date.

The AI module scans the description for keywords and assigns a relevant category.

The expense is stored in an SQLite database.

Users can view all expenses or filter by category/date using built-in functions.
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
(Optional) Create and activate a virtual environment:

bash
Copy
Edit
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
Install dependencies (if any):

bash
Copy
Edit
pip install -r requirements.txt
Note: This project uses Python’s built-in sqlite3 module, so no additional database drivers are required.

Usage
Run the main program:

bash
Copy
Edit
python main.py
Follow the on-screen prompts to add expenses, view reports, and manage your data.
