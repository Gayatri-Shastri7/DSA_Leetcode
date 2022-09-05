class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        i = 0
		
		
        while i < len(a):
            c = a[i]-1
			#  Conditions
            if a[i]<len(a) and a[i]>0 and a[i]!=a[c]:
                a[i],a[c]=a[c],a[i]
            else:
                i+=1
                
                
        for i in range(len(a)):
            if i+1 != a[i]:
                return i+1
		
        return len(a)+1

