# 作者 ljc

# 反转一个单链表。
#
# 进阶:
# 链表可以迭代或递归地反转。你能否两个都实现一遍？
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return  prev