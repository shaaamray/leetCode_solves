# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:  # edge case for single node or no node
            return head

        first = head
        second = head.next
        first.next = self.swapPairs(head.next.next)
        second.next = first

        return second  # return swapped adjacent pair
