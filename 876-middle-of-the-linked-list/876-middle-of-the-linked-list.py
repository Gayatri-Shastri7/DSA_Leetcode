'''
Traverse the Linked List
Find Length of the linked list.
Then do find the middle index

OR 

2 ptr approach.
Fast ptr and slow ptr
When fast ptr reaches the end of the linked list, then the slow ptr will be pointing the middle element
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= head
        fast = head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
        