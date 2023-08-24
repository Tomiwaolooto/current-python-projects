from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from welcome import WelcomeScreen
from signup import SignUpScreen
from login import LoginScreen
from main_screen import MainScreen
from database import Database


class MyDiary(MDApp):  # import the SignUpSre
    def build(self):  # PyBook inherits from the MDApp
        Builder.load_file("welcome.kv")
        Builder.load_file("signup.kv")
        Builder.load_file("login.kv")
        Builder.load_file("main_screen.kv")

        self.wm = ScreenManager()  # add our screen manager class to a variable,self.wn
        screens = [
            WelcomeScreen(), SignUpScreen(), LoginScreen(), MainScreen()
        ]
        for screen in screens:  # loop through our list of screens
            self.wm.add_widget(screen)  # add each screen to our manager
        return self.wm


MyDiary().run()
