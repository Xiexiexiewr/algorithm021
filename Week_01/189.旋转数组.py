#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#
# 1.暴力求解 三个指针    时间：O(n*k) 空间：O(1)
# 2.拷贝到新数组         时间：O(n) 空间：O(n)
# 3.python切片          时间：O(n) 空间：O(n)
# 4.三次反转（1.整体2.前半段3.后半段    时间：O(n) 空间：O(1)

# @lc code=start

#1.暴力求解：超时
# class Solution(object):
#     def rotate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for i in range(k):
#             pre = nums[len(nums)-1]
#             for j in range(len(nums)):
#                 t = nums[j]
#                 nums[j] = pre
#                 pre = t
#         return nums

# 3.切片
# class Solution(object):
#     def rotate(self, nums, k):
#         k = k % len(nums)--->k %= len(nums)
#         nums[:] = nums[-k:]+nums[:-k]
#         return nums

# 4.三次反转：
class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        return nums 

# @lc code=end

