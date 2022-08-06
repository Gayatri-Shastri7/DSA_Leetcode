# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


'''
This can be done using flast and slow ptr. If the fast ptr goes to null then there is no cycle 
else 
if both fast and slow ptr reaches at same point then there is a cycle
'''


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow=head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
           
        return False

        
        
        
        