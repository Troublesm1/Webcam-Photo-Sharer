from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests

Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
    #GET USER QUERY FROM INPUT
        query = self.manager.current_screen.ids.user_query.text

    #GET WIKIPEDIA PAGE AND FIRST URL LINK
        page = wikipedia.page(query)
        image_link = page.images[0]
        return image_link

    def download_image(self):
    # DOWNLOAD THE IMAGE
        req = requests.get(self.get_image_link())
        imagepath = 'files/image.jpg'
        with open(imagepath, 'wb') as file:
            file.write(req.content)
        return imagepath

    def set_image(self):
    # SET THE IMAGE IN THE IMAGE WIDGET
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()