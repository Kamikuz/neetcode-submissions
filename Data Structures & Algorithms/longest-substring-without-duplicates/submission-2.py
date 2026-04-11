class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        exists = set()
        res = 0
        l = 0

        for r in range(len(s)):
            # if exist, move l forward
            while s[r] in exists:
                exists.remove(s[l])
                l += 1
            exists.add(s[r])
            res = max(res, r - l + 1)
        return res
