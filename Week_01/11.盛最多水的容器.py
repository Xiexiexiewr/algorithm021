# 枚举 ： i，j 两层循环 迭代 O(n^2)
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         maxArea = 0
#         for i in range(len(height)):
#             j = i + 1
#             for j in range(len(height)):
#                 area = (j - i) * min(height[i], height[j]) 
#                 maxArea = max(maxArea,area)
#         return maxArea
    
# O（n）左右边界i,j 向中间收敛，左右夹逼
class Solution(object):
    def maxArea(self, height):   
        maxArea = 0
        j = len(height) - 1
        i = 0
        while(i < j):
            # area = (j - i) * min(height[i], height[j])
            # maxArea = max(maxArea, area)
            # if height[i] < height[j]:
            #     i = i + 1
            # else:
            #     j = j - 1
            if height[i] < height[j]:
                minHeight = height[i]
                i = i + 1
            else:
                minHeight = height[j]
                j = j - 1
            area = (j - i + 1 ) * minHeight
            maxArea = max(maxArea, area)
        return maxArea
