#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#


#1.二分查找
# y = x……2
#2.牛顿迭代法
# @lc code=start

#牛顿迭代法：
# class Solution(object):
#     def mySqrt(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         r = x
#         while r*r > x :
#             r = (r + x/r) / 2
#         return r

#二分法:
class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x // 2 + 1
        while left < right:
            #一定要取右中位数
            # mid = left + (right - left) //2
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid
        return left
# @lc code=end

