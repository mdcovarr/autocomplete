"""
    Main Script to test Trie implementation
"""
import os
from math import ceil, log2
from Trie.trie import Trie

CWD = os.path.dirname(os.path.realpath(__file__))
INPUT_FILE = "baby-names.txt"


def get_mid(s, e):
    return s + (e - s) // 2


def construct_st_util(arr, ss, se, st, si):
    """
        Recursive helper function used to
        construct the Segment Tree
    """
    if (ss == se):
        st[si] = arr[ss]
        return arr[ss]

    # Get mid point
    mid = get_mid(ss, se)

    left_max = construct_st_util(arr, ss, mid, st, si * 2 + 1)
    right_max = construct_st_util(arr, mid + 1, se, st, si * 2 + 2)

    if left_max[1] > right_max[1]:
        st[si] = left_max
    else:
        st[si] = right_max

    return st[si]


def construct_st(arr, n):
    """
        Method used to construct a segment tree
    """
    # Height of segment tree
    x = (int)(ceil(log2(n)))
    # Maximum size of segment tree
    max_size = 2 * (int)(2 ** x) - 1
    # Allocate memory
    st = [None] * max_size
    # Fill the allocated memory st
    construct_st_util(arr, 0, n - 1, st, 0)

    return st

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
            array.append([key.lower(), int(weight)])

    """
        Sort the array alphabetically
    """
    array = sorted(array, key = lambda x:x[0])
    n = len(array)

    st = construct_st(array, n)
    print(st[0])


if __name__ == "__main__":
    main()