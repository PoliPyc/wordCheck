import gzip
import itertools
from kivy.uix.widget import Widget
from kivy.properties import StringProperty

#########################################################
#   Make less ugly gui and mobile friendly              #
#   Speed word search (split files by first letter)     #
#   Change palette                                      #
#########################################################
class Wordcheck(Widget):
    WORDS_FILE = "words.dat"
    results = StringProperty()

    def perm(self, words, lenght, letters):
        perms = []
        foundWords = []
        perm = itertools.permutations(letters, lenght)
        for item in perm:
            perms.append(''.join(item))

        for word in words:
            if word in perms:
                foundWords.append(''.join(word))
                print(word)

        return foundWords

    def loadWordsFromFile(self, letters, lenght):
        file = gzip.open(self.WORDS_FILE, "rb")
        for line in file:
            line = line.decode('utf-8').strip()
            if len(line) == lenght and line[0] in letters:
                yield line

    def getWords(self, letters, length):
        words = self.loadWordsFromFile(letters, length)
        return self.perm(words, length, letters)

    def printWords(self, letters):
        words = self.getWords(letters, len(letters))
        for word in words:
            self.results = self.results + word + '\n'

        