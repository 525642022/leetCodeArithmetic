# 作者 ljc
# 给定一个二叉树，返回其节点值自底向上的层次遍历。
# （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, 0, res)
        return res
    def dfs(self, root,level, res):
        if root:
            if len(res) <level+1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)
