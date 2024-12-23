class Codec:
    def serialize(self, root):
        if root is None: # NOTHING TO SERIALIZE
            return ""
        dex2val = {} # track which indices in the array form of a tree have what value (1-indexed)
        def fill(cur, k): # populate the map
            if cur is not None: # if a node is here
                dex2val[k] = cur.val # put the value at index k
                fill(cur.left, 2*k) # left is twice k
                fill(cur.right, 2*k+1) # right is twice k + 1
        fill(root, 1) # 1-indexed
        v = [str(i)+":"+str(dex2val[i]) for i in sorted(list(dex2val.keys()))]
        return "|".join(v) # better than putting as array because of the potentially many None values

    def deserialize(self, data):
        if data == "": # NOTHING TO DESERIALIZE
            return None
        v = data.split("|") # split up into data points
        dex2val = {} # rebuild index to value map
        for pt in v: # populate the map
            datum = pt.split(":")
            dex2val[int(datum[0])] = int(datum[1])
        def build(k): # creates a node and recurses for children, then returns
            node = TreeNode(dex2val[k])
            if 2*k in dex2val: # children only get set (default None) if they exist
                node.left = build(2*k)
            if 2*k+1 in dex2val:
                node.right = build(2*k+1)
            return node
        root = build(1) # 1-indexed
        return root
