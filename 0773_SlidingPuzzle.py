class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        targ = "123450" # goal configuratioon
        # current configuration
        brd = "".join([str(q) for q in board[0]])+"".join([str(q) for q in board[1]])
        if brd == targ: # if already good
            return 0
        vis = {brd} # vis set, don't want to repeat steps
        q = deque()
        q.append((0, brd)) # initial config

        def swap(s, a, b): # QOL swap tile method
            a, b = min(a, b), max(a, b)
            return s[:a] + s[b] + s[a+1:b] + s[a] + s[b+1:]

        while len(q) != 0: # while still elements left to process
            m, b = q[0] # queue => BFS prioritizes least moves 
            q.popleft()
            # assume the current ISNT the solution, prevents waiting
            # instead check solution when doing next moves
            # so if no solution, the next moves are all NON SOLUTIONS
            i = b.index('0') # used to find next moves
            nxt = [] # stores next moves
            
            match i: # generate the next moves
                case 0: # can either swap with right or below
                    nxt.append(swap(b, 0, 1))
                    nxt.append(swap(b, 0, 3))
                case 1: # left, right, or below
                    nxt.append(swap(b, 1, 0))
                    nxt.append(swap(b, 1, 2))
                    nxt.append(swap(b, 1, 4))
                case 2: # left or below
                    nxt.append(swap(b, 2, 1))
                    nxt.append(swap(b, 2, 5))
                case 3: # right or above
                    nxt.append(swap(b, 3, 0))
                    nxt.append(swap(b, 3, 4))
                case 4: # left, right or above
                    nxt.append(swap(b, 4, 1))
                    nxt.append(swap(b, 4, 3))
                    nxt.append(swap(b, 4, 5))
                case 5: # left or above
                    nxt.append(swap(b, 5, 2))
                    nxt.append(swap(b, 5, 4))

            for n in nxt: # for each next move
                if n == targ: # if its the solution, its 1 more than the current move ct.
                    return m+1
                if n not in vis: # else, only add if its a unique state
                    vis.add(n)
                    q.append((m+1, n))
        # if while loop exits, and nothing was returned, that means no possible solution
        return -1
