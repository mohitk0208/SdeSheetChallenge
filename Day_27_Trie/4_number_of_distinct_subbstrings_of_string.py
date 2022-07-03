'''
###################### Number of Distinct Substrings of String ######################
Given a string 'S', you are supposed to return the number of distinct substrings(including empty substring) of the given string. You should implement the program using a trie.

Sample Input 1 :
aa

Sample Output 1 :
3

Explanation Of Sample Input 2 :
In the first test case, the two distinct substrings are {‘a’, “aa”, “” }.

codestudio : https://www.codingninjas.com/codestudio/problems/count-distinct-substrings_985292?utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_tries_videos&leftPanelTab=0

'''




# solution
# approach 1: Brute Force
def countDistinctSubstrings(s):
    ans = set([""])

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            ans.add(s[i:j])

    return len(ans)


# approach 2: Trie
class Trie:
    def __init__(self):
        self.arr = [None]*26


def countDistinctSubstrings(s):
    count = 0
    root = Trie()

    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            x = ord(s[j]) - 97
            if node.arr[x] == None: # when new Trie is added it means this substring is distinct and count is incremented
                count += 1
                temp = Trie()
                node.arr[x] = temp

            node = node.arr[x]

    return count + 1

