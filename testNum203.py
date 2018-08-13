# 作者 ljc

# 删除链表中等于给定值 val 的所有元素。
# 示例
# 给定: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
# 返回: 1 --> 2 --> 3 --> 4 --> 5
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        next = dummy

        while next != None and next.next != None:
            if next.next.val == val:
                next.next = next.next.next
            else:
                next = next.next

            return dummy.next
