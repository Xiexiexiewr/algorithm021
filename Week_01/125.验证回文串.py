#
# @lc app=leetcode.cn id=125 lang=python
#
# [125] 验证回文串
#

# @lc code=start
import re
class Solution(object):
    def isPalindrome(self, s):
        """
        高层次（主干）逻辑
        1. 去除非字母和非数字
        2. reverse并和原字符串比较
        """
        filteredS = self.filterNonNumberAndChar(s)
        print(filteredS,self.reverseString(filteredS))
        if self.reverseString(filteredS) == filteredS:
            return True
        else :
            return False

    def filterNonNumberAndChar(self, s):
        s = re.sub('[^A-Za-z0-9]', '', s)
        s = s.lower()
        return s

    def reverseString(self, filteredS):
        return filteredS[::-1]


# @lc code=end

