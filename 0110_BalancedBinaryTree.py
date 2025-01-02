class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None: # null case
            return True
        return self.bal(root)[0] # useful to keep track of both return type, and depth
    
    def bal(self, node): # for any node
        if node: # if node is not None
            if node.left is None and node.right is None: # if leaf
                return (True, 1) # depth is just itself, and trivially balanced
            elif node.left is None: # if only right node
                x = self.bal(node.right) # recurse
                if x[0] == False or x[1] > 1: # make sure depth doesn't exceed 1 (d - 0 <= 1)
                    return (False, None) # if False, doesnt matter what depth is
                else: # if okay
                    return (True, 1+x[1]) # send the new depth up
            elif node.right is None: # same case for left node only
                x = self.bal(node.left)
                if x[0] == False or x[1] > 1:
                    return (False, None)
                else:
                    return (True, 1+x[1])
            else: # if both children
                x, y = self.bal(node.left), self.bal(node.right) # recurse
                if x[0] == False or y[0] == False or abs(x[1]-y[1]) > 1:
                    # if either are false, propagate it up
                    # or if the difference is too large
                    return (False, None)
                else:
                    # otherwise, depth is 1 + maximum of the two subdepths
                    return (True, 1+max(x[1], y[1]))
