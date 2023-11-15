This is budget tracker app, created to set goals and budgets, and add any incomes and expenses

  Budget\_Tracker package — Tracker documentation     

[Tracker](index.html)

  

*   [Budget\_Tracker package](#)
    *   [Submodules](#submodules)
    *   [Budget\_Tracker.budget module](#module-Budget_Tracker.budget)
        *   [`Budget`](#Budget_Tracker.budget.Budget)
            *   [`Budget.close()`](#Budget_Tracker.budget.Budget.close)
            *   [`Budget.create()`](#Budget_Tracker.budget.Budget.create)
            *   [`Budget.next_id()`](#Budget_Tracker.budget.Budget.next_id)
            *   [`Budget.open()`](#Budget_Tracker.budget.Budget.open)
            *   [`Budget.view()`](#Budget_Tracker.budget.Budget.view)
    *   [Budget\_Tracker.expense module](#module-Budget_Tracker.expense)
        *   [`Expense`](#Budget_Tracker.expense.Expense)
            *   [`Expense.add()`](#Budget_Tracker.expense.Expense.add)
            *   [`Expense.categories()`](#Budget_Tracker.expense.Expense.categories)
            *   [`Expense.check_total()`](#Budget_Tracker.expense.Expense.check_total)
            *   [`Expense.close()`](#Budget_Tracker.expense.Expense.close)
            *   [`Expense.next_id()`](#Budget_Tracker.expense.Expense.next_id)
            *   [`Expense.open()`](#Budget_Tracker.expense.Expense.open)
            *   [`Expense.view()`](#Budget_Tracker.expense.Expense.view)
    *   [Budget\_Tracker.goal module](#module-Budget_Tracker.goal)
        *   [`Goal`](#Budget_Tracker.goal.Goal)
            *   [`Goal.close()`](#Budget_Tracker.goal.Goal.close)
            *   [`Goal.create()`](#Budget_Tracker.goal.Goal.create)
            *   [`Goal.next_id()`](#Budget_Tracker.goal.Goal.next_id)
            *   [`Goal.open()`](#Budget_Tracker.goal.Goal.open)
            *   [`Goal.view()`](#Budget_Tracker.goal.Goal.view)
    *   [Budget\_Tracker.income module](#module-Budget_Tracker.income)
        *   [`Income`](#Budget_Tracker.income.Income)
            *   [`Income.add()`](#Budget_Tracker.income.Income.add)
            *   [`Income.categories()`](#Budget_Tracker.income.Income.categories)
            *   [`Income.check_total()`](#Budget_Tracker.income.Income.check_total)
            *   [`Income.close()`](#Budget_Tracker.income.Income.close)
            *   [`Income.next_id()`](#Budget_Tracker.income.Income.next_id)
            *   [`Income.open()`](#Budget_Tracker.income.Income.open)
            *   [`Income.view()`](#Budget_Tracker.income.Income.view)
    *   [Budget\_Tracker.main module](#budget-tracker-main-module)
    *   [Module contents](#module-Budget_Tracker)

[Tracker](index.html)

*   [](index.html)
*   Budget\_Tracker package
*   [View page source](_sources/Budget_Tracker.rst.txt)

* * *

Budget\_Tracker package[](#budget-tracker-package "Link to this heading")
==========================================================================

Submodules[](#submodules "Link to this heading")
-------------------------------------------------

Budget\_Tracker.budget module[](#module-Budget_Tracker.budget "Link to this heading")
--------------------------------------------------------------------------------------

_class_ Budget\_Tracker.budget.Budget[\[source\]](_modules/Budget_Tracker/budget.html#Budget)[](#Budget_Tracker.budget.Budget "Link to this definition")

Bases: `object`

close()[\[source\]](_modules/Budget_Tracker/budget.html#Budget.close)[](#Budget_Tracker.budget.Budget.close "Link to this definition")

Closes the database connection

create()[\[source\]](_modules/Budget_Tracker/budget.html#Budget.create)[](#Budget_Tracker.budget.Budget.create "Link to this definition")

Adds a budget to the budget table :param id: The ID of the budget :param category: The category of the budget :param amount: The value of the budget

next\_id()[\[source\]](_modules/Budget_Tracker/budget.html#Budget.next_id)[](#Budget_Tracker.budget.Budget.next_id "Link to this definition")

Returns the next available ID for the budget table

open()[\[source\]](_modules/Budget_Tracker/budget.html#Budget.open)[](#Budget_Tracker.budget.Budget.open "Link to this definition")

Check the budget table has been created, creates it if it hasn’t, then connects to it

view()[\[source\]](_modules/Budget_Tracker/budget.html#Budget.view)[](#Budget_Tracker.budget.Budget.view "Link to this definition")

Lists all budgets in the budget table

Budget\_Tracker.expense module[](#module-Budget_Tracker.expense "Link to this heading")
----------------------------------------------------------------------------------------

_class_ Budget\_Tracker.expense.Expense[\[source\]](_modules/Budget_Tracker/expense.html#Expense)[](#Budget_Tracker.expense.Expense "Link to this definition")

Bases: `object`

add()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.add)[](#Budget_Tracker.expense.Expense.add "Link to this definition")

Adds an expense to the expense table :param id: The ID of the income :param item: The name of the expense :param amount: The expense amount :param category: The category of the expense

categories()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.categories)[](#Budget_Tracker.expense.Expense.categories "Link to this definition")

Prints a list of all categories and amount of expenses for each

check\_total()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.check_total)[](#Budget_Tracker.expense.Expense.check_total "Link to this definition")

Returns the total amount of expenses

close()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.close)[](#Budget_Tracker.expense.Expense.close "Link to this definition")

Closes the database connection

next\_id()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.next_id)[](#Budget_Tracker.expense.Expense.next_id "Link to this definition")

Returns the next available ID for an expense

open()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.open)[](#Budget_Tracker.expense.Expense.open "Link to this definition")

Check if the expense table has been created, creates it if it hasn’t, then connects to it

view()[\[source\]](_modules/Budget_Tracker/expense.html#Expense.view)[](#Budget_Tracker.expense.Expense.view "Link to this definition")

Prints a list of all expenses

Budget\_Tracker.goal module[](#module-Budget_Tracker.goal "Link to this heading")
----------------------------------------------------------------------------------

_class_ Budget\_Tracker.goal.Goal[\[source\]](_modules/Budget_Tracker/goal.html#Goal)[](#Budget_Tracker.goal.Goal "Link to this definition")

Bases: `object`

close()[\[source\]](_modules/Budget_Tracker/goal.html#Goal.close)[](#Budget_Tracker.goal.Goal.close "Link to this definition")

Closes the database connection

create()[\[source\]](_modules/Budget_Tracker/goal.html#Goal.create)[](#Budget_Tracker.goal.Goal.create "Link to this definition")

Adds a goal to the goal table :param id: The ID of the goal :param category: The category of the goal :param amount: The value of the goal

next\_id()[\[source\]](_modules/Budget_Tracker/goal.html#Goal.next_id)[](#Budget_Tracker.goal.Goal.next_id "Link to this definition")

Returns the next available ID for the goal table

open()[\[source\]](_modules/Budget_Tracker/goal.html#Goal.open)[](#Budget_Tracker.goal.Goal.open "Link to this definition")

Check the goal table has been created, creates it if it hasn’t, then connects to it

view()[\[source\]](_modules/Budget_Tracker/goal.html#Goal.view)[](#Budget_Tracker.goal.Goal.view "Link to this definition")

Lists all goals in the goal table

Budget\_Tracker.income module[](#module-Budget_Tracker.income "Link to this heading")
--------------------------------------------------------------------------------------

_class_ Budget\_Tracker.income.Income[\[source\]](_modules/Budget_Tracker/income.html#Income)[](#Budget_Tracker.income.Income "Link to this definition")

Bases: `object`

add()[\[source\]](_modules/Budget_Tracker/income.html#Income.add)[](#Budget_Tracker.income.Income.add "Link to this definition")

Adds an income to the income table :param id: The ID of the income :param item: The name of the income :param amount: The amount of the income :param category: The category of the income

categories()[\[source\]](_modules/Budget_Tracker/income.html#Income.categories)[](#Budget_Tracker.income.Income.categories "Link to this definition")

Prints a list of all categories and amount of income for each

check\_total()[\[source\]](_modules/Budget_Tracker/income.html#Income.check_total)[](#Budget_Tracker.income.Income.check_total "Link to this definition")

Returns the total amount of income

close()[\[source\]](_modules/Budget_Tracker/income.html#Income.close)[](#Budget_Tracker.income.Income.close "Link to this definition")

Closes the database connection

next\_id()[\[source\]](_modules/Budget_Tracker/income.html#Income.next_id)[](#Budget_Tracker.income.Income.next_id "Link to this definition")

Returns the next available id for the income table

open()[\[source\]](_modules/Budget_Tracker/income.html#Income.open)[](#Budget_Tracker.income.Income.open "Link to this definition")

Check the income table has been created, creates it if it hasn’t, then connects to it

view()[\[source\]](_modules/Budget_Tracker/income.html#Income.view)[](#Budget_Tracker.income.Income.view "Link to this definition")

Prints a list of all incomes

Budget\_Tracker.main module[](#budget-tracker-main-module "Link to this heading")
----------------------------------------------------------------------------------

Module contents[](#module-Budget_Tracker "Link to this heading")
-----------------------------------------------------------------

* * *

© Copyright 2023, Will.

Built with [Sphinx](https://www.sphinx-doc.org/) using a [theme](https://github.com/readthedocs/sphinx_rtd_theme) provided by [Read the Docs](https://readthedocs.org).

jQuery(function () { SphinxRtdTheme.Navigation.enable(true); });
