import sqlite3
class Goal():
    def __init__(self) -> None:
        """
        Initializes a database connection and cursor
        """
        self.db = sqlite3.connect('goal')
        self.cursor = self.db.cursor()
        self.open()

    def open(self):
        """
        Check the goal table has been created, creates it if it hasn't, then connects to it
        """
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='goal'")
        table_exists = self.cursor.fetchone()

        if table_exists:
            pass
        else:
            self.cursor.execute("""CREATE TABLE goal 
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
        Returns the next available ID for the goal table
        """
        self.cursor.execute("SELECT MAX(id) FROM goal")
        max_id = self.cursor.fetchone()
        if max_id[0] is not None:
            return max_id[0] + 1
        else:
            return 1

    def create(self):
        """
        Adds a goal to the goal table
        :param id: The ID of the goal
        :param category: The category of the goal
        :param amount: The value of the goal
        """
        id = self.next_id()
        category = input("Enter category: ")
        amount = input("Enter amount: £")
        self.cursor.execute("INSERT INTO goal VALUES (?, ?, ?)", (id, category, amount))
        self.db.commit()
        print(f"Goal for {category} added successfully")

    def view(self):
        """
        Lists all goals in the goal table
        """
        self.cursor.execute("SELECT * FROM goal")
        goals = self.cursor.fetchall()
        if goals:
            for goal in goals:
                print(f"goal category: {goal[1]}\nAmount: £{goal[2]}\n")
        else:
            print("No goals found")