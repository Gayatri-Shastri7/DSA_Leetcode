'''
1. This is solved using Dynamic Programming
2. We will be using Matrix  Chain multiplication 
3. If it's palindrome, then return zero
4. Else, run for loops(i,j,k)
5. After running the for loops; then 
6. Store the result in temp answers 
7. Afterwards return temp1+temp2+1
8. Pickup min(res,tempres)
9. Return the answer

'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        def solve(ip,op):
            if len(ip)==0:
                res.append(op[:])
                return

            size=len(ip)
            for i in range(size):
                temp=ip[:i+1]
                if temp==temp[::-1]:
                    op1=op
                    op1.append(temp)
                    solve(ip[i+1:],op1)
                    op1.pop()

        solve(s,[])
        return res