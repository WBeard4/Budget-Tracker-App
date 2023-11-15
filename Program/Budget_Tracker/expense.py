import sqlite3
class Expense():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect('expense.db')
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check if the expense table has been created, creates it if it hasn't, then connects to it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='expense'")
        table_exists = self.cursor.fetchone()
        if table_exists:
            pass
        else:
            self.cursor.execute("""CREATE TABLE expense 
                                (id INTEGER PRIMARY KEY, 
                                item TEXT, amount FLOAT, 
                                category TEXT)""")
            self.db.commit()

    def close(self):
        """
        Closes the database connection
        """
        self.db.close()

    def next_id(self):
        """
        Returns the next available ID for an expense
        """
        self.cursor.execute("SELECT MAX(id) FROM expense")
        max_id = self.cursor.fetchone()
        if max_id[0] is not None:
            return max_id[0] + 1
        else:
            return 1
        
    def check_total(self):
        """
        Returns the total amount of expenses
        """
        self.cursor.execute("SELECT SUM(amount) FROM expense")
        total = self.cursor.fetchone()
        if total:
            return total
        else:
            return 0

    def add(self):
        """
        Adds an expense to the expense table
        :param id: The ID of the income
        :param item: The name of the expense
        :param amount: The expense amount
        :param category: The category of the expense
        """
        id = self.next_id()
        item = input("Enter the name of the expense: ")
        amount = float(input("Enter the amount of the expense: £"))
        category = input("Enter the category of the expense: ")
        self.cursor.execute("""INSERT INTO expense
                            VALUES (?, ?, ?, ?)""", (id, item, amount, category))
        self.db.commit()
        print(f"{item} has been added to expenses.")

    def view(self):
        """
        Prints a list of all expenses
        """
        self.cursor.execute("SELECT * FROM expense")
        expenses = self.cursor.fetchall()
        if expenses:
            for expense in expenses:
                print(f"Expense: {expense[1]}\nAmount: £{expense[2]}\nCategory: {expense[3]}\n")
        else:
            print("No expenses found.")

    def categories(self):
        """
        Prints a list of all categories and amount of expenses for each
        """
        self.cursor.execute("SELECT category, SUM(amount) FROM expense GROUP BY category")
        categories = self.cursor.fetchall()
        if categories:
            for category in categories:
                print(f"Category: {category[0]}\nAmount: £{category[1]}\n")
        else:
            print("No expenses found.")