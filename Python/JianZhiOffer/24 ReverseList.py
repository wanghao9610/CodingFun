"""定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Use a chain mechanism to reverse the LiseNode.
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:  # if cur is not None
            nxt = cur.next  # store the cur.next node
            cur.next = pre  # link cur.next to previous node
            pre = cur   # update pre with cur
            cur = nxt   # update cur with next
        return pre