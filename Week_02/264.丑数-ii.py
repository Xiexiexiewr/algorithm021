#
# @lc app=leetcode.cn id=264 lang=python
#
# [264] 丑数 II
#

# @lc code=start
# 1.暴力求解 依次循环，计数
# 2.堆
# 3.动态规划
import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = [1]
        heapq.heapify(heap)
        res = 0
        for _ in range(n):
            res = heapq.heappop(heap)
            while heap and res == heap[0]:
                res = heapq.heappop(heap)
            a, b, c = res * 2, res * 3, res * 5
            for t in [a, b, c]:
                heapq.heappush(heap,t)
        return res
# @lc code=end

