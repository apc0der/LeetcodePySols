class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan":"01", "Feb":"02", "Mar":"03", 
                 "Apr":"04", "May":"05", "Jun":"06", 
                 "Jul":"07", "Aug":"08", "Sep":"09", 
                 "Oct":"10", "Nov":"11", "Dec":"12"}
        d = date.split(" ")
        ret = d[2]+"-"
        ret += month[d[1]]+"-"
        d = d[0][:-2]
        if int(d) < 10:
            ret += '0'
        ret += d
        return ret
