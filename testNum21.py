# 作者 ljc
#
# 合并两个已排序的链表，并将其作为一个新列表返回。新列表应该通过拼接前两个列表的节点来完成。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 思路 1.是否可以单独的去开辟一块新的空间去存储最终的结果
#      是 新建存贮空间并存贮 否 则使用l1或l2去存贮并使用递归
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # dummy = cur  =ListNode(0)
        # while l1 and l2:
        #     if l1.val<l2.val:
        #         cur.next = l1
        #         l1 = l1.next
        #     else:
        #         cur.next = l2
        #         l2 = l2.next
        #     cur = cur.next
        # cur.next = l1 or l2
        # return dummy.next
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


