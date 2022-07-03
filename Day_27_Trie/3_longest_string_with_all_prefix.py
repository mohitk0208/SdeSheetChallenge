'''
################### Longest string with all prefix ###################
Ninja developed a love for arrays and strings so this time his teacher gave him an array of strings, ‘A’ of size ‘N’. Each element of this array is a string. The teacher taught Ninja about prefixes in the past, so he wants to test his knowledge.

A string is called a complete string if every prefix of this string is also present in the array ‘A’. Ninja is challenged to find the longest complete string in the array ‘A’.If there are multiple strings with the same length, return the lexicographically smallest one and if no string exists, return "None".


codestudio : https://www.codingninjas.com/codestudio/problems/complete-string_2687860?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

'''

# solution
# this is a Trie implementation
class Trie:
    def __init__(self):
        self.arr = [None]*26
        self.flag = False

    def insert(self, word):
        curr = self
        for c in word:
            i = ord(c) - 97

            if curr.arr[i] == None:
                temp = Trie()
                curr.arr[i] = temp

            curr = curr.arr[i]

        curr.flag = True

    # SC -> O(1) and TC -> O(N) , N = len(word)
    # approach :
    #     - for every prefix check if the flag is True, True means a word exists with this prefix
    #     - if for any prefix the flag is False, return False
    #     - if for all prefixes the flag is True, return True
    def isComplete(self, word):
        curr = self

        for c in word:
            i = ord(c) - 97

            if curr.arr[i] == None:
                return False

            curr = curr.arr[i]
            if not curr.flag:
                return False

        return True



def completeString(n: int, a: List[str])-> str:

    ans = [0, None]
    t = Trie()

    for word in a:                      # insert all words in the Trie
        t.insert(word)

    for word in a:
        if t.isComplete(word):        # check if the word is complete
            if len(word) == ans[0]:   # if length is same, choose lexicographically smallest
                if word < ans[1]:
                    ans[1] = word
            elif len(word) > ans[0]:  # if length is greater, choose the word
                ans[0] = len(word)
                ans[1] = word

    return ans[1]                   # return the longest complete string
