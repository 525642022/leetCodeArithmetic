# 作者 ljc
# 给定两个二叉树，写一个函数来检查它们是否相同。
# 如果两棵树在结构上相同并且节点具有相同的值，则认为它们是相同的。
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(q.right, q.right)
        return p is q
