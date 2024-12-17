class Solution:
    def isNumber(self, s: str) -> bool:
        if s[0] == '-' or s[0] == '+':
            s = s[1:] # take out the sign, if any

        base = None
        exponent = None

        if 'e' in s: # whether it be little e or big E
            base = s[:s.index('e')] # base comes before
            exponent = s[s.index('e')+1:] # exponent comes after
        elif 'E' in s:
            base = s[:s.index('E')]
            exponent = s[s.index('E')+1:]

        if exponent is None: # if there was never an exponent
            if s.count('.') > 1: # if more than 1 decimal pt
                return False
            elif s.count('.') == 1: # if one decimal
                whole = s[:s.index('.')] # whole part before
                frac = s[s.index('.')+1:] # fractional after
                if whole == "": # okay to have nothing before
                    return frac.isdigit()
                elif frac == "": # okay to have nothing after
                    return whole.isdigit()
                else: # make sure both are numbers
                    return whole.isdigit() and frac.isdigit()
            else: # if no decimal, just make sure it is a number
                return s.isdigit()
        else: # if we do have exponent
            if exponent == "" or base == "e": # if wrong parse
                return False
            if exponent[0] == '-' or exponent[0] == '+':
                exponent = exponent[1:] # remove the sign
            if base.count('.') > 1: # if more than one decimal pt
                return False
            elif base.count('.') == 1: # same case as above, but with extra exponent check
                whole = base[:base.index('.')]
                frac = base[base.index('.')+1:]
                if whole == "":
                    return frac.isdigit() and exponent.isdigit()
                elif frac == "":
                    return whole.isdigit() and exponent.isdigit()
                else:
                    return whole.isdigit() and frac.isdigit() and exponent.isdigit()
            else:
                return base.isdigit() and exponent.isdigit()
