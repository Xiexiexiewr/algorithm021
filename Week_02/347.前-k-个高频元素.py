#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
from collections import Counter
import heapq as hq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        lookup = Counter(nums)
        res = []
        heap = []
        for num, freq in lookup.items():
            if len(heap) ==k :
                if heap[0][0] < freq:
                    hq.heappop(heap)
                    hq.heappush(heap, (freq,num))
                    # hq.heapreplace(heap,(freq,num))
            else:
                hq.heappush(heap, (freq,num))
        while heap:
            res.append(hq.heappop(heap)[1])
        
        return res
        # count = Counter(nums)
        # count_value = count.values()
        # hp = count_value[:k]
        # heapq.heapify(hp)
        # for i in count_value[k:]:
        #     if i > hp[0]:
        #         heappop(hp)
        #         heappush(hp, i)
        # ans = []
        # for key, value in count.items():
        #     if value >= hp[0]:
        #         ans.append(key)
        # return ans
# @lc code=end

