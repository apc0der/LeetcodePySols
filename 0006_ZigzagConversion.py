class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            # if one row, straight line
            return s
        if numRows == 2:
            # if two rows, alternating
            return s[::2]+s[1::2]
        lst = [[] for i in range(numRows)] # result
        down = True # direction
        row = 0 # row index
        for i in range(len(s)): # iterate across chars
            lst[row].append(s[i]) # add curr char to the row
            if down: # if down            
                if row == len(lst)-1: # switch
                    down = False
                    row -= 1
                else:
                    row += 1
            else: # if not down
                if row == 1: # switch
                    down = True
                row -= 1
        s = "".join(["".join(subL) for subL in lst]) # format
        return s
