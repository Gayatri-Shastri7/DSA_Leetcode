class Solution {
public:
    bool valid_row(int c_row, vector<vector<char>>&grid, int n)
    {
        for(int i=0;i<n;i++)
        {
            if(grid[c_row][i]=='Q')
                return false;
        }
        return true;
    }
    
    bool valid_col(int c_col, vector<vector<char>>&grid, int n)
    {
        for(int i=0;i<n;i++)
        {
            if(grid[i][c_col]=='Q')
                return false;
        }
        return true;
    }
        bool valid_dia(vector<vector<char>>&grid,int c_row, int c_col,  int n)
    {
            int i = c_row;
            int j = c_col;
            while(i>=0 && j>=0)
            {
                if(grid[i][j]=='Q')
                    return false;
                i--;j--;
            }
            
             i = c_row;
             j = c_col;
            while(i>=0 && j<n)
            {
                if(grid[i][j]=='Q')
                    return false;
                i--;j++;
            }
            
             i = c_row;
             j = c_col;
            while(i<n && j>=0)
            {
                if(grid[i][j]=='Q')
                    return false;
                i++;j--;
            }
    i = c_row;
    j = c_col;
    while(i<n && j<n)
    {
        if(grid[i][j]=='Q')
            return false;
        i++,j++;
    }
            return true;
    }
    bool isValid(vector<vector<char>>&grid, int c_row,int c_col,int n)
    {
        return valid_row(c_row,grid,n) && valid_col(c_col,grid,n) && valid_dia(grid,c_row,c_col,n);
    }
    
    //Function to convert grid char to strings
    vector<string> populate(vector<vector<char>>&grid,int n)
    {
       
            vector<string> result;
            for(int i=0;i<n;i++)
            {
                string temp="";
                for(int j=0;j<n;j++)
                {
                    temp += grid[i][j];
                }
                result.push_back(temp);
            }
            return result;
        }
    
    void solve(vector<vector<char>>&grid, int c_row,int n, vector<vector<string>>&ans)
    {
        if(c_row ==n){
            vector<string> temp =populate(grid,n);
            ans.push_back(temp);
            return;
            
        }
        for(int c_col=0;c_col<n;c_col++)
        {
            if(isValid(grid,c_row,c_col,n)){
                grid[c_row][c_col] ='Q';
                solve(grid,c_row+1,n,ans);
                grid[c_row][c_col]='.';
            }
        }
    }
    
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> ans;
        vector<vector<char>>grid(n,vector<char>(n,'.'));
        solve(grid,0,n,ans);
        return ans;
        
    }
};