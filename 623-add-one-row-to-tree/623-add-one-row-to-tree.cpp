/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {

        if(root==NULL)
        return NULL;

        if(d==1)
        {
            TreeNode* node=new TreeNode(v);
            node->left=root;
            return node;
        }

        helper(root,d,v,1);
        return root;
    }
    void helper(TreeNode* root,int d,int v,int curr){
        if(root==NULL)
            return;

        if(curr==d-1){
            TreeNode* temp=root->left;
            root->left = new TreeNode(v);
            root->left->left=temp;

            temp=root->right;
            root->right=new TreeNode(v);
            root->right->right=temp;
            return;
        }else
        {
            helper(root->left,d,v,curr+1);
            helper(root->right,d,v,curr+1);
        }
    }
};
