from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

from Wordcheck.Wordcheck import Wordcheck

class WordCheckApp(App):
    def build(self):
        app = Wordcheck()
        app.getWords('tyupe', 3)
        return app

if __name__ == '__main__':
    WordCheckApp().run()