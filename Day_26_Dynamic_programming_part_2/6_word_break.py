'''
######################### word break ####################
Given a string A and a dictionary of n words B, find out if A can be segmented into a space-separated sequence of dictionary words.

Note: From the dictionary B each word can be taken any number of times and in any order.

n = 12
B = { "i", "like", "sam",
"sung", "samsung", "mobile",
"ice","cream", "icecream",
"man", "go", "mango" }
A = "ilike"
Output:
1


gfg : https://practice.geeksforgeeks.org/problems/word-break1352/1

'''


# solution
# approach 1 : recursive
def wordBreak(line, dictionary):

    n = len(line)

    def dp(i, j):
        if i == j:
            return True

        if line[i:j] in dictionary:
            return True

        for k in range(i+1, j+1):
            if line[i:k] in dictionary:
                if dp(k, j):
                    return True

        return False


    return 1 if dp(0, n) else 0