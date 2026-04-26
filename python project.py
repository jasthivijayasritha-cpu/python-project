import datetime

# Data Storage
income_list = []
expense_list = []

categories = [
    "Food", "Transport", "Rent", "Shopping",
    "Bills", "Entertainment", "Others"
]

# Add Income
def add_income():
    print("\n--- Add Income ---")

    source = input("Enter income source: ")
    amount = float(input("Enter income amount: "))
    date = input("Enter date (dd-mm-yyyy): ")

    income = {
        "source": source,
        "amount": amount,
        "date": date
    }

    income_list.append(income)
    print("Income Added Successfully")


# Add Expense
def add_expense():
    print("\n--- Add Expense ---")

    for i, cat in enumerate(categories):
        print(i + 1, cat)

    choice = int(input("Choose category: "))
    category = categories[choice - 1]

    amount = float(input("Enter expense amount: "))
    description = input("Enter description: ")
    date = input("Enter date (dd-mm-yyyy): ")

    expense = {
        "category": category,
        "amount": amount,
        "description": description,
        "date": date
    }

    expense_list.append(expense)
    print("Expense Added Successfully")


# View Summary
def view_summary():
    total_income = sum(i["amount"] for i in income_list)
    total_expense = sum(e["amount"] for e in expense_list)

    balance = total_income - total_expense

    print("\n===== FINANCIAL SUMMARY =====")
    print("Total Income :", total_income)
    print("Total Expense:", total_expense)
    print("Remaining Balance:", balance)


# Category Analysis
def category_analysis():
    print("\n===== CATEGORY ANALYSIS =====")

    cat_total = {}

    for e in expense_list:
        cat = e["category"]
        cat_total[cat] = cat_total.get(cat, 0) + e["amount"]

    for cat, amt in cat_total.items():
        print(cat, ":", amt)

    if cat_total:
        highest = max(cat_total, key=cat_total.get)
        print("\nHighest Spending Category:", highest)


# Budget Check
def check_budget():
    budget = float(input("Enter monthly budget: "))
    total_expense = sum(e["amount"] for e in expense_list)

    print("Total Expense:", total_expense)

    if total_expense > budget:
        print("⚠ Budget Exceeded!")
    elif total_expense > 0.75 * budget:
        print("⚠ 75% Budget Used")
    else:
        print("Budget under control")


# Smart Insights
def smart_insights():
    if not expense_list:
        print("No data")
        return

    cat_total = {}
    for e in expense_list:
        cat_total[e["category"]] = cat_total.get(e["category"], 0) + e["amount"]

    highest = max(cat_total, key=cat_total.get)

    print("\n===== SMART INSIGHTS =====")
    print("Highest spending category:", highest)

    if highest == "Food":
        print("Suggestion: Try reducing outside food expenses")
    elif highest == "Shopping":
        print("Suggestion: Limit unnecessary purchases")
    elif highest == "Entertainment":
        print("Suggestion: Reduce entertainment subscriptions")
    else:
        print("Suggestion: Track expenses regularly")


# Main Menu
def main():
    name = input("Enter User Name: ")

    print("\nWelcome", name)
    print("SMART FINANCE MANAGER")

    while True:
        print("\n====== MENU ======")
        print("1 Add Income")
        print("2 Add Expense")
        print("3 View Summary")
        print("4 Category Analysis")
        print("5 Check Budget")
        print("6 Smart Insights")
        print("0 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            category_analysis()
        elif choice == "5":
            check_budget()
        elif choice == "6":
            smart_insights()
        elif choice == "0":
            print("Thank you for using Smart Finance Manager")
            break
        else:
            print("Invalid choice")


# Run Program
main()