class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        m = {} # keeps track of nodes at each level, L-->R
        def build(cur, dep):
            if cur is not None: # if it is a valid node, not None
                if dep not in m: # if first discovered at this depth
                    m[dep] = [] # empty list
                m[dep].append(cur.val) # builds left to right, since DFS
                build(cur.left, dep+1)
                build(cur.right, dep+1)
        build(root, 0) # init call
        form = [] # array form
        for k in sorted(m.keys()):
            if k%2 == 0: # keep even levels nice
                form += m[k]
            else: # reverse odd levels
                form += m[k][::-1]
        def make(k): # builds tree up from array form
            if k <= len(form): # if valid index
                node = TreeNode(form[k-1]) # get the value
                node.left = make(2*k) # set the children
                node.right = make(2*k+1)
                return node
            else: # otherwise we need a null child
                return None
        ret = make(1) # init call
        return ret
