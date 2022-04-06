"""Generate Markov text from text files."""

from email import contentmanager
from itertools import chain
from random import choice



def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    
    words = text_string.split()
    words.append(None)
    # print(words)
    for i in range(len(words) - 2):
        # put i and i+1 into a tuple, and use as a key in dictionary
        new_tuple = (words[i], words[i + 1]) #key
        #assign word at i+2 to be value to key
        #Key = value
        # chains[new_tuple] = words[i+2]

        #if key is in dictionary
        if new_tuple in chains.keys():
            #append new word to list of values
            chains[new_tuple].append(words[i+2])
        #otherwise (key is not yet in dictionary and no list exists yet)
        else:
            #initialize a list and append word to list
            values_list = []
            values_list.append(words[i + 2])
            #key = value
            chains[new_tuple] = values_list
    return chains


def make_text(chains):
    """Return text from chains."""
    
    words = []
    # Randomly choose a tuple of key 
    random_key = choice(list(chains.keys()))
    print(random_key, 'random_key')
    words = [random_key[0], random_key[1]]
    print(words, 'words')
    random_word = choice(chains[random_key])
    print(random_word, 'Random Word')

    # Step 3 as instruction
    while random_word is not None:
        # Step 1 as instruction
        random_key = (random_key[1], random_word)
        words.append(random_word)
        # Step 2 as instruction
        random_word = choice(chains[random_key])

    return ' '.join(words)


input_path = 'green-eggs.txt'
# input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
