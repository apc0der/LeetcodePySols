class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ps, ts = sorted(players), deque(sorted(trainers))
        ct = 0 # matches
        for p in ps:
            if len(ts) == 0: # safety
                break
            while ts[0] < p: # remove unqualified trainers
                ts.popleft()
                if len(ts) == 0: # safety
                    break
            if len(ts) == 0: # safety
                break
            ts.popleft() # the trainer we broke on, can be paired with the player
            ct += 1 # thus, add 1
        return ct
