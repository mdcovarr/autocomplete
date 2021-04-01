"""
    Main Script to test Trie implementation
"""
import os
from Trie.trie import Trie

CWD = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = "baby-names.txt"



def main():
    """
     1. Get input data
    """
    t = Trie()
    array = []

    filename = os.path.join(CWD, "data", INPUT_FILE)

    with open(filename, "r") as f:
        first = True
        for line in f.readlines():
            if first:
                first = False
                continue

            line = line.lstrip().rstrip()
            weight, key = line.split("\t")
            t.insert(key.lower(), int(weight))
            array.append([key.lower(), weight])

    """
        Sort the array alphabetically
    """
    array = sorted(array, key = lambda x:x[0])


if __name__ == "__main__":
    main()