#
# @lc app=leetcode.cn id=32 lang=python
#
# [32] 最长有效括号
#

# @lc code=start
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        for i in range(n):
            if s[i] == ')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + dp[i - dp[i-1]-2] +2
        return max(dp)
# @lc code=end

