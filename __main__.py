"""
    Main Script to test Trie implementation
"""
from Trie.trie import Trie


def main():
    keys = [
        "the",
        "a",
        "there",
        "answer",
        "any",
        "by",
        "their",
    ]

    t = Trie()

    for key in keys:
        t.insert(key)

    print("Key {} in Trie? {}".format("the", t.search("the")))
    print("Key {} in Trie? {}".format("thy", t.search("thy")))


if __name__ == "__main__":
    main()