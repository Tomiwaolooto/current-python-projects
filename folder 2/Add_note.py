from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen
from database import Database
from kivymd.uix.list import TwoLineIconListItem
from kivy.properties import StringProperty
from kivymd.toast import toast
from kivy.utils import get_color_from_hex as gch
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


class ListItem(TwoLineIconListItem):
    title = StringProperty()
    body = StringProperty()

    def show_notes(self):
        self.dialog = MDDialog(title=self.title, text=self.body, buttons=[MDFlatButton(text="Close", on_press=self.close)])

        self.dialog.open()

    def close(self, obj):
        self.dialog.dismiss()


class AddNoteScreen(MDScreen):
    conn = Database().conn
    cursor = conn.cursor()

    def go_back(self):
        self.manager.current = "Main_screen"

    def save_note(self):
        title = self.ids['title'].text
        body = self.ids['body'].text

        if title != "" and body != "":
            self.cursor.execute(f"INSERT INTO `notes` (`title`,`body`) VALUES ('{title}','{body}')")
            self.conn.commit()
            self.manager.get_screen("Main_screen").ids['Chr_lst_view'].add_widget(ListItem(title=title, body=body))

            toast("saved successfully", background=gch("788080"))
            self.manager.current = "Main_screen"
