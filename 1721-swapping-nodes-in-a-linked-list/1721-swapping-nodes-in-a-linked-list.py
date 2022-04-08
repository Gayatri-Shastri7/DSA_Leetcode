# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    
        count = 0
        headCopy = head

        #N = total nodes in linked list
        #O(N) time
        while head!=None:
            count += 1
            head = head.next

        last = count - k + 1
        count = 0
        head = headCopy

        #O(N) time
        while head!=None:
            count+=1
            if count == k:
                start = head
            if count == last:
                end = head

            head = head.next

        start.val,end.val = end.val,start.val
        return headCopy