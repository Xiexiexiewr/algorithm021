#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#

# @lc code=start

# 贪心算法：O(n)
# class Solution(object):
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         farmost = 0
#         n = len(nums)
#         for i in range(n):
#             if i <= farmost:
#                 farmost = max(farmost, i + nums[i])
#                 if farmost >= n - 1:
#                     return True
#         return False

# class Solution(object):
#     def canJump(self, nums):
#         if nums == [0]:
#             return True
#         maxDistance = 0
#         for i,jump in enumerate(nums):
#             if maxDistance >= i and i + jump > maxDistance:
#                 maxDistance = i + jump
#                 if maxDistance >= len(nums) - 1:
#                     return True
#         return False

class Solution(object):
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums))[::-1]:
            if i + nums[i] >= goal:
                goal = i
        return not goal
# @lc code=end

