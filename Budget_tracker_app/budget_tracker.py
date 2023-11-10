'''Compulsory Task (Option 1)
Follow these steps to build the expense and budget tracker app:
● Create a program that allows the user to:
○ add new expense categories to the database
○ update an expense amount
○ delete an expense category from the database
○ track their spending
○ add income
○ add income categories
○ delete an income category from the database
○ track their income
○ View expense or income categories
○ The program should be able to calculate the user’s budget based on
the income and expenses that they have provided
● Install the SQLite library. This will allow your app to communicate with the
SQLite database.
● Connect to the SQLite database. You can do this by using the "connect"
function from the sqlite3 library.
● Next, you will need to create your database tables to store your data. You
can use the "execute" function to execute SQL commands to create tables.
● Insert data: After creating tables, ensure that users are able to insert data
into them. You can use the "execute" function to execute SQL commands to
insert data.
● Ensure that users can retrieve data from the database using SQL queries.
● Close the connection to the database using the "close" function.
● The program should present the user with the following menu:
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
The program should perform the function that the user selects. The
implementation of these functions is left up to you.'''

# Import any libraries needed
import sqlite3
import sys

# Functions
# def add_expense
def add_expense():
    item = input("Name of item: ")
    cost = int(input("How much did this cost?: "))
    category = input("Which category does this fall under?: ").lower()
    expense = 1
    id = next_id()
    total = check_total()
    total_money = total- cost
    cursor.execute('''INSERT INTO Budget(id, Item, Expense, Cost, Category, Total) 
                   VALUES(?, ?, ?, ?, ?, ?)''', (id, item, expense, cost, category, total_money))
    db.commit()
    print(f"{item} has been added to budget planner")
    print()


# Going to be amending the total a lot, so creating a function to pull it
def check_total():
    cursor.execute("SELECT Total FROM Budget ORDER BY id DESC LIMIT 1")

    latest_total = cursor.fetchone()
    if latest_total:
        return(latest_total[0])
    else:
        return(0)

# Function to get the next id
def next_id():
    cursor.execute("SELECT MAX(id) FROM Budget")
    latest_id = cursor.fetchone()

    if latest_id[0] is not None:
        return(latest_id[0] + 1)
    else:
        return(1)

# def view_expenses
def view_expenses():
    cursor.execute("SELECT * FROM Budget WHERE Expense = 1")
    expenses = cursor.fetchall()
    if expenses:
        for item in expenses:
            print(f"Item {item[0]}: {item[1]} Cost: £{item[3]}")
    else:
        print("No expenses found")
    
# Connect / create the SQLite database
try:
    db = sqlite3.connect("tracker.db")
    cursor = db.cursor()

    # Check if the table exists, skip creation if it does
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Budget'")
    table_exists = cursor.fetchone()

    if table_exists:
        print("Opening budget planner")
    # Create the table
    else:
        cursor.execute('''CREATE TABLE Budget
                    (id INTEGER PRIMARY KEY,
                    Item TEXT,
                    Expense BOOLEAN,
                    Cost INTEGER,
                    Category TEXT,
                    Total INTEGER)''')
        
        db.commit()
        print("Budget planner created")


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
        # def view_expense_by_cat
        # def add_income
        # def view_income
        # def view_income_by_cat
        # def cat_budget
        # def view_cat_budget
        # def set_goals
        # def view_goals
            elif user_choice == 11:
                db.close()
                sys.exit("Exiting program")
        except sqlite3.Error as e:
            print(f"Error: {e}")
except sqlite3.Error as e:
    print(f"Error: {e}")