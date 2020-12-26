#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

#1.动规
#2.贪心

#贪心：
# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in range(1, len(prices)):
            # tmp = prices[i] - prices[i-1]
            # if tmp > 0:
            #     profit += tmp
            profit += max(prices[i] - prices[i-1], 0)
        return profit
        
# @lc code=end

