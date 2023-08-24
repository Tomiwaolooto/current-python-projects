import mysql.connector


class Database:
    def __init__(self):
        self.host = "localhost"
        self.user = "root"
        self.password = ""
        self.database = "ABC_app_db"

        self.conn = mysql.connector.connect(host=self.host, user=self.user, password=self.password)
        self.cursor = self.conn.cursor()

        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")

        self.cursor.execute(f"USE {self.database}")

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS `users` (id INTEGER PRIMARY KEY AUTO_INCREMENT,"
                            " name VARCHAR (255) NOT NULL UNIQUE, email VARCHAR (255) NOT NULL UNIQUE,"
                            " gender VARCHAR(20), profile_pic VARCHAR(255), last_screen VARCHAR(40), "
                            "username VARCHAR(25) NOT NULL UNIQUE, Dob VARCHAR(10))")
        self.conn.commit()

    def save_data(self, email, username, name, gender, Dob, profile_pic):
        self.cursor.execute(f"INSERT INTO `users` (email, username, name, gender, Dob, profile_pic) VALUES ('{email}',"
                            f"'{username}', '{name}','{gender}','{Dob}', '{profile_pic}')")
        self.conn.commit()


Database().create_table()

