# Avinash_decodelabs_tasks2
# Expense Tracker

### Brief One Line Summary
A lightweight, interactive command-line Python application that tracks daily expenses and calculates a running total with robust input validation.

 ### Overview
 This project is a simple, console-based utility designed to let users log financial transactions sequentially. It serves as a practical demonstration of core 
 programming principles like loops, conditional logic, exception handling, and persistent state management within a single execution runtime.

  ### Problem Statement
  Manually tracking daily expenses can be tedious. Many complex financial applications require heavy resource usage, accounts, or internet connectivity. 
  There is a  need for a minimalist, localized, and instant tool to accumulate numbers securely and quickly on a terminal without configuration overhead.

   ### Tools and Technologies
   * **Language:** Python 3.x
   * **Libraries/Modules:** Built-in features only (try-except handling, standard I/O via input() and print()).
     
   ###  Methods
   * **State Initialization:** Tracking values (total and count) outside the main operation loop to prevent state resets.
     
   * **Sentinel-Controlled Loop:** Utilizing a while True loop paired with a string break condition ('quit') to allow an arbitrary, user-defined number of entries.
     
   * **Defensive Programming (Poka-Yoke):** Implemented a try-except block to intercept ValueError exceptions, gracefully preventing code crashes when non-numeric strings are inputted.
     
   * **Accumulator Pattern:** Incrementally adding validated floating-point entries into a running total sum.

  ### How to Run this project?
1. Ensure you have Python installed on your system.
2. Save the provided script code into a file named `expense_tracker.py`
3. Open your terminal or command prompt and navigate to the directory containing the file.
4. Run the script using the following command:
   ``` bash
   python EXPENSE_TRACKER.pY

  ### Results & Conclusion
* The program successfully achieves its goal of tracking expenses reliably. By decoupling the logic accumulation phase from the final summary output phase, the terminal interface remains clean, predictable, and resilient against erratic user inputs.

 ### Future Work
 * **Data Persistence:** Integrate file I/O operations (CSV, JSON, or SQLite database) to save expense history across multiple sessions.

* **Categorization:** Allow users to tag expenses with categories (e.g., Food, Transport, Utilities).

* **Data Visualization:** Generate terminal-based or external matplotlib graphs showing spending trends over time.

### Dashboard/Model/Output
``` text

=== Expense Tracker ===
Enter an expense amount, or type 'quit' to stop.

Enter expense amount: 12.50
✅ Added $12.50  |  Running Total: $12.50

Enter expense amount: hello
⚠️  Invalid input. Please enter a number (or 'quit' to stop).

Enter expense amount: -5
⚠️  Expense cannot be negative. Try again.

Enter expense amount: 4.00
✅ Added $4.00  |  Running Total: $16.50

Enter expense amount: quit

=== Summary ===
Transactions logged: 2
Total Spent: $16.50


