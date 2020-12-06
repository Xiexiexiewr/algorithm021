#
# @lc app=leetcode.cn id=84 lang=python
#
# [84] 柱状图中最大的矩形
#1.暴力1 
#for i->0,n-2
#   for j->i+1,n-1
#      (i,j)->最小高度，area
#      update maxArea
#2.暴力2
#for i->0,n-1:
#    找到left bound，right bound比它低的左右两个
#     area = height[i]*(right-left)
#     update maxArea
#3.stack
#

# @lc code=start
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
# @lc code=end

