import os
import json

def load_data():
    if os.path.exists("budget_data.json"):
        with open("budget_data.json", "r") as file:
            return json.load(file)
    else:
        return {"income": 0, "expenses": []}

def save_data(data):
    with open("budget_data.json", "w") as file:
        json.dump(data, file)

def display_menu():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Budget")
    print("4. View Expense Analysis")
    print("5. Exit")

def add_income(data):
    income = float(input("Enter income amount: "))
    data["income"] += income
    print(f"Income of ${income} added successfully!")

def add_expense(data):
    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    data["expenses"].append({"category": category, "amount": amount})
    print(f"Expense of ${amount} in '{category}' category added successfully!")

def calculate_budget(data):
    total_expenses = sum(item["amount"] for item in data["expenses"])
    remaining_budget = data["income"] - total_expenses
    return remaining_budget

def view_budget(data):
    remaining_budget = calculate_budget(data)
    print(f"\nRemaining Budget: ${remaining_budget}\n")

def expense_analysis(data):
    categories = set(item["category"] for item in data["expenses"])
    print("\nExpense Analysis:")
    for category in categories:
        total_category_expense = sum(item["amount"] for item in data["expenses"] if item["category"] == category)
        print(f"{category}: ${total_category_expense}")
    print()

def main():
    data = load_data()

    while True:
        display_menu()

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_income(data)
        elif choice == "2":
            add_expense(data)
        elif choice == "3":
            view_budget(data)
        elif choice == "4":
            expense_analysis(data)
        elif choice == "5":
            save_data(data)
            print("Budget data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()