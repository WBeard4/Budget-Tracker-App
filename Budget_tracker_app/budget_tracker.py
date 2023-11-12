# Import any libraries needed
import sqlite3
import sys

# Functions
# def add_expense
def add_expense():
    item = input("Name of item: ")
    cost = float(input("How much did this cost?: £"))
    category = input("Which category does this fall under?: ").title().strip()
    expense = 1
    id = next_id()
    total = check_total()
    total_money = total- cost
    cursor_tracker.execute('''INSERT INTO Budget(id, Item, Expense, Cost, Category, Total) 
                   VALUES(?, ?, ?, ?, ?, ?)''', (id, item, expense, cost, category, total_money))
    db_tracker.commit()
    print(f"{item} has been added to budget planner")
    print()

    # Take expense from budget if category has a budget
    cursor_budget.execute('''SELECT * FROM Set_budget WHERE Category = ? ORDER BY id DESC LIMIT 1 ''', (category,))
    old_budget = cursor_budget.fetchone()
    if old_budget:
        old_budget = float(old_budget[2])
        new_budget = old_budget - cost

        cursor_budget.execute("SELECT MAX(id) FROM Set_budget")
        latest_id = cursor_budget.fetchone()
        if latest_id[0] is not None:
            latest_id = latest_id[0] + 1
        else:
            latest_id = 1
        
        cursor_budget.execute('''INSERT INTO Set_Budget(id, Category, Amount) VALUES(?, ?, ?)''', (latest_id, category, new_budget))
        db_budget.commit()
        print(f"Current budget for this category: £{new_budget}")
    else:
        pass

# Going to be amending the total a lot, so creating a function to pull it
def check_total():
    cursor_tracker.execute("SELECT Total FROM Budget ORDER BY id DESC LIMIT 1")

    latest_total = cursor_tracker.fetchone()
    if latest_total:
        return(latest_total[0])
    else:
        return(0)

# Function to get the next id
def next_id():
    cursor_tracker.execute("SELECT MAX(id) FROM Budget")
    latest_id = cursor_tracker.fetchone()

    if latest_id[0] is not None:
        return(latest_id[0] + 1)
    else:
        return(1)

# Function to print the total current balance
def current_balance():
    print(f"Current balance: £{check_total()}")

# def view_expenses
def view_expenses():
    cursor_tracker.execute("SELECT * FROM Budget WHERE Expense = 1")
    expenses = cursor_tracker.fetchall()
    if expenses:
        for item in expenses:
            print(f"Item {item[0]}: {item[1]} Cost: £{item[3]}")
    else:
        print("No expenses found")
    
# def view_expense_by_cat
def view_expense_by_cat():
    cursor_tracker.execute("SELECT * FROM Budget WHERE Expense = 1 ORDER BY Category")
    expenses = cursor_tracker.fetchall()
    if expenses:
        for item in expenses:
            print(f"Category: {item[4].title()} - {item[1]} Cost: £{item[3]}")

# def add_income
def add_income():
    item = input("Please input income source: ")
    cost = float(input("How much is this income?: £"))
    category = input("What category does this fall under?: ").title().strip()
    expense = 0
    id = next_id()
    total = check_total()
    total_money = total + cost
    cursor_tracker.execute('''INSERT INTO Budget(id, Item, Expense, Cost, Category, Total) 
                    VALUES(?, ?, ?, ?, ?, ?)''', (id, item, expense, cost, category, total_money))
    db_tracker.commit()
    print(f"{item} has been added to budget planner")
    print()

# def view_income
def view_income():
    cursor_tracker.execute("SELECT * FROM Budget WHERE Expense = 0")
    income = cursor_tracker.fetchall()
    if income:
        for item in income:
            print(f"Item {item[0]}: {item[1]} Amount: £{item[3]}")
    else:
        print("No income found")

# def view_income_by_cat
def view_income_by_cat():
    cursor_tracker.execute("SELECT * FROM Budget WHERE Expense = 0 ORDER BY Category")
    incomes = cursor_tracker.fetchall()
    if incomes:
        for item in incomes:
            print(f"Category: {item[4].title()} - {item[1]} Cost: £{item[3]}")

# def cat_budget
def cat_budget():
    cursor_tracker.execute("SELECT * FROM Budget")
    categories = cursor_tracker.fetchall()
    print("Please choose from the below categories")
    category_list = []
    for category in categories:
        category_name = category[4]
        if category_name not in category_list:
            category_list.append(category_name)
        else:
            continue
    category_list = sorted(category_list)
    print(category_list)
    for i in category_list:
        print(i)
    budget_category = input(": ").title().strip()
    budget_amount = input("How much is the budget?: £")

    cursor_tracker.execute("SELECT MAX(id) FROM Set_budget")
    latest_id = cursor_tracker.fetchone()
    if latest_id[0] is not None:
        latest_id = latest_id[0] + 1
    else:
        latest_id = 1

    cursor_budget.execute('''INSERT INTO Set_budget(id, Category, Amount) 
                          VALUES (?, ?, ?)''', (latest_id, budget_category, budget_amount,))
    print(f"Budget for {budget_category} set to £{budget_amount}")
    db_budget.commit()

# Connect / create the SQLite database
try:
    # db_tracker is used for income / expense table
    # db_budget is used for tracking budgets
    db_tracker = sqlite3.connect("tracker.db")
    cursor_tracker = db_tracker.cursor()

    # Check if the table exists, skip creation if it does
    cursor_tracker.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Budget'")
    table_exists = cursor_tracker.fetchone()

    if table_exists:
        print("Opening budget planner")
    # Create the table
    else:
        cursor_tracker.execute('''CREATE TABLE Budget
                    (id INTEGER PRIMARY KEY,
                    Item TEXT,
                    Expense BOOLEAN,
                    Cost INTEGER,
                    Category TEXT,
                    Total INTEGER)''')
        
        db_tracker.commit()
        print("Budget planner created")

    # Opening a second db to store budgets
    db_budget = sqlite3.connect("Set_budget.db")
    cursor_budget = db_budget.cursor()

    # Check if the table exists, skip creation if it does
    cursor_budget.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Set_budget'")
    table_exists = cursor_budget.fetchone()
    if table_exists:
        print("Opening Budgets")
    else:
        cursor_budget.execute('''CREATE TABLE Set_budget
                              (id INTEGER PRIMARY KEY,
                              Category TEXT,
                              Amount INTEGER)''')
        db_budget.commit()

# Get input from list of options
    while True:
        try:
            user_choice = int(input('''Please select from the following:
            1. Add expense
            2. View expenses
            3. View expenses by category
            4. Add income
            5. View income
            6. View income by category
            7. Set budget for a category
            8. View budget for a category
            9. Set financial goals
            10. View progress towards financial goals
            11. Quit
                Selection: '''))


        # def add_expense
            if user_choice == 1:
                add_expense()
        # def view_expenses
            elif user_choice == 2:
                view_expenses()
                current_balance()
        # def view_expense_by_cat
            elif user_choice == 3:
                view_expense_by_cat()
                current_balance()
        # def add_income
            elif user_choice == 4:
                add_income()
        # def view_income
            elif user_choice == 5:
                view_income()
                current_balance()
        # def view_income_by_cat
            elif user_choice == 6:
                view_income_by_cat()
                current_balance()
        # def cat_budget
            elif user_choice == 7:
                cat_budget()
        # def view_cat_budget
        # def set_goals
        # def view_goals
            elif user_choice == 11:
                db_tracker.close()
                sys.exit("Exiting program")
        except sqlite3.Error as e:
            print(f"Error: {e}")
except sqlite3.Error as e:
    print(f"Error: {e}")