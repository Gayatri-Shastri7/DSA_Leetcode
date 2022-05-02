class Solution:
    def sortArrayByParity(self, A):
        start=0
        end=len(A) - 1
        
        while start <= end:
            if A[start] % 2 == 0:
                start += 1
            else:
                A[start], A[end] = A[end], A[start]
                end -= 1
        return A