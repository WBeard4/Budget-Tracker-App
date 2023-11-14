import sqlite3
from database import *

db = Database()

class Goals():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect("Set_goal.db")
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check if the 'Set_goal' table has been created. If it hasn't, it will create it, and will open it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Set_goal'")
        table_exists = self.cursor.fetchone()
        if table_exists:
            pass
        else:
            self.cursor.execute('''CREATE TABLE Set_goal
                                (id INTEGER PRIMARY KEY,
                                Category TEXT,
                                Amount INTEGER)''')
            self.db.commit()

    def create(self):
        """
        Creates a new goal, by retrieving list of categories from income / expense db, and using those as the options
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
        
        goal_category = input(": ").title().strip()
        goal_amount = int(input("How much is the goal?: £"))
        self.cursor.execute("SELECT MAX(id) FROM Set_goal")
        latest_id = self.cursor.fetchone()
        if latest_id[0] is not None:
            latest_id = latest_id[0] + 1
        else:
            latest_id = 1

        self.cursor.execute('''INSERT INTO Set_goal(id, Category, Amount) 
                            VALUES (?, ?, ?)''', (latest_id, goal_category, goal_amount,))
        print(f"Goal for {goal_category} set to £{goal_amount}")
        self.db.commit()
    
    def view(self):
        """
        Prints a list of all the goals, then lets the user choose which they want to see the value for 
        """
        self.cursor.execute("SELECT * FROM Set_goal")
        goals = self.cursor.fetchall()
        print("Please choose from the below goals: ")
        goal_list = []
        for goal in goals:
            goal_name = goal[1]
            if goal_name not in goal_list:
                goal_list.append(goal_name)
            else:
                continue
        goal_list = sorted(goal_list)
        for i in goal_list:
            print(i)

        goal_choice = input(": ").strip().title()
        self.cursor.execute("SELECT * FROM Set_goal WHERE Category = ?", (goal_choice,))
        goal_category = self.cursor.fetchone()
        if goal_category:
            print(f"Category: {goal_choice}. goal: £{goal_category[2]}\n")
        else:
            print(f"No goal set for {goal_choice}\n")