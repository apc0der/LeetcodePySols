class Solution:
    def maxArea(self, height: List[int]) -> int:
        # left wall, right wall, max area
        l, r, m = 0, len(height)-1, 0
        while l != r: # while the gap is existent
            m = max(m, (r-l)*min(height[l], height[r])) # get the area
            if height[l] < height[r]: # if shorter left
                l += 1 # change it
            else: # otherwise change right
                r -= 1
        return m
