"""
    Module used to define Trie Data Structure
"""
import string


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = [None for _ in range(len(string.ascii_lowercase))]
        self.weight = -1
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        """
            Default Constructor
        """
        self.root = self.get_node()
        self.word_list = []


    def get_node(self):
        """
            Method used to get a new trie node
        """
        return TrieNode()


    def char_to_index(self, ch):
        """
            Method to change a character to an integer index
            value
        """
        return ord(ch) - ord('a')


    def insert(self, key, weight):
        """
            Method used to insert a new key to an existing trie

            Parameters
            ----------
            key: str
                key we would like to insert into trie

            Returns
            -------
            None
        """
        trie_crawl = self.root
        length = len(key)

        for level in range(length):
            index = self.char_to_index(key[level])

            if level == length - 1:
                # make sure to add the weight of the word
                if not trie_crawl.children[index]:
                    trie_crawl.children[index] = self.get_node()
                    trie_crawl.children[index].val = key[level]
                    trie_crawl.children[index].weight = weight

            else:
                # we are still iterating through the word
                if not trie_crawl.children[index]:
                    trie_crawl.children[index] = self.get_node()
                    trie_crawl.children[index].val = key[level]

            trie_crawl = trie_crawl.children[index]

        trie_crawl.is_end_of_word = True


    def search(self, key):
        """
            Method used to search a key on an existing trie

            Parameters
            ---------
            key: str
                a word we are searching for in the trie
                e.g., key = michael

            Returns
            -------
            None: boolean
                True if key exists in trie and is a word,
                False otherwise
        """
        trie_crawl = self.root
        length = len(key)

        for level in range(length):
            index = self.char_to_index(key[level])

            if not trie_crawl.children[index]:
                return False
            else:
                trie_crawl = trie_crawl.children[index]

        # Returns true of key exists and is an end of a word
        return (trie_crawl != None) and (trie_crawl.is_end_of_word)


    def suggestions_record(self, node, word):
        """
            Method to recursively traverse trie
            and return a whole words
        """
        if node.is_end_of_word:
            self.word_list.append(word)

        for i in range(len(node.children)):
            if node.children[i]:
                self.suggestions_record(node.children[i], word + node.children[i].val)



    def print_suggestions(self, key):
        """
            Method used to return all the words in the trie
            whose common prefix is the given key thus listing
            all suggestions for autocomplete
        """
        node = self.root
        length = len(key)
        not_found = False
        temp_word = ""

        for level in range(length):
            index = self.char_to_index(key[level])

            if not node.children[index]:
                not_found = True
                break

            temp_word += key[level]
            node = node.children[index]

        if not_found:
            return 0
        elif node.is_end_of_word:
            return -1

        self.suggestions_record(node, temp_word)

        for s in self.word_list:
            print(s)
        return 1
