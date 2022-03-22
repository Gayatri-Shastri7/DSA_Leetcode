class Solution {
public:
    string getSmallestString(int n, int k) {
     
        
        string res(n, ' ');
        
        for(int i=n; i>0; i--)
        {
            int charIdx = min(26, (k-i+1));
            res[i-1] = 'a' + (charIdx - 1);
            k -= charIdx;
        }
        
        return res;
    
    }
};