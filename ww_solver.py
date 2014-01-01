# TODO: DictionaryPruner class so that you don't have globals hanging around.


capitalLetters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', \
                  'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', \
                  'Z')
curseWords = ("ass", "fuck", "shit", "cunt", "whore", "nigger")

trailingChars = '\n%'

def prune_dictionary(filename="test_dictionary.txt", \
                     output="pruned_dictionary.txt"):
    """
    Given a file containing strings (preferrably English language words ;) )
    delimited by some character (e.g., '\n', ',', ...), prune_dictionary()
    prunes words not used by WordWhomp and produces a new file
    prunted_dictionary.txt in the current directory.
    """

    # Read the dictionary file into memory.
    try:
        f = open(filename)
        wordList = f.readlines()
        f.close()
    except IOError:
        print "Could not open file \"",filename,"\""
        exit()
        
    # TODO: handle delimiters other than newlines
    # Could do it as follows:
    # for line in f:
    #   -> split words by delimeter
    #   -> prune words
    #   -> append valid words to running list

    wordList[:] = [word.rstrip(trailingChars) for word in wordList if \
                   is_dictionary_word(word)]

    try:
        f = open(output, 'w')
        for word in wordList:
            f.write(word)
            f.write('\n')
        f.close()
    except IOError:
        print "Could not open file \"",filename,"\" for writing."
        exit()

def is_dictionary_word(word):
    global trailingChars
    word = word.rstrip(trailingChars)
    if (is_bad_length(word) == True) or \
       (is_proper_noun(word) == True) or \
       (contains_curse(word) == True):
        return False
    return True

def is_bad_length(word):
    length = len(word)
    if (length <= 6) and (length >= 2):
        return False
    return True

def is_proper_noun(word):
    global capitalLetters
    if word[0] in capitalLetters:
        return True
    return False

def contains_curse(word):
    global curseWords
    for curse in curseWords:
        if curse in word:
            return True
    return False

filename = raw_input("Please enter the name of dictionary file: ").rstrip()
prune_dictionary(filename)
