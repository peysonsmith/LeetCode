# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def dfs(curr): # Return [Is it balanced: boolean, height: int]
            # Base case: No children, so it is balanced and has a height of 0
            if not curr:
                return [True, 0]

            # Call dfs on both left and right subtree
            left = dfs(curr.left)
            right = dfs(curr.right)

            # For it to be balanced check:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. |left.height - right.height| <= 1
            isBal = left[0] == True and right[0] == True and abs(left[1] - right[1]) <= 1

            # Return if it is balanced and the height which is one more than the longest subtree
            return [isBal, 1 + max(left[1], right[1])]

        res = dfs(root)
        return res[0]