#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#递归
# 时间复杂度：O(n),n为节点数，访问每个节点恰好一次
# 空间复杂度：O(h)，h为树的得高度，最坏O(n)，平均O(logn)
# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         def inTraversal(cur):
#             if not cur:
#                 return
#             inTraversal(cur.left)
#             res.append(cur.val)   
#             inTraversal(cur.right)    
#         res = []
#         inTraversal(root)
#         return res

#用栈来实现
# 时间复杂度：O(n),n为节点数，访问每个节点恰好一次
# 空间复杂度：O(n)
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: TreeNode
#         :rtype: List[int]
#         """
#         stack = []
#         res = []
#         cur = root
#         while stack or cur:
#             while cur:
#                 stack.append(cur)
#                 cur = cur.left
#             cur = stack.pop()
#             res.append(cur.val)
#             cur = cur.right
#         return res

# @lc code=end

