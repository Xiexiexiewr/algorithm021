#
# @lc app=leetcode.cn id=190 lang=python
#
# [190] 颠倒二进制位
#


#位运算移位
# @lc code=start
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret, number = 0, 31
        while n:
            ret += (n & 1) << number
            n >>= 1
            number -= 1
        return ret
        
# @lc code=end

