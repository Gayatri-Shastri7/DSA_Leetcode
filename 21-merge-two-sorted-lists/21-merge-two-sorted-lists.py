# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if l1==None:
        #     return l2
        # if l2==None:
        #     return l1
        # if(l1.val>l2.val):
        #     tmp = l1
        #     l1=l2
        #     l2=tmp
        # res = l1
        # while(l1 !=None and l2 !=None):
        #     tmp = None
        #     while(l1 != None and l1.val <= l2.val):
        #         tmp=l1
        #         l1 = l1.next
        #     temp = l1
        #     l1 = l2
        #     l2 = temp
        # return res

        res = ListNode()
        p = res
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return res.next
        