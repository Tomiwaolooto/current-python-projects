from kivymd.uix.screen import MDScreen
from database import Database
from kivymd.toast import toast
import re
import plyer


class SignUpScreen(MDScreen):
    conn = Database().conn
    cursor = conn.cursor()

    def upload_picture(self):
        plyer.filechooser.open_file(filters=["*png", "*jpg"])

    def signup(self):
        email = self.ids['email'].text
        username = self.ids['Username'].text
        password = self.ids['password'].text

        pattern_email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
        if email == "" or username == "" or password == "":
            toast("all fields are required")
        elif not re.search(pattern_email, email):
            toast("please enter email in [a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org) format")
        elif len(password) < 4 or len(password) > 6:
            toast("password must contain 4-6 characters ")
        else:
            Database().save_data(email, username, password)
