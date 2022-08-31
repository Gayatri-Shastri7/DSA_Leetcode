# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return head
        l=[]
        ptr= head
        while(head):
            l.append(head.val)
            head = head.next
        ln=len(l)
        k=k%ln
        print(l[-k:])
        print(l[:-k])
        l = l[-k:]+l[:-k]


        res= None
        for i in l[::-1]:
            res=ListNode(i,res)

        return res
            
