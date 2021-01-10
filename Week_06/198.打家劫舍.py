#
# @lc app=leetcode.cn id=198 lang=python
#
# [198] 打家劫舍
#

# a[i][0,1] :  0-i 能偷到 max value
# 0:不偷  1：偷
# DP方程：
    # a[0][0] = 0
    # a[0][1] = nums[0]
    # a[i][0] = max(a[i-1][0],a[i-1][1])
    # a[i][1] = a[i-1][0] + nums[i]

# a[i]: 0-i 全部 能偷盗到max value，第i个房子可偷或不偷
# DP方程：
#   
#   a[i] = max(a[i-1], nums[i] + a[i-2])

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = 0
        now = 0
        for i in nums:
            # dp[i] = max(dp[i-1], nums[i] + dp[i -2])
            pre, now = now, max(pre + i, now)
        return now
# @lc code=end

