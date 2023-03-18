# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        current, prev = head, ListNode(None)

        while current:
            if current.val == val:
                if current == head:
                    head = head.next
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return head