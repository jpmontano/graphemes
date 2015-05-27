#!/opt/local/bin/python3.4 -tt


def split_into_graphemes(nishchars):
    '''This function splits a string of Nishnaabe characters into its
    respective constituent graphemes. It accepts a string of
    Nishnaabe characters (nishchars) and returns a list of
    graphemes (alreadysplitgraphemes).'''

    # List of possible single-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    singlechargraphemes = [
        "-", "'", "a", "b", "d", "e", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "s", "t", "w", "y", "z"]

    # List of possible two-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    digraphs = [
        "aa", "ch", "ii", "nd", "ng", "nh", "ns", "ny", "oo",
        "sh", "sk", "zh"]

    # List of possible three-letter-graphemes in Pic River's dialect
    # of the Nishnaabe language.
    trigraphs = [
        "nzh", "shk"]

    # Convert the Nishnaabe word to all-lowercase
    nishchars = nishchars.lower()

    # Prepare an empty list to store all of the graphemes of the
    # Nishnaabe word nishcars.
    collectedgraphemes = []
    
    # Calculate teh length (in characters) of the Nishnaabe word
    # which will be iterated through.
    numofnishchars = len(nishchars)

    # Extend the length of the Nishnaabe word to prevent an
    # "IndexError: string index out of range"
    # when we iterate past the last character of the Nishnaabe word,
    # nishchars, in our while-loop. The length of this string being
    # added to nishchars needs to be one character shorter than the
    # length of the longest potential grapheme.
    nishchars += "  "

    # Initialize our counter with which we'll iterate through the
    # characters of the Nishnaabe word nishchars.
    i = 0

    # Iterate through the Nishnaabe expression (i.e., the string
    # of Nishnaabe characters named nishcars) in order to split
    # it into the graphemes of which nishcars consists.
    while (i < numofnishchars):
        
        # From the current counter/pointer with which we're interating
        # through nishcars, create three quick and convenient strings
        # with which to do some querying in the upcoming lines of code.
        queried1char = nishchars[i]
        queried2chars = nishchars[i] + nishchars[i + 1]
        queried3chars = nishchars[i] + nishchars[i + 1] + nishchars[i + 2]

        # Query the list of possible Nishnaabe three-letter-graphemes for
        # the existence of the current three characters from the
        # Nishnaabe word nishchars.
        if queried3chars in trigraphs:
            collectedgraphemes.append(queried3chars)
            i += 3
        
        # Query the list of possible Nishnaabe two-letter-graphemes for
        # the existence of the current two characters from the
        # Nishnaabe word nishchars.
        elif queried2chars in digraphs:
            collectedgraphemes.append(queried2chars)
            i += 2
        
        # Query the list of possible Nishnaabe one-letter-graphemes for
        # the existence of the current one character from the
        # Nishnaabe word nishchars.
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
    
    # Return the constituent split-up graphemes of the Nishnaabe word
    # nishchars.
    return collectedgraphemes




# Begin main processing loop.
#
# A sample list of Nishnaabe expressions to split into graphemes
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
    "wzhashkoons"
]

# Iterate through the sample list of Nishnaabe expressions and split each
# of them into its respective constituent graphemes.
for nishsample in nishsamples:
    print(split_into_graphemes(nishsample))

