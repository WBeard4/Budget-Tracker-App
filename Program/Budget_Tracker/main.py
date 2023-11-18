from expense import *
from income import *   
from budget import *
from goal import *
import sqlite3
import sys

# Initialize instances of required classes
income = Income()
expense = Expense()
budget = Budget()
goal = Goal()


# Main loop for user interaction
while True:
        try:
            # Get user choice for which operation they would like
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

            # Add an expense
            if user_choice == 1:
                expense.add()

            # View expenses
            elif user_choice == 2:
                expense.view()

            # View expenses by category
            elif user_choice == 3:
                expense.categories()

            # Add income
            elif user_choice == 4:
                income.add()
      
            # View income
            elif user_choice == 5:
                income.view()

            # View income by category
            elif user_choice == 6:
                income.categories()

            # Create a budget
            elif user_choice == 7:
                budget.create()

            # View budget
            elif user_choice == 8:
                budget.view()

            # Create financial goals
            elif user_choice == 9:
                goal.create()

            # View financial goals
            elif user_choice == 10:
                goal.view()
                
            # Exit
            elif user_choice == 11:
                income.close()
                expense.close()
                budget.close()
                goal.close()
                sys.exit("Exiting program")

        except sqlite3.Error as e:
            print(f"Error: {e}")