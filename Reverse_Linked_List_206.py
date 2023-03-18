# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iterative approach , time --> O(n) , memory --> O(1)

        current, prev = head, None
        while current:
            store = current.next
            current.next = prev
            prev = current
            current = store
        return prev 
        
        #recursive approach, time --> O(n), memory --> O(n)

        if head == None:
            return None

        new_head = head
        if head.next:
            new_head = self.reverseList(head.next) # recursion call
            head.next.next = head  # we are comparing two value at once, & head.next is basically the new_head here

        head.next = None
        return new_head