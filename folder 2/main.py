# import the builder class that loads the kv files.
from kivy.uix.screenmanager import ScreenManager  # manages the screens
from kivymd.app import MDApp  # the base class that our main class wil inherit from
from database import Database
from kivymd.app import MDApp
from kivy.lang import Builder
from main_sreen import MainScreen
from Add_note import AddNoteScreen, ListItem
from kivy.clock import Clock
from kivymd.toast import toast
from kivy.utils import get_color_from_hex as gch
from kivymd.uix.dialog import MDDialog


class NoteBook(MDApp):
    def build(self):  # this function automatically builds our app is launched

        # create an instance of the ScreenManager class. And assign it to a variable, 'self.wm'
        self.wm = ScreenManager()
        self.theme_cls.material_style = "M3"
        Builder.load_file("main_screen.kv")
        Builder.load_file("Add_note.kv")

        screens = [MainScreen(), AddNoteScreen()]  # create a list of our screens class instances
        Clock.schedule_once(self.DisplayNote, 3)

        for screen in screens:  # for each screen instance,
            # add it to our screen manager. let the screenmanager know about the screens
            self.wm.add_widget(screen)
        return self.wm  # return the loaded screen manager

    def DisplayNote(self, *args):
        conn = Database().conn
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notes")
        result = cursor.fetchall()
        print(result)
        for value in result:
            title = value[1]
            body = value[2]
            self.wm.get_screen("Main_screen").ids['Chr_lst_view'].add_widget(ListItem(title=title, body=body))

    def delete_note(self, title, body):
        conn = Database().conn
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM `notes` WHERE `title` ='{title}' AND `body` = '{body}'")
        conn.commit()
        self.wm.get_screen("Main_screen").ids['Chr_lst_view'].clear_widgets()
        toast("deleted successfully", background=gch("788080"))
        self.DisplayNote()

    # def ask_delete(self,*args):
    #     self.dialog = MDDialog(title="Delete Note", text="are you sure you want to delete this")


NoteBook().run()  # run the app in standalone mode.
