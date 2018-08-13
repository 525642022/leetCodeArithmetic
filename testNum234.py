# 作者 ljc
#
# 请检查一个链表是否为回文链表。
#
# 进阶：
# 你能在 O(n) 的时间和 O(1) 的额外空间中做到吗？
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
             slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        return not rev

    def isPalindrome(self, head):
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev

