class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        nodes = {} # maps value to node
        lsts = {} # ancestor dict
        def trace(node, anc): # build ancestor list
            nodes[node.val] = node
            if node.left is None and node.right is None:
                lsts[node.val] = [node.val]+anc
            else:
                if node.left is not None:
                    trace(node.left, [node.val]+anc)
                if node.right is not None:
                    trace(node.right, [node.val]+anc)
        
        trace(root, [])
        keys = list([k for k in lsts])
        longest = max([len(lsts[k]) for k in keys]) # get the deepest path to root
        matr = []
        for k in keys: # prune out any that are not the deepest leaves
            if len(lsts[k]) == longest:
                matr.append(lsts[k])

        if len(matr) == 1: # single leaf case
            return nodes[matr[0][0]]
        for j in range(0, longest): # check common
            match = True
            for i in range(1, len(matr)):
                if matr[i][j] != matr[0][j]:
                    match = False
                    break
            if match:
                return nodes[matr[0][j]]
        return root
