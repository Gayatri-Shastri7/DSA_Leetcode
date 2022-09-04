class Solution:      
    def trap(self, height: List[int]) -> int:
        left_sum=0
        right_sum=0
        total_sum=0
        current_height_left=0
        current_height_right=0
        max_height=0
        for i in range (len(height)):
            
            ###Find the sum from left:
            current_height_left=max(height[i],current_height_left)
            left_sum+=current_height_left
            
            ###Find the sum from right:
            current_height_right=max(height[-(i+1)], current_height_right)
            right_sum+=current_height_right
            
            ###Find the highest block
            max_height=max(max_height,height[i])
            
            ###Substract the height of the blocks once 
            total_sum+=height[i]
        
        return (left_sum+right_sum-total_sum-len(height)*max_height)
            
        
        '''
        maxLeft = 0
        maxRight = 0
        ans = 0
        indLeft,indRight = 0,len(height)-1
        while indLeft<indRight:
            if height[indLeft]<height[indRight]:
                if height[indLeft]>maxLeft:
                    maxLeft = height[indLeft]
                ans+=(maxLeft-height[indLeft])
                indLeft+=1
            else:
                if height[indRight]>maxRight:
                    maxRight = height[indRight]
                ans+=(maxRight-height[indRight])
                indRight-=1
        return ans
                        
        
        '''

        
        '''
        stack  = []
        ans = 0
        for ind in range(len(height)):
            while stack and height[ind]>height[stack[-1]]:
                top = stack.pop()
                if len(stack)==0:
                    break
                dist = ind-stack[-1]-1
                ans+=((min(height[ind],height[stack[-1]])-height[top])*dist) 
            stack.append(ind)
        return ans        
        
        '''

        '''
         ans = 0
        
        #using two pointers i and j on indices 1 and n-1
        i = 1
        j = len(height) - 1
        
        #initialising leftmax to the leftmost bar and rightmax to the rightmost bar
        lmax = height[0]
        rmax = height[-1]
        
        while i <=j:
            # check lmax and rmax for current i, j positions
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]
            
            #fill water upto lmax level for index i and move i to the right
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
				
            #fill water upto rmax level for index j and move j to the left
            else:
                ans += rmax - height[j]
                j -= 1
                
        return ans       
        
        '''
