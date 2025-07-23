
from db import connect, insert_expense
from categorize import auto_categorize
from datetime import datetime

def main():
    connect()  

    while True:
        print("\n--- Smart Expense Manager ---")
        print("1. Add Expense")
        print("2. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = float(input("Amount: "))
            description = input("Description: ")
            date = input("Date (YYYY-MM-DD, leave blank for today): ")
            if not date:
                date = datetime.now().strftime("%Y-%m-%d")

            category = auto_categorize(description)
            insert_expense(amount, description, category, date)
            print(f"Expense added under category: {category}")

        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
