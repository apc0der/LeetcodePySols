class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        m = [] # return keeps track of max per level (index)
        def exp(cur, dep):
            if cur is not None:
                if len(m) == dep: # if new dep reached
                    m.append(cur.val) # add a base max
                else:
                    m[dep] = max(m[dep], cur.val) # running max
                exp(cur.left, dep+1) # explore deeper
                exp(cur.right, dep+1)
        exp(root, 0) # init recursive call
        return m
