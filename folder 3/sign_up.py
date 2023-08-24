from database import Database
from kivymd.toast import toast
import re
from kivy.utils import get_color_from_hex as gch
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
import plyer


class SignUpScreen(MDScreen):

    def upload_picture(self):
        plyer.filechooser.open_file(filters=["*png", "*jpg"])

    def open_datepicker(self):
        self.datepicker = MDDatePicker()
        self.datepicker.bind(on_save= self.save, on_cancel = self.cancel)
        self.datepicker.open()
    def save(self, instance, value, date_range):
        print(value)
        self.ids['dob'].text = str(value)
        self.datepicker.dismiss()

    def cancel(self, instance, value):
        self.datepicker.dismiss()

    def Checkbox_click(self, instance, value, gender):
        if value == True:
            self.ids.gen.text = f'{gender}'


    def signup(self):
        gender = self.ids['gen'].text
        email = self.ids['email'].text
        username = self.ids['username'].text
        name = self.ids['name'].text
        dob = self.ids['dob'].text
        profile_pic = self.ids['picture'].text

        pattern_email = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org)"
        if email == "" or username == "" or name == "":
            toast("all fields are required")
        elif not re.search(pattern_email, email):
            toast("please enter email in [a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net|org) format")
        elif len(name) < 2 or len(name) > 25:
            toast("password must contain 4-6 characters ")
        else:
            Database().save_data(email, username, name, gender, dob, profile_pic)

        toast("saved successfully", background=gch("2888A0"))
        self.manager.current = "Welcome_screen"