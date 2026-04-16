from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base case if s1.length > s2.lenth, Flase
        if len(s1) > len(s2):
            return False

        # define counts for s1, s2 for first s1.length chars
        c1, window = Counter(s1), Counter(s2[:len(s1)])

        if c1 == window:
                return True

        for i in range(len(s1), len(s2)):
            # update the right edge
            window[s2[i]] += 1

            # update the left egde (shift the offset back to 0)
            window[s2[i-len(s1)]] -= 1
            
            # udpate the window for the empty
            if window[s2[i-len(s1)]] == 0:
                del window[s2[i-len(s1)]]

            # if included,  return True
            if c1 == window:
                return True
        
        # no matches permutation
        return False
        