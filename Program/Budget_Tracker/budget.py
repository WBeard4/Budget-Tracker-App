import sqlite3
class Budget():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect('budget')
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check the budget table has been created, creates it if it hasn't, then connects to it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='budget'")
        table_exists = self.cursor.fetchone()

        if table_exists:
            pass
        else:
            self.cursor.execute("""CREATE TABLE budget 
                                (id INTEGER PRIMARY KEY, 
                                category TEXT, 
                                amount FLOAT)""")
            self.db.commit()

    def close(self):
        """
        Closes the database connection
        """
        self.db.close()

    def next_id(self):
        """
        Returns the next available ID for the budget table
        """
        self.cursor.execute("SELECT MAX(id) FROM budget")
        max_id = self.cursor.fetchone()
        if max_id[0] is not None:
            return max_id[0] + 1
        else:
            return 1

    def create(self):
        """
        Adds a budget to the budget table
        :param id: The ID of the budget
        :param category: The category of the budget
        :param amount: The value of the budget
        """
        id = self.next_id()
        category = input("Enter category: ")
        amount = input("Enter amount: £")
        self.cursor.execute("INSERT INTO budget VALUES (?, ?, ?)", (id, category, amount))
        self.db.commit()
        print(f"Budget for {category} added successfully")

    def view(self):
        """
        Lists all budgets in the budget table
        """
        self.cursor.execute("SELECT * FROM budget")
        budgets = self.cursor.fetchall()
        if budgets:
            for budget in budgets:
                print(f"Budget category: {budget[1]}\nAmount: £{budget[2]}\n")
        else:
            print("No budgets found")