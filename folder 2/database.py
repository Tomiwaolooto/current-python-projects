import mysql.connector  # import the module we'll be using for our database


class Database:  # our databse class

    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "note_app_db"

        self.conn = mysql.connector.connect(
            host=self.host, user=self.user, password=self.password)  # connecting to our database server. It is this variable we import as 'Database().conn' in other modules

        # cretes the cursor that helps with passing commands to our database server
        self.cursor = self.conn.cursor()

        # creates our database
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

        # tell our program to use this database
        self.cursor.execute(f"USE {self.database}")

    def create_notes_table(self):  # creates our 'notes' table
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS `notes` (id INTEGER PRIMARY KEY AUTO_INCREMENT, title VARCHAR(255) NOT NULL, body VARCHAR(25) NOT NULL)")

        self.conn.commit()


Database().create_notes_table()