class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        s_list = sorted(s)
        t_list = sorted(t)
        count = 0
        for i in range(0, len(s)):
            if s_list[i] == t_list[i]:
                count += 1

        
        if count == len(s):
            return True
        else:
            return False