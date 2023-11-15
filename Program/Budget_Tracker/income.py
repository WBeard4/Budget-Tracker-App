import sqlite3
class Income():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect('income.db')
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check the income table has been created, creates it if it hasn't, then connects to it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='income'")
        table_exists = self.cursor.fetchone()

        if table_exists:
            pass
        else:
            self.cursor.execute("""CREATE TABLE income 
                                (id INTEGER PRIMARY KEY, 
                                item TEXT, 
                                amount FLOAT, 
                                category TEXT)""")
            self.db.commit()

    def close(self):
        """
        Closes the database connection
        """
        self.db.close()

    def next_id(self):
        """
        Returns the next available id for the income table
        """
        self.cursor.execute("SELECT MAX(id) FROM income")
        max_id = self.cursor.fetchone()
        if max_id[0] is not None:
            return max_id[0] + 1
        else:
            return 1
        
    def check_total(self):
        """
        Returns the total amount of income
        """
        self.cursor.execute("SELECT SUM(amount) FROM income")
        total = self.cursor.fetchone()
        if total:
            return total
        else:
            return 0
    
    def add(self):
        """
        Adds an income to the income table
        :param id: The ID of the income
        :param item: The name of the income
        :param amount: The amount of the income
        :param category: The category of the income
        """
        id = self.next_id()
        item = input("Enter the name of the income source: ").strip()
        amount = float(input("Enter the amount of the income: £"))
        category = input("Enter the category of the income: ").strip()
        self.cursor.execute("INSERT INTO income VALUES (?, ?, ?, ?)", (id, item, amount, category))
        self.db.commit()
        print(f"{item} has been added to incomes.")

    def view(self):
        """
        Prints a list of all incomes
        """
        self.cursor.execute("SELECT * FROM income")
        incomes = self.cursor.fetchall()
        if incomes:
            for income in incomes:
                print(f"Income Source: {income[1]}\nAmount: £{income[2]}\nCategory: {income[3]}\n")
        else:
            print("No incomes found.")


    def categories(self):
        """
        Prints a list of all categories and amount of income for each
        """
        self.cursor.execute("SELECT category, SUM(amount) FROM income GROUP BY category")
        categories = self.cursor.fetchall()
        if categories:
            for category in categories:
                print(f"Category: {category[0]}\nAmount: £{category[1]}\n")
        else:
            print("No incomes found.")