# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None
        # Get the head value of the current tree
        current = postorder.pop()
        
        #Find the index of the head in inorder list
        index = inorder.index(current)
        
        right_subtree = self.buildTree(inorder[index+1:], postorder)
        left_subtree = self.buildTree(inorder[:index], postorder)
        result =TreeNode(current, left_subtree, right_subtree)
        return result
