from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
import os
from pprint import pprint

Window.size = (300, 500)
path = os.path.dirname(os.path.realpath(__file__))

class HomeScreen(MDApp):

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def build(self):
        self.theme_cls.primary_palette = "DeepOrange"
        self.theme_cls.primary_hue = "A200"
        # self.theme_cls.theme_style = "Dark"
        screen = Builder.load_file(path + '\home.kv')
        # pprint(vars(screen))
        screen.ids.avatar.source = path + '\mine.png'
        return screen

    def on_start(self):
        pass

    def open_camera(self):
        print('open_camera')


HomeScreen().run()