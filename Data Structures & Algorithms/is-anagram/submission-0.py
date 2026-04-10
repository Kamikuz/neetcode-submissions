class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m = {}
        for i in range(len(s)):
            m[s[i]] = 1 + m.get(s[i], 0)
            m[t[i]] = -1 + m.get(t[i], 0)

        for _, c in m.items():
            if  c != 0:
                return False

        return True