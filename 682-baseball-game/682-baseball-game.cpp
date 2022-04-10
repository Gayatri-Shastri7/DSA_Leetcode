class Solution {
public:
    int calPoints(vector<string>& ops) {
        int a, b;
        int ans = 0;
        stack<int>s;
        for(auto i : ops){
            if(i == "C"){
                s.pop();
            }
            else if(i == "D"){
                s.push(s.top()*2);
            }
            else if(i == "+"){
                a = s.top();
                s.pop();
                b = s.top();
                s.push(a);
                s.push(a + b);
            }
            else {
                s.push(stoi(i)); //stoi() is used to convert string into integer 
            }
        }
        while(!s.empty()){
            ans += s.top();
            s.pop();
        }
        return ans;
    }
};