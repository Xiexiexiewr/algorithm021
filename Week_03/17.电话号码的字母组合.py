#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def search(s, digits, i, res, digitMap):
            #terminate
            if i == len(digits):
                res.append(s)
                return
            
            #process 
            digit = digits[i]
            for j in digitMap[digit]:
                search(s + j, digits, i + 1, res, digitMap)

        search('', digits, 0, res, phoneMap)
        return res

            
# @lc code=end

