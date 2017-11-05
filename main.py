#!/usr/bin/python3

import itertools
import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class wordCheck(Widget):

    def perm(self, words, lenght, letters):
        perms = []
        perm = itertools.permutations(letters, lenght)
        for item in perm:
            perms.append(''.join(item))

        for word in words:
            if word in perms:
                print(word)

        return perms

    def getWordsFromFile(self, letters, lenght):
        file = open("slowa.txt", "r")
        for line in file:
            line = line.strip()
            if len(line) == lenght and line[0] in letters:
                yield line

    def getLetters(self, letters, length):
        words = self.getWordsFromFile(letters, length)
        return self.perm(words, length, letters)

class WordCheckApp(App):
    def build(self):
        app = wordCheck()
        app.getLetters('tyupe', 3)
        return app


if __name__ == '__main__':
    WordCheckApp().run()