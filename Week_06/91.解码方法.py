#
# @lc app=leetcode.cn id=91 lang=python
#
# [91] 解码方法
#

# @lc code=start
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.startswith('0'):  #以‘0’开头直接返回
            return 0
         
        n = len(s)
        dp = [1] * (n + 1)  # 用1初始化

        for i in range(2, n + 1):
            if s[i-1] == '0' and s[i-2] not in '12': # 除了10/20 其余前导为0的直接返回
                return 0
            if s[i-2:i] in ['10', '20']: # 只有10，20才能返回 dp[i] = dp[i-2]
                dp[i] = dp[i-2]
            elif '10' < s[i-2:i] <= '26': #这个范围内有两种解码方式
                dp[i] = dp[i-1] + dp[i-2]
            else:                          # ‘01’至‘09’ 或 > '26'  只有单独解码
                dp[i] = dp[i-1]
        return dp[n]

# @lc code=end

