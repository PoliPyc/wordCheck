import gzip
import itertools

class Wordcheck(object):
    WORDS_FILE = "words.dat"

    def perm(self, words, lenght, letters):
        perms = []
        perm = itertools.permutations(letters, lenght)
        for item in perm:
            perms.append(''.join(item))

        for word in words:
            if word in perms:
                print(word)

        return perms

    def loadWordsFromFile(self, letters, lenght):
        file = gzip.open(self.WORDS_FILE, "rb")
        for line in file:
            line = line.decode('utf-8').strip()
            if len(line) == lenght and line[0] in letters:
                yield line

    def getWords(self, letters, length):
        words = self.loadWordsFromFile(letters, length)
        return self.perm(words, length, letters)