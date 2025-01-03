class Solution:
    def minimumOperations(self, num: str) -> int:
        # four case: 00, 25, 50, 75
        num = str(num)
        ret = len(num)-num.count("0") # just zeroes
        if '0' in num: # if theres a zero
            q = num.rindex('0') # we want a 0, or 5 before
            if '0' in num[:q]: # 0 case
                p = num[:q].rindex('0')
                ret = min(ret, len(num)-p-2)
            if '5' in num[:q]: # 5 case
                p = num[:q].rindex('5')
                ret = min(ret, len(num)-p-2)
        if '5' in num: # if theres a 5
            q = num.rindex('5') # we want a 2 or 7 before
            if '2' in num[:q]: # 2 case
                p = num[:q].rindex('2')
                ret = min(ret, len(num)-p-2)
            if '7' in num[:q]: # 7 case
                p = num[:q].rindex('7')
                ret = min(ret, len(num)-p-2)
        return ret # just finite casework
