import sys
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
    
     def maxDepth(self, root):
        if root == None:
            return 0
        else:
            return 1+ max(self.maxDepth(root.left), self.maxDepth(root.right))

