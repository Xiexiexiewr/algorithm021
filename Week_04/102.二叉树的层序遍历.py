#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 1. BFS
# 2. DFS（记录当前是哪一层）
# 3. 迭代---BFS

#DFS
# class Solution(object):
#     def levelOrder(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[List[int]]
#         """
#         if not root:
#             return []
#         res = []
#         def DFS(level, r, res):
#             if len(res) == level:
#                 res.append([])
#             res[level].append(r.val)
#             if r.left:
#                 DFS(level + 1, r.left, res)
#             if r.right:
#                 DFS(level + 1, r.right, res)
#         DFS(0, root, res)
#         return res

#BFS
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
 #               print(tmp)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        return res

# @lc code=end

