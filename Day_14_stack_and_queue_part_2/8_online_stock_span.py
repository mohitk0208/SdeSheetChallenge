'''
################# Online Stock Span ###############################
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the stock price was less than or equal to today's price.

For example, if the price of a stock over the next 7 days were [100,80,60,70,60,75,85], then the stock spans would be [1,1,1,2,1,4,6].
Implement the StockSpanner class:

StockSpanner() Initializes the object of the class.
int next(int price) Returns the span of the stock's price given that today's price is price.


leetcode : https://leetcode.com/problems/online-stock-span/

'''



# solution

# SC -> O(n)
class StockSpanner:

    def __init__(self):
        self.stack = []
        self.curr_idx = 0


    def next(self, price: int) -> int:
        ans = 1
        if len(self.stack) == 0:
            ans = 1

        elif self.stack[-1][0] > price:
            ans = self.curr_idx - self.stack[-1][1]

        else:
            while len(self.stack) > 0 and self.stack[-1][0] <= price:
                self.stack.pop()

            if len(self.stack) == 0 :
                ans = self.curr_idx + 1
            else:
                ans = self.curr_idx - self.stack[-1][1]

        self.stack.append((price, self.curr_idx))
        self.curr_idx += 1

        return ans