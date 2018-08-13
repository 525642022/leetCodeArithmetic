# 作者 ljc
# 给定一个二叉树，返回从根节点到叶节点的所有路径。
#
# 例如，给定以下二叉树:
#
#    1
#  /   \
# 2     3
#  \
#   5
# 所有根到叶路径是:
#
# ["1->2->5", "1->3"]

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res, stack = [], [(root, "")]
        while stack:
            node, ls = stack.pop()
            if not node.left and node.right:
                res.append(ls + str(node.val))
            if node.right:
                stack.append((node.right, ls + str(node.val) + '-->'))
            if node.left:
                stack.append((node.left, ls + str(node.val) + '-->'))
            return res
# dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res