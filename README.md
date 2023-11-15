This is budget tracker app, created to set goals and budgets, and add any incomes and expenses



Budget module
--------------------------------------------------------------------------------------


close()

Closes the database connection

create()

Adds a budget to the budget table :param id: The ID of the budget :param category: The category of the budget :param amount: The value of the budget

next\_id()

Returns the next available ID for the budget table

open()

Check the budget table has been created, creates it if it hasn’t, then connects to it

view()

Lists all budgets in the budget table

Expense module
----------------------------------------------------------------------------------------


add()

Adds an expense to the expense table :param id: The ID of the income :param item: The name of the expense :param amount: The expense amount :param category: The category of the expense

categories()

Prints a list of all categories and amount of expenses for each

check\_total()

Returns the total amount of expenses

close()

Closes the database connection

next\_id()

Returns the next available ID for an expense

open()

Check if the expense table has been created, creates it if it hasn’t, then connects to it

view()

Prints a list of all expenses

Goal module
----------------------------------------------------------------------------------


close()

Closes the database connection

create()

Adds a goal to the goal table :param id: The ID of the goal :param category: The category of the goal :param amount: The value of the goal

next\_id()

Returns the next available ID for the goal table

open()

Check the goal table has been created, creates it if it hasn’t, then connects to it

view()

Lists all goals in the goal table

Income module
--------------------------------------------------------------------------------------

add()

Adds an income to the income table :param id: The ID of the income :param item: The name of the income :param amount: The amount of the income :param category: The category of the income

categories()
Prints a list of all categories and amount of income for each

check\_total()

Returns the total amount of income

close()

Closes the database connection

next\_id()

Returns the next available id for the income table

open()

Check the income table has been created, creates it if it hasn’t, then connects to it

view()

Prints a list of all incomes
