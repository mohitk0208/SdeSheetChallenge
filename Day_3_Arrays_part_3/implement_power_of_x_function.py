'''
##################### Implement Power of X Function #####################

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104


leetcode : https://leetcode.com/problems/powx-n/
'''

# leetcode solution
# approach 1 : use brute force and multiply x by x n times
# approach 2:
#     - if n is even, then x = x * x and n = n / 2
#     - if n is odd, then result = result * x and n = n - 1


# time complexity : O(log n)
# space complexity : O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        nn = abs(n)
        while nn > 0:
            if (nn % 2 == 0):
                x *= x
                nn = nn // 2
            else:
                res = res * x
                nn -= 1


        return 1 / res if n < 0 else res

