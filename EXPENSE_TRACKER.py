def expense_tracker():
    total = 0.0          # Initialization (State) - kept OUTSIDE the loop
    count = 0            # Number of valid transactions logged

    print("=== Expense Tracker ===")
    print("Enter an expense amount, or type 'quit' to stop.\n")

    while True:
        user_input = input("Enter expense amount: ").strip()

        # Sentinel value check (Kill Switch)
        if user_input.lower() == 'quit':
            break

        # Defensive coding (Poka-Yoke) - validate input
        try:
            expense = float(user_input)
        except ValueError:
            print("⚠️  Invalid input. Please enter a number (or 'quit' to stop).\n")
            continue

        # Optional: reject negative expenses
        if expense < 0:
            print("⚠️  Expense cannot be negative. Try again.\n")
            continue

        # Accumulator pattern
        total += expense
        count += 1
        print(f"✅ Added ${expense:.2f}  |  Running Total: ${total:.2f}\n")

    # Output phase (decoupled from logic)
    print("\n=== Summary ===")
    print(f"Transactions logged: {count}")
    print(f"Total Spent: ${total:.2f}")


if __name__ == "__main__":
    expense_tracker()