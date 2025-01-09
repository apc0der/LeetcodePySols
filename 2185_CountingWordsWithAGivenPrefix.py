class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len([q for q in words if len(q) >= len(pref) and q[:len(pref)] == pref])
