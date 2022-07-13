'''
####################### Check for Balanced Parenthesis #######################
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

leetcode : https://leetcode.com/problems/valid-parentheses/

'''

# solution
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(':')',
            '{':'}',
            '[':']'
        }

        for c in s:
            if c in pairs.keys():
                stack.append(c)

            else:
                if len(stack) == 0:
                    return False

                if pairs[stack[-1]] == c:
                    stack.pop()
                    continue
                else:
                    return False

        if len(stack) == 0:
            return True

        return False