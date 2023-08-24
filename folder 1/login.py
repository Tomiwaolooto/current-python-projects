from kivymd.uix.screen import MDScreen
from database import Database


class LoginScreen(MDScreen):
    choice = ''
    conn = Database().conn
    cursor = conn.cursor()

    def login(self):
        email_or_username_field = self.ids['email' or 'username'].text
        password = self.ids['password'].text

        if '@' in email_or_username_field and '.' in email_or_username_field:
            self.choice = "email"
        else:
            self.choice = "username"

        self.cursor.execute(f"SELECT* FROM users WHERE`{self.choice}` = {email_or_username_field} AND password = "
                            f"{password}")

        result = self.cursor.fetchall()
