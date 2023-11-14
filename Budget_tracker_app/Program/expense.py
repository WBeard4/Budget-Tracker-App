from database import *
db = Database()


class Expense():
    def __init__(self, db):
        """
        Opens a database connection to the budget table
        """
        self.database = db

    def add(self):
        """
        Asks for inputs to be passed onto the add_income function in the database class
        :param id: ID for the new entry
        :param item: Name of the income/expense source
        :param expense: Boolean value to tell if it is an expense or an income
        :param amount: Value of the income/expense
        :param category: Which category the income/expense comes under
        :total: Total money after the income/expense
        """
        item = input("Expense Source: ")
        amount = float(input("How much did was this expense?: £"))
        category = input("Which category does this fall under?: ").title().strip()
        expense = 0
        id = self.database.next_id()
        total = self.database.check_total()
        total_money = total - amount
        self.database.add_income(id, item, expense, amount, category, total_money)
        print(f"{item} has been added to budget planner\n")

    def view(self):
        """
        Calls database function to list all expenses
        """
        print("Here is a list of your expenses: \n")
        self.database.view_expense()

    def categories(self):
        """
        Calls database function to list all expenses by category
        """
        print("Here is a list of your expenses ordered by category: \n")
        self.database.expense_categories()
          