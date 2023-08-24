import plyer

from database import Database
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.card import MDCard


class FeedsCard(MDCard, FakeRectangularElevationBehavior):
    image = StringProperty()
    text = StringProperty()


class MainScreen(MDScreen):
    def upload_picture(self):
        plyer.filechooser.open_file(
            filters=["*png", "*jpg"], on_selection=self.save_picture)

    def save_picture(self, imagepath):
        path = Database().path
        if imagepath:
            img = open(f"{path}/image.txt", "w")
            path = imagepath[0]
            print(path)
            path = path.replace("\\", "/")
            img.write(path)

    def send(self):
        path = Database().path
        feed_text_field = self.ids['feed_text_field'].text

        with open(f"{path}/image.txt", "r") as image:
            image = image.readlines()
        img = image[0]

        conn = Database().conn
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO `feed_table` (`photo_path`, `message`) VALUES ('{img}', '{feed_text_field}')")
        conn.commit()
        self.ids['container'].add_widget(
            FeedsCard(text=feed_text_field, image=img))
