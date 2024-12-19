class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        a, s = arr, sorted(arr) # get the target
        chunks = 0 # number of splits
        l = 0 # original left bound
        r = 1 # original right bound
        while l != len(a): # while there are some elements left to chunk
            # if the elements in the chunk window, when sorted, do not match the target window
            if sorted(a[l:r]) != s[l:r]: 
                r += 1 # extend the chunk window
            else: # if it does match
                chunks += 1 # we have a chunk
                l = r # new chunk starts here
                r = l+1 # new chunk ends here
        return chunks # return the number of chunks
