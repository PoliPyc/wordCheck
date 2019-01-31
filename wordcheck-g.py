from kivy.app import App
from kivy.uix.widget import Widget
from random import randint

from Wordcheck.Wordcheck import Wordcheck

class WordCheckApp(App):
    def build(self):
        app = Wordcheck()
        # app.getWords('tyupe', 3)
        return app

if __name__ == '__main__':
    WordCheckApp().run()