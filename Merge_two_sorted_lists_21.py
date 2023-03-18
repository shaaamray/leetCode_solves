# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()
        head, tail = dummy_node, dummy_node

        while list1 and list2: #until list1 and list2 is None
            if list1.val > list2.val:
                tail.next = list2 #check nodes one by one
                list2 = list2.next
                tail = tail.next
            else:
                tail.next = list1
                list1 = list1.next
                tail = tail.next

        #if any node is remaining, then connect it all        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy_node.next
    
