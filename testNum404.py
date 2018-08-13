# 作者 ljc

# 计算给定二叉树的所有左叶子之和。
#
# 示例：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root : return 0
        if root.left and not root.left.left and not root.left.rigth:
            return root.left.val + self.sumOfLeftLeaves(root.rigth)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.rigth)

