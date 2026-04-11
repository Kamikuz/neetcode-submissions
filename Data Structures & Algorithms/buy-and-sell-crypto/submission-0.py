class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res =  0
        buy = 0

        for cur in range(len(prices)):
            if prices[cur] < prices[buy]:
                buy = cur
            else:
                res = max(prices[cur] - prices[buy],res)

        return res