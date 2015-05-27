#!/opt/local/bin/python3.4 -tt


def split_into_graphemes(nishchars):
    '''This function splits a Nishnaabe word into its
    respective constituent graphemes. It accepts a string of
    Nishnaabe characters (nishchars) and returns a list of
    graphemes (collectedgraphemes).'''

    # List of possible single-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    singlechargraphemes = [
        "-", "'", "a", "b", "d", "e", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "s", "t", "w", "y", "z"]

    # List of possible two-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    digraphs = [
        "aa", "ch", "ii", "nd", "ng", "nh", "nj", "ns", "ny",
        "oo", "sh", "sk", "zh"]

    # List of possible three-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    trigraphs = [
        "nzh", "shk"]

    # Convert the Nishnaabe word, nishchars, to all-lowercase
    nishchars = nishchars.lower()

    # Prepare an empty list to store all of the graphemes of the
    # Nishnaabe word nishchars.
    collectedgraphemes = []
    
    # Calculate the length (in characters) of the Nishnaabe word
    # which will be iterated through.
    numofnishchars = len(nishchars)

    # Extend the length of Nishnaabe word nishchars to prevent an
    # "IndexError: string index out of range"
    # when we iterate past the last character of the Nishnaabe word in
    # our while-loop. This nonsense string needs to have a length at
    # least as large as one character shorter than the length of the
    # longest possible grapheme. (Since the longest possible grapheme is
    # currently three characters, we add one less than three characters
    # to the end of nishchars.) The characters which make up this
    # nonsense string need to be characters which are not possible
    # occurrences within the Nishnaabe orthography of Pic River's dialect.
    nishchars += "qq"

    # Initialize our counter with which we'll iterate through the
    # characters of the Nishnaabe word nishchars.
    i = 0

    # Iterate through the Nishnaabe word, nishchars, in order to split
    # it into the graphemes of which nishchars consists.
    while (i < numofnishchars):
        
        # From the current counter, i, with which we're interating
        # through nishchars, we create three quick and convenient strings
        # with which to do some querying in the upcoming lines of code.
        queried1char = nishchars[i]
        queried2chars = nishchars[i] + nishchars[i + 1]
        queried3chars = nishchars[i] + nishchars[i + 1] + nishchars[i + 2]

        # Query the list of possible Nishnaabe three-letter-graphemes for
        # the existence of the currently-pointed-to three-character-sequence
        # within the Nishnaabe word nishchars. If the three-character-
        # sequence is found in the trigraphs list, then we add that
        # three-character-sequence to our collectedgraphemes list.
        if queried3chars in trigraphs:
            collectedgraphemes.append(queried3chars)
            i += 3
        
        # Query the list of possible Nishnaabe two-letter-graphemes for
        # the existence of the currently-pointed-to two-character-sequence
        # within the Nishnaabe word nishchars. If the two-character-
        # sequence is found in the digraphs list, then we add that
        # two-character-sequence to our collectedgraphemes list.
        elif queried2chars in digraphs:
            collectedgraphemes.append(queried2chars)
            i += 2
        
        # Query the list of possible Nishnaabe one-letter-graphemes for
        # the existence of the currently-pointed-to one-character-sequence
        # within the Nishnaabe word nishchars. If the one-character-
        # sequence is found in the singlechargraphemes list, then we add
        # that one-character-sequence to our collectedgraphemes list.
        elif queried1char in singlechargraphemes:
            collectedgraphemes.append(queried1char)
            i += 1
        
        # Alert user of an unrecognizable character within the Nishnaabe
        # word currently being worked on.
        else:
            print('I am unable to recognize the following character:')
            print('"' + str(nishchars[i]) + '"')
            print('at position #' + str(i + 1))
            print('in the word: "' + nishchars)
            break
    
    # Return, as list collectedgraphemes, the constituent split-up
    # graphemes of the Nishnaabe word nishchars.
    return collectedgraphemes




##############################
# Begin main processing loop.
##############################

# A sample list of Nishnaabe words to split into graphemes
nishsamples = [
    "nishnaabe",
    "boozhoo",
    "aaniin",
    "waabndaan",
    "en'goons",
    "biiwaan'goonh",
    "gnoon'diwag",
    "gaa-gii-ni-zhaang",
    "endgwen",
    "gzaaghin",
    "wzhashk",
    "wzhashkoons",
    "aanjtoon"
]

# Iterate through the sample list of Nishnaabe words and split each
# Nishnaabe word into its respective constituent graphemes.
for nishsample in nishsamples:
    print(split_into_graphemes(nishsample))
