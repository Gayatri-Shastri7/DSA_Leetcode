class Solution {
public:
    void findAll(map<char,string>&mapper, string digits,vector<string>&ans, string &s,int currentIndex)
    {
        if(currentIndex >=digits.length()){
            ans.push_back(s);
            return;
        }
        
        char currNum = digits[currentIndex];
        string alpha = mapper[currNum];
        
        for(int i=0; i<alpha.size(); i++){
            s.push_back(alpha[i]);
            findAll(mapper,digits,ans,s,currentIndex+1);
            s.pop_back();
        }
        return;
    }    
    
    vector<string> letterCombinations(string digits) {
        map<char,string>mapper{
            {'1',""},
            {'2',"abc"},
            {'3',"def"},
            {'4',"ghi"},
            {'5',"jkl"},
            {'6',"mno"},
            {'7',"pqrs"},
            {'8',"tuv"},
            {'9',"wxyz"},
        };
        string s="";
        vector<string> ans;
        if(digits.size()==0){
            return ans;
        }
        findAll(mapper,digits,ans,s,0);
        return ans;
    }
};