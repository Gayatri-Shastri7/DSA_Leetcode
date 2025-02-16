class Solution {
    private boolean isConstructed(int[] ans, boolean[] vis, int n, int index){
        if(index == 2*n-1) return true;
        if(ans[index] != 0) return isConstructed(ans,vis, n, index+1);
        boolean found = false;
        for(int i=n; i >= 1; i--){
            if(!vis[i] && ((i==1) || (index + i < 2*n-1 && ans[index + i] == 0))){
                ans[index] = i;
                if(i != 1)ans[index + i] = i;
                vis[i] = true; 
                found = isConstructed(ans,vis, n,index+1); 
                if(found)return found;
                ans[index] = 0;
                if(i != 1)ans[index + i] = 0;
                vis[i] = false;
            }
        }
        return found;
    }
    public int[] constructDistancedSequence(int n) {
        boolean[] vis = new boolean[n+1];
        int ans[] = new int[2*n-1];
        isConstructed(ans, vis, n, 0);
        return ans;
    }
}