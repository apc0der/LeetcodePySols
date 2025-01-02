class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        played, loss0, loss1, loss2 = set(), set(), set(), set() # loss brackets
        # played keeps track of only the played ones
        # loss0 is for all played winners
        # loss1 is for one losses
        # loss2 is for 2+ losses
        for m in matches: # per match
            if m[0] not in played: # if an unseen player
                loss0.add(m[0]) # winner has zero losses
                played.add(m[0]) # gets played 
                # nothing else needed for winners bc we only track losses
            if m[1] not in played: # which is why the loser is if-else, not just if
                loss1.add(m[1]) # new loser
                played.add(m[1]) # gets played
            else: # if loser seen before
                if m[1] in loss0: # was a winner, now gets 1 loss
                    loss0.remove(m[1])
                    loss1.add(m[1])
                elif m[1] in loss1: # alr lost once, now loses 2+ times
                    loss1.remove(m[1])
                    loss2.add(m[1])
        # sets make the return easy
        return [sorted(list(loss0)), sorted(list(loss1))]          
