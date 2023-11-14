import sqlite3

class Database():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect("tracker.db")
        self.cursor = self.db.cursor()
        self.open()
        
    def open(self):

        """
        Check if the 'Budget' table has been created. If it hasn't, it will create it, and will open it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Budget'")
        table_exists = self.cursor.fetchone()

        if table_exists:
            pass
        # Create the table
        else:
            self.cursor.execute('''CREATE TABLE Budget
                        (id INTEGER PRIMARY KEY,
                        Item TEXT,
                        Expense BOOLEAN,
                        Cost INTEGER,
                        Category TEXT,
                        Total INTEGER)''')
            
            self.db.commit()
            print("Budget planner created")
    
    def close(self):
        """
        Closes the database connection
        """
        self.db.close()
        
    def next_id(self):
        """
        Returns the next id to be used in the database
        """
        self.cursor.execute("SELECT MAX(id) FROM Budget")
        max_id = self.cursor.fetchone()
        if max_id[0] is not None:
            return(max_id[0] + 1)
        else:
            return(1)
    
    def check_total(self):
        """
        Returns the total money in the budget
        """
        self.cursor.execute("SELECT Total FROM Budget")
        total = self.cursor.fetchone()
        if total:
            return total[0]
        else:
            return 0
        
    def add_income(self, id, item, expense, amount, category, total_money):
        """
        Adds a new income or expense entry to budget table
        :param id: ID for the new entry
        :param item: Name of the income/expense source
        :param expense: Boolean value to tell if it is an expense or an income
        :param amount: Value of the income/expense
        :param category: Which category the income/expense comes under
        :total: Total money after the income/expense
        """
        self.cursor.execute('''INSERT INTO Budget(id, Item, Expense, Cost, Category, Total) 
                    VALUES(?, ?, ?, ?, ?, ?)''', (id, item, expense, amount, category, total_money))
        self.db.commit()
    
    def view_income(self):
        """
        Prints a list of all the incomes
        """
        self.cursor.execute("SELECT * FROM Budget WHERE Expense = 0")
        income = self.cursor.fetchall()
        if income:
            for item in income:
                print(f"Income source: {item[1]}\nAmount: £{item[3]} \n")
        else:
            print("No income found")

    def income_categories(self):
        """
        Prints a list of all the incomes ordered by category
        """
        self.cursor.execute("SELECT * FROM Budget WHERE Expense = 0 ORDER BY Category")
        income = self.cursor.fetchall()
        if income:
            for item in income:
                print(f"Category: {item[4].title()} - {item[1]} Amount: £{item[3]}")

    def view_expense(self):
        """
        Prints a list of all the expenses
        """
        self.cursor.execute("SELECT * FROM Budget WHERE Expense = 1")
        expense = self.cursor.fetchall()
        if expense:
            for item in expense:
                print(f"Expense source: {item[1]}\nAmount: £{item[3]} \n")
        else:
            print("No Expense found")

    def expense_categories(self):
        """
        Prints a list of all the expenses ordered by category
        """
        self.cursor.execute("SELECT * FROM Budget WHERE Expense = 1 ORDER BY Category")
        expense = self.cursor.fetchall()
        if expense:
            for item in expense:
                print(f"Category: {item[4].title()} - {item[1]} Cost: £{item[3]}")

    def get_categories(self):
        """
        Returns a list of all the categories
        """
        self.cursor.execute("SELECT * FROM Budget")
        categories = self.cursor.fetchall()
        return categories