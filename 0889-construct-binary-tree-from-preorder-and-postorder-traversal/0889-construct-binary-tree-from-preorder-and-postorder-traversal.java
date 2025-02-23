/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    int preIndex = 0;
    int postIndex = 0;

    public TreeNode constructFromPrePost(int[] preorder, int[] postorder) {
        return buildTree(preorder, postorder);
    }

    public TreeNode buildTree(int preorder[], int postorder[]) {

        TreeNode root = new TreeNode(preorder[preIndex++]);

        if (root.val != postorder[postIndex])
            root.left = buildTree(preorder, postorder);

        if (root.val != postorder[postIndex])
            root.right = buildTree(preorder, postorder);

        postIndex++;
        return root;
    }
}