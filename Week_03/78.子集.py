#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

#1.递归
#2.迭代
#3.库函数
# @lc code=start

#2.迭代：
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         result=[[]]

#         # for num in nums:
#         #     newset = []
#         #     for subset in result:
#         #         new_subset = subset + [num]
#         #         newset.append(new_subset)
            
#         #     result.extend(newset)
#         for i in nums:
#             result = result + [[i] + num for num in result]
#             # print result
#         return result

#1.递归：
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res = []
#         n = len(nums)
#         def dfs(index, tmp):
#             res.append(tmp[:])
#             for i in range(index, n):
                # tmp.append(nums[i])
                # dfs(i + 1, tmp)
                # tmp.pop()
#         dfs(0,[])
#         return res
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        def dfs(index, tmp):
            res.append(tmp)
            for i in range(index, n):
                dfs(i + 1, tmp + [nums[i]])
        dfs(0,[])
        return res

#递归模板化：
# class Solution(object):
#     def subsets(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         res, tmp = [], []
#         self.dfs(res, 0, nums, tmp)
#         return res
#     def dfs(self, res, start, nums, tmp):
#          res.append(tmp[:])
#          for i in range(start, len(nums)):
#              tmp.append(nums[i])
#              self.dfs(res, i+1, nums,tmp)
#              tmp.pop()
            


# @lc code=end

