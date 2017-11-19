#!/usr/bin/python3

import gzip
import itertools
import sys
from time import time
startTime = time()

WORDS_FILE = "words.dat"

def perm(words, lenght):
    perm = itertools.permutations(letters, lenght)
    for item in perm:
        perms.append(''.join(item))

    for word in words:
        if word in perms:
            print(word)

def getWords(letters, lenght):
    file = gzip.open(WORDS_FILE, "rb")
    for line in file:
        line = line.decode('utf-8').strip()
        if len(line) == lenght and line[0] in letters:
            yield line


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