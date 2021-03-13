"""
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using two pointer, one for l1 ListNode, one for l2 ListNode.
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = dum = ListNode(0)     # cur point to the dumn head.
        while l1 and l2:
            if l1.val < l2.val:     # case 1, l1.val > l2.val
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next          # cur move to next step.
        cur.next = l1 if l1 else l2
        return dum.next