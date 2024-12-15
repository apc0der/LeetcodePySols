class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        # simple simulation, no brainpower
        m1, m2 = memory1, memory2
        crash = None
        for i in range(1, 100000): # check 100000 seconds
            if m1 >= m2: # pick most memory stick (or 1 if tie)
                if i > m1: # if not available
                    crash = i # crash
                    break
                else: # otherwise allocate
                    m1 -= i
            else: # same exact logic here
                if i > m2:
                    crash = i
                    break
                else:
                    m2 -= i
        return [crash, m1, m2]
