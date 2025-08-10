class Solution:
    def minMaxDifference(self, num: int) -> int:
        # only place digit that matters is the most significant
        s = str(num)
        bot = int(str(num).replace(str(num)[0], '0'))
        lst = [i for i in range(len(s)) if s[i] != '9']
        if len(lst) == 0:
            return num - bot
        
        top = int(s.replace(s[lst[0]], '9'))
        return top-bot
