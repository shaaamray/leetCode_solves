# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we have two linked list here

        #pointer assign
        dummy_node = ListNode()
        current = dummy_node

        carry = 0
        while l1 or l2 or carry:
            if l1:
                l1_digit = l1.val
            else:
                l1_digit = 0

            if l2:
                l2_digit = l2.val
            else:
                l2_digit = 0

            value = l1_digit + l2_digit + carry
            carry = value // 10 # mod value
            value = value % 10 # remainder value

            current.next = ListNode(value)

            # update pointers
            current = current.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None

        return dummy_node.next