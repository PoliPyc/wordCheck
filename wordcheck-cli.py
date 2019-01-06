#!/usr/bin/python3

import sys
from time import time

from Wordcheck.Wordcheck import Wordcheck

startTime = time()

if(len(sys.argv) < 2):
    raise("wordCheck: Nie podano liter")
else:
    letters = list(sys.argv[1])

if (len(sys.argv) < 3):
    length = len(letters)
else:
    length = int(sys.argv[2])

    app = Wordcheck()
    app.getWords(letters, length)


    print('done')

print("Query took {0:.2f} seconds.".format(time() - startTime))