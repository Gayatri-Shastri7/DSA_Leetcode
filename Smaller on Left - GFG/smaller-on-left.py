#User function Template for python3

import bisect
def Smallestonleft (arr,  n) : 
   sorted_arr = []
   results = []
   
   for i in range(0,n):
       bisect.insort(sorted_arr, arr[i])
       
       left_index = bisect.bisect_left(sorted_arr, arr[i])
       if left_index == 0:
           results.append(-1)
       else:
           results.append(sorted_arr[left_index-1])    
       
   return results
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    res = Smallestonleft(arr, n);
    for each in res:
        print(each,end=' ')
    print()




# } Driver Code Ends