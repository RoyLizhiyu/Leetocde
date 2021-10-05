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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null){
            return false;
        }
        int comp = targetSum - root.val;
        
        if (comp == 0){
            if (root.left == null && root.right == null){
                return true;
            }
        }
     boolean left = hasPathSum(root.left, comp);
     boolean right = hasPathSum(root.right, comp);
    return left || right;
        
    }
}
