class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_c = Counter(s)
        t_c = Counter(t)
        if len(t)!=len(s):
            return False
        for c in s:
            if s_c[c]!=t_c[c]:
                return False
        return True
        
        