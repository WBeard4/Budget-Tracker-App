import sqlite3
from database import *

db = Database()

class Budget():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect("Set_budget.db")
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check if the 'Set_budget' table has been created. If it hasn't, it will create it, and will open it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Set_budget'")
        table_exists = self.cursor.fetchone()
        if table_exists:
            pass
        else:
            self.cursor.execute('''CREATE TABLE Set_budget
                                (id INTEGER PRIMARY KEY,
                                Category TEXT,
                                Amount INTEGER)''')
            self.db.commit()


    def create(self):
        """
        Creates a new budget, by retrieving list of categories from income / expense db, and using those as the options
        """
        categories = db.get_categories()
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
        budget_amount = int(input("How much is the budget?: £"))
        self.cursor.execute("SELECT MAX(id) FROM Set_budget")
        latest_id = self.cursor.fetchone()
        if latest_id[0] is not None:
            latest_id = latest_id[0] + 1
        else:
            latest_id = 1

        self.cursor.execute('''INSERT INTO Set_budget(id, Category, Amount) 
                            VALUES (?, ?, ?)''', (latest_id, budget_category, budget_amount,))
        print(f"Budget for {budget_category} set to £{budget_amount}")
        self.db.commit()
    
    def view(self):
        """
        Prints a list of all the budgets, then lets the user choose which they want to see the value for 
        """
        self.cursor.execute("SELECT * FROM Set_budget")
        budgets = self.cursor.fetchall()
        print("Please choose from the below budgets: ")
        budget_list = []
        for budget in budgets:
            budget_name = budget[1]
            if budget_name not in budget_list:
                budget_list.append(budget_name)
            else:
                continue
        budget_list = sorted(budget_list)
        for i in budget_list:
            print(i)

        budget_choice = input(": ").strip().title()
        self.cursor.execute("SELECT * FROM Set_budget WHERE Category = ?", (budget_choice,))
        budget_category = self.cursor.fetchone()
        if budget_category:
            print(f"Category: {budget_choice}. Budget: {budget_category[2]}\n")
        else:
            print(f"No budget set for {budget_choice}\n")










