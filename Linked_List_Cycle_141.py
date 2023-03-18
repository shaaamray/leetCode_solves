# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #using floyd's tortoise and hare algorithm
        slw_pointer, fst_pointer = head, head

        while fst_pointer and fst_pointer.next:
            slw_pointer = slw_pointer.next
            fst_pointer = fst_pointer.next.next

            if slw_pointer == fst_pointer:
                return True

        return False