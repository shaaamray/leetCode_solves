# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first need to find the start node of the second half
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # now need to reverse the second half of the list
        start = slow.next
        slow.next = None  # breaking the list into two half
        prev = None

        while start:
            # using two pointers start and prev
            store = start.next
            start.next = prev
            prev = start
            start = store

        head1, head2 = head, prev
        # now merging two lists
        while head2:
            s1, s2 = head1.next, head2.next
            head1.next = head2
            head2.next = s1
            head1 = s1
            head2 = s2
