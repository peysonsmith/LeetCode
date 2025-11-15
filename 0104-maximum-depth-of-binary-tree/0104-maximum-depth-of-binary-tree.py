# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Recursive DFS:
        # if root == None:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # BFS Queue
        if root == None:
            return 0

        level = 0
        q = deque([root])
        while q: # while q is not empty
            for i in range(len(q)):
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)

            level += 1
        return level