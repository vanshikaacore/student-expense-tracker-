expenses = []

while True:
    print("\n===== Student Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter expense category: ")
        amount = float(input("Enter amount: ₹"))

        expenses.append({
            "category": category,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        print("\n===== Expense List =====")

        if not expenses:
            print("No expenses recorded.")
        else:
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense['category']} - ₹{expense['amount']}")

    elif choice == "3":
        total = sum(expense["amount"] for expense in expenses)

        print("\n===== Summary =====")
        print(f"Total Expenses: ₹{total}")

    elif choice == "4":
        print("Thank you for using Student Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
