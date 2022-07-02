'''
########################### Implement trie (Prefix tree) ###########################
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() -> Initializes the trie object.
void insert(String word) ->  Inserts the string word into the trie.
boolean search(String word) ->  Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) ->  Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

leetcode : https://leetcode.com/problems/implement-trie-prefix-tree/

'''

# explanation



# solution
class Trie:

    def __init__(self):
        self.arr = [None]*26
        self.flag = False

    # SC -> O(1) and TC -> O(N)
    def insert(self, word: str) -> None:
        curr = self
        for c in word:
            i = ord(c)-97
            if curr.arr[i] == None:
                temp = Trie()
                curr.arr[i] = temp

            curr = curr.arr[i]

        curr.flag = True


    # SC -> O(1) and TC -> O(N)
    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            i = ord(c)-97
            if curr.arr[i] == None:
                return False

            curr = curr.arr[i]

        return curr.flag


    # SC -> O(1) and TC -> O(N)
    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            i = ord(c)-97
            if curr.arr[i] == None:
                return False

            curr = curr.arr[i]

        return True
