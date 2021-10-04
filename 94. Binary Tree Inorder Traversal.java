class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        if (root == null){
            return result;
        }
        List<Integer> left = inorderTraversal(root.left);
        List<Integer> right = inorderTraversal(root.right);
        result.addAll(left);
        result.add(root.val);
        result.addAll(right);
        return result;
        
        
    }
}
