/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null ) return root ;
        swapNode(root);
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }
    public void swapNode(TreeNode root){
        TreeNode tmp = root.left;
        root.left = root.right;
        root.right = tmp;
    }
}
};