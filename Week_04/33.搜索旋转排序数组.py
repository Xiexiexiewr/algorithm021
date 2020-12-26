#
# @lc app=leetcode.cn id=33 lang=python
#
# [33] 搜索旋转排序数组
#


#1.暴力：还原O(n) / O(logN)-》升序-》二分：O(logN)   写还原logn的总结
#2.正解：二分查找
# ！a.单调 左半部分和中间的关系（左边如是单调递增，则在左边找，否则右边）
# b.边界
# c.index
# @lc code=start
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
# @lc code=end

