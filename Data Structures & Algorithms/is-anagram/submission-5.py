class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_vec = [0]*26
        t_vec = [0]*26
        for char in s:
            s_vec[ord('a')-ord(char)]+=1
        for char in t:
            t_vec[ord('a')-ord(char)]+=1
        return s_vec==t_vec

        
        