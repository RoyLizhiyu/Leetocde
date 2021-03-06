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
    int answer = 1;
    public void helper(TreeNode node, int depth){
        if (node == null){
            return;
        }
        
        if (node.left == null && node.right == null){
            answer = Math.max(answer, depth);
            return;
        }
        
        helper(node.left, depth+1);
        helper(node.right, depth+1);
    }
    public int maxDepth(TreeNode root) {
        if (root == null){
            return 0;
        }
        
        helper(root, 1);
        return answer;
    }
}
