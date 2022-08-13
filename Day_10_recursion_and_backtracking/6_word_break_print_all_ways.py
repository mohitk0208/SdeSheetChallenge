'''
################ Word Break (Print all ways ) ###############
You are given a non-empty string S containing no spaces’ and a dictionary of non-empty strings (say the list of words). You are supposed to construct and return all possible sentences after adding spaces in the originally given string ‘S’, such that each word in a sentence exists in the given dictionary.


codestudio : https://www.codingninjas.com/codestudio/problems/983635?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0

'''


# solution
# approach 1 : recursion
def wordBreak(s, dictionary):

    ans = []

    def dp(i, j, curr):
        if i >= j:
            ans.append(" ".join(curr))
            return

        for k in range(i+1, j+1):
            if s[i:k] in dictionary:
                curr.append(s[i:k])
                dp(k, j, curr)
                curr.pop()

    dp(0, len(s), [])

    return ans