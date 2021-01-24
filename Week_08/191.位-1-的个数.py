#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#


#1. n = n & (n-1)
# @lc code=start
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         count = 0
#         while n:
#             count += 1
#             n &= n-1
#         return count

#2. bin函数
# class Solution(object):
#     def hammingWeight(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return bin(n).count("1")

#3. 取余
# class Solution(object):
#     def hammingWeight(self, n):
#         count = 0
#         while n:
#             res = n % 2
#             if res == 1:
#                 count += 1
#             n /= 2

#         return count

#4. 清除最低位：
class Solution(object):
    def hammingWeight(self, n):
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count        
# @lc code=end

