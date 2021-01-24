#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        #因为2的幂次方只能会有一个1，所以最低位为1去掉之后，就是全是0
        return n != 0 and (n & (n-1)) == 0
# @lc code=end

