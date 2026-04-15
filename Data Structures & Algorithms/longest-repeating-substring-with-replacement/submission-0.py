class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        feqs = defaultdict(int)
        l = 0
        maxf = 0
        res = 0

        for r in range(len(s)):
            feqs[s[r]] += 1
            maxf = max(feqs[s[r]], maxf)
            
            while r - l + 1 - maxf > k:
                feqs[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res