'''
################### Implement Trie (prefix tree) ######################
1) Trie(): Ninja has to initialize the object of this “TRIE” data structure.

2) insert(“WORD”): Ninja has to insert the string “WORD”  into this “TRIE” data structure.

3) countWordsEqualTo(“WORD”): Ninja has to return how many times this “WORD” is present in this “TRIE”.

4) countWordsStartingWith(“PREFIX”): Ninjas have to return how many words are there in this “TRIE” that have the string “PREFIX” as a prefix.

5) erase(“WORD”): Ninja has to delete one occurrence of the string “WORD” from the “TRIE”.

Note:
1. If erase(“WORD”) function is called then it is guaranteed that the “WORD” is present in the “TRIE”.

2. If you are going to use variables with dynamic memory allocation then you need to release the memory associated with them at the end of your solution.


codestudio : https://www.codingninjas.com/codestudio/problems/implement-trie_1387095?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

'''

# solution
class Trie:
    def __init__(self):
        self.arr = [None]*26
        self.ew = 0
        self.cp = 0

    # SC -> O(1) and TC -> O(N), N = len(word)
    def insert(self, word):
        curr  = self

        for c in word :
            i = ord(c) - 97

            if curr.arr[i] == None:
                temp = Trie()
                curr.arr[i] = temp

            curr = curr.arr[i]
            curr.cp += 1

        curr.ew += 1

    # SC -> O(1) and TC -> O(N), N = len(word)
    def countWordsEqualTo(self, word):

        curr = self

        for c in word:
            i = ord(c) - 97

            if curr.arr[i] == None:
                return 0

            curr = curr.arr[i]

        return curr.ew


    # SC -> O(1) and TC -> O(N), N = len(word)
    def countWordsStartingWith(self, word):

        curr = self

        for c in word:
            i = ord(c) - 97

            if curr.arr[i] == None:
                return 0

            curr = curr.arr[i]

        return curr.cp

    # SC -> O(1) and TC -> O(N), N = len(word)
    def erase(self, word):
        curr = self

        for c in word:
            i = ord(c) - 97

            if curr.arr[i] == None:
                return

            curr = curr.arr[i]
            curr.cp -=1

        curr.ew -= 1