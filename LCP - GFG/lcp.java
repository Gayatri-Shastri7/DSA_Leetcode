// { Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;
import java.math.*;

class GFG
{
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.next());
        
        while(t-- > 0)
        {
            int n = Integer.parseInt(sc.next());
            
            String s[] = new String[n];
            for(int i=0;i<n;i++)
            {
                s[i] = sc.next();
            }
            Solution T = new Solution();
            System.out.println(T.lcp(s,n));
        }
        
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution
{
public String lcp(String S[],int n)
   {
  if (n == 0) return "";
 String prefix = S[0];
 for (int i = 1; i < n; i++)
  while (S[i].indexOf(prefix) != 0) {
   prefix = prefix.substring(0, prefix.length() - 1);
   if (prefix.isEmpty()) return "-1";
  }        
 return prefix;

       
   }
}
