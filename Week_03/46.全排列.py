#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def recursion(index, nums, res):
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                print(nums)
                recursion(index + 1, nums, res)
                nums[index], nums[i] = nums[i], nums[index]
                print('after', nums)
        recursion(0, nums, res)
        return res
# @lc code=end

