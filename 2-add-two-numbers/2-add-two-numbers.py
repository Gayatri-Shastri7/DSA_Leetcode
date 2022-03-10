# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0)
        head = node
        carry = 0
        val = 0
        while( l1 or l2 ):
            tmp = ListNode(0)
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = (v1 + v2 + carry) % 10  
            carry = (v1 + v2 + carry) // 10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next      
            tmp.val = val
            node.next = tmp
            node = node.next
        if(carry > 0):
            tmp = ListNode(carry) 
            node.next = tmp
            node = node.next            
        return head.next;        