/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int result = 0;
    public boolean is_uni(TreeNode node){
        if (node == null){
            return false;
        }
        
        if (node.left == null && node.right == null){
            result++;
            return true;
        }
        boolean is_unival = true;
        if (node.left != null){
            is_unival = is_uni(node.left) && is_unival && node.left.val == node.val;
        }
        if (node.right != null){
            is_unival = is_uni(node.right) && is_unival && node.right.val == node.val;
        }
        if (!is_unival){
            return false;
        }
        result++;
        return true;
    }
    public int countUnivalSubtrees(TreeNode root) {
        if (root == null){
            return 0;
        }
        is_uni(root);
        return result;
    }
}
