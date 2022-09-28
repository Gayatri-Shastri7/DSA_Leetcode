# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0,head)
        left =dummy
        right = head
        
        while n>0 and right:
            right = right.next
            n-=1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return(dummy.next)
    
        # def index(node):
        #     if not node:
        #         return 0
        #     i = index(node.next) + 1
        #     if i > n:
        #         node.next.val = node.val
        #     return i
        # index(head)
        # return head.next                                                                                       
    
    