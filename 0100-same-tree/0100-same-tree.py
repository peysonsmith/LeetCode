# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Base cases:
        # 1. If the two trees are both null return true
        # 2. If the p is null or q is null and the other is not return false
        # 3. If the value of p and the value of q are different return false
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        # DFS through each tree comparing each node to each other
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

