class DictionaryPruner():
    
    capitalLetters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', \
                           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', \
                           'U', 'V', 'X', 'Y', 'Z')
    
    trailingChars = '\n%'

    def __init__(self, filename="dictionary.txt", \
                 output="pruned_dictionary.txt"):
        self.filename = filename
        self.output = output

    def prune_dictionary(self):
        """
        Given a file containing strings (preferrably English language words ;) )
        delimited by some character (e.g., '\n', ',', ...), prune_dictionary()
        prunes words not used by WordWhomp and produces a new file
        prunted_dictionary.txt in the current directory.
        """

        # Read the dictionary file into memory.
        try:
            f = open(self.filename)
            wordList = f.readlines()
            f.close()
        except IOError:
            print "Could not open file \"",self.filename,"\""
            exit()
            
        # TODO: handle delimiters other than newlines
        # Could do it as follows:
        # for line in f:
        #   -> split words by delimeter
        #   -> prune words
        #   -> append valid words to running list

        wordList[:] = [word.rstrip(self.trailingChars) for word in wordList if \
                       self.is_dictionary_word(word)]

        try:
            f = open(self.output, 'w')
            for word in wordList:
                f.write(word)
                f.write('\n')
            f.close()
        except IOError:
            print "Could not open file \"",filename,"\" for writing."
            exit()

    def is_dictionary_word(self, word):
        word = word.rstrip(self.trailingChars)
        if (self.is_bad_length(word) == True) or \
           (self.is_proper_noun(word) == True):
            return False
        return True

    def is_bad_length(self, word):
        length = len(word)
        if (length <= 6) and (length >= 3):
            return False
        return True

    def is_proper_noun(self, word):
        if word[0] in self.capitalLetters:
            return True
        return False

filename = raw_input("Please enter the name of dictionary file: ").rstrip()
output = raw_input("Please enter the name of the output file: ").rstrip()
pruner = DictionaryPruner(filename, output)
pruner.prune_dictionary()
