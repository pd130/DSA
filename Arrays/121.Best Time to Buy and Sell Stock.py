#Brute Force 
# Time :O(N^2)
# Space : O(N)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = {0 : 1}
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)):
                test = prices[j] - prices[i] 
                if test not in profit:
                    profit[test] = 1
        return max(profit.keys())
#Optimal
#Time : O(N)
#Space : O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 999999
        maximum = 0
        for i in range(len(prices)):
            minimum = min(prices[i] , minimum)
            maximum = max(maximum , prices[i] - minimum)
        return maximum

            

            