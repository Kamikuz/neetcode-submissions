class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # base check
        if not t:
            return ""

        # build freq map
        countT = defaultdict(int)
        for c in t:
            countT[c] += 1
        
        # init
        window = defaultdict(int)
        have = 0
        need = len(countT)
        l = 0
        res, resL = [-1, -1], float("infinity")
        for r in range(len(s)):
            # update the count
            window[s[r]] += 1
            
            if countT[s[r]] == window[s[r]]:
                have += 1
            
            while have == need:
                if (r-l+1) < resL:
                    res, resL = [l, r], r - l + 1
                
                window[s[l]] -= 1
                if window[s[l]] + 1 == countT[s[l]]:
                    have -= 1
                
                l  += 1

        l, r = res
        return s[l: r+1] if resL != float("infinity") else ""