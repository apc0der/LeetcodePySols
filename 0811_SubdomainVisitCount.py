class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainCts = {} # tracks frequencies
        for c in cpdomains:
            dt = c.split(" ") # get the visit and domain separate
            v = int(dt[0])
            d = dt[1].split(".")
            for s in range(len(d)):
                subd = ".".join(d[s:]) # each subdomain
                if subd not in domainCts:
                    domainCts[subd] = 0
                domainCts[subd] += v
        ret = [] # build up return list
        for k in domainCts.keys():
            ret += [str(domainCts[k]) + " " + k]
        return ret
