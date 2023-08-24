from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from welcome_screen import WelcomeScreen
from sign_up import SignUpScreen
from mainscreen import MainScreen
from empl_sreen import AddEmployee


# from signup import SignUpScreen
# from login import LoginScreen
# from main_screen import MainScreen
# from database import Database
class Abc(MDApp):  # import the SignUpSre
    def build(self):  # PyBook inherits from the MDApp
        Builder.load_file("welcome_screen.kv")
        Builder.load_file("signup.kv")
        Builder.load_file("mainscreen.kv")
        Builder.load_file("+empl_screen.kv")

        self.wm = ScreenManager()  # add our screen manager class to a variable,self.wn
        screens = [
            WelcomeScreen(), SignUpScreen(), MainScreen(), AddEmployee()
        ]
        for screen in screens:  # loop through our list of screens
            self.wm.add_widget(screen)  # add each screen to our manager
        return self.wm


Abc().run()
