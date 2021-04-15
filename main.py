from kivymd.app import MDApp
from sm.sm import ScreenManagerRouter as sm

class MainApp(MDApp):

    def build(self):
        return sm


MainApp().run()