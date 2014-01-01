# Not necessarily the most efficient implementation, but as it runs sufficiently
# quickly as is no further optimization will be done.

import re
from itertools import permutations

class WordWhompSolver():

    def __init__(self, letters=None, dictionaryFile="pruned_dictionary.txt"):

        self.wordList = list()
        self.dictionaryFile = dictionaryFile
        self.letters = letters

        # Read dictionary into memory.
        self.read_in_dictionary()

    def read_in_dictionary(self):
        """
        Assumes dictionary file is in formate produced by pruner.py.
        """
        f = open(self.dictionaryFile)
        for line in f:
            self.wordList.append(line.rstrip())
        f.close()

    def solve(self):
        if self.letters == None:
            print "Must set game instance before calling solve()."
            exit()

        self.wordList = set(self.wordList)

        for i in xrange(3, 7, 1):
            print i, " letter words:"
            combinations = set([''.join(perm) for perm in \
                            permutations(self.letters, i)])
            for word in self.wordList.intersection(combinations):
                print word

    def set_instance(self, letters):
        letters = letters.lower()
        self.letters = letters

def is_valid_input(letters):
    try:
        letters = str(letters)
    except ValueError:
        print "Input is not a string."
        return False

    if len(letters) != 6:
        print "Input must be exactly 6 characters long."
        return False
    
    if not re.match("^[a-zA-Z]+$", letters):
        print "Input does not consist of only upper/lower case letters."
        return False
    return True

solver = WordWhompSolver()
# Main loop.
while 1:
    letters = raw_input("Enter letters for this game of WordWhomp: ").rstrip()
    if (is_valid_input(letters) == False):
        continue
    solver.set_instance(letters)
    solver.solve()
