#!/usr/bin/python3

import gzip
import itertools
import sys
from time import time

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

startTime = time()

WORDS_FILE = "words.dat"

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

    def getWordsFromFile(letters, lenght):
        file = gzip.open(WORDS_FILE, "rb")
        for line in file:
            line = line.decode('utf-8').strip()
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

if(len(sys.argv) < 2):
    print("wordCheck: Nie podano liter")
else:
    letters = list(sys.argv[1])
    perms = []

    if(len(sys.argv) < 3 or sys.argv[2] == '3'):
        threeChars = getWords(letters, 3)
        perm(threeChars, 3)

    if(len(sys.argv) < 3 or sys.argv[2] == '4'):
        fourChars = getWords(letters, 4)
        perm(fourChars, 4)

    if(len(sys.argv) < 3 or sys.argv[2] == '5'):
        fiveChars = getWords(letters, 5)
        perm(fiveChars, 5)

    if (len(sys.argv) < 3 or sys.argv[2] == '6'):
        fiveChars = getWords(letters, 6)
        perm(fiveChars, 6)

    if (len(sys.argv) < 3 or sys.argv[2] == '7'):
        fiveChars = getWords(letters, 7)
        perm(fiveChars, 7)


    print('done')

print("Query took {0:.2f} seconds.".format(time() - startTime))

if __name__ == '__main__':
    WordCheckApp().run()