import mysql.connector


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "MyDairy_app_db"

        self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

        self.cursor.execute(f"USE {self.database}")

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY AUTO_INCREMENT,"
                            " email VARCHAR (255) NOT NULL UNIQUE, username VARCHAR(25) NOT NULL UNIQUE,"
                            " password VARCHAR(20), profile_pic VARCHAR(255), last_screen VARCHAR(40))")
        self.conn.commit()

    def save_data(self, email, username, password):
        self.cursor.execute(f"INSERT INTO `users` (email, username, password) VALUES ('{email}', '{username}', '{password}')")
        self.conn.commit()


Database().create_table()
