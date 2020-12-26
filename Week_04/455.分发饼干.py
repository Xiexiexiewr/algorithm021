#
# @lc app=leetcode.cn id=455 lang=python
#
# [455] 分发饼干
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        j = 0
        i = 0
        while j < len(g) and i < len(s):
            if s[i] >= g[j]:
                j += 1
            i += 1
            
        # for i in range(len(s)):
        #     if s[i] >= g[j]:
        #         j += 1
        #     if j == len(g):
        #         return j
        return j
# @lc code=end

