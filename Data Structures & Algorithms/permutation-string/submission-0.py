class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # base condition
        if len(s2) < len(s1):
            return False

        # update both count into the hash table
        c1, c2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            c1[s1[i]] += 1
            c2[s2[i]] += 1
        
        # inital the matched count
        matched = 0
        for c in c1: 
            matched += (1 if c1[c] == c2[c] else 0)

        # start from the next char
        l = 0
        for r in range(len(s1), len(s2)):
            # exist permutation
            if matched == len(c1):
                return True

            # update the end 
            char_r = s2[r]
            c2[char_r] += 1
            if char_r in c1:
                if c1[char_r] == c2[char_r]:
                    matched += 1
                elif c2[char_r] == c1[char_r] + 1:
                    matched -= 1
            
            # update the start
            char_l = s2[l]
            c2[char_l] -= 1

            # only the 
            if char_l in c1:
                if c1[char_l] == c2[char_l]:
                    matched += 1
                elif c2[char_l] == c1[char_l] - 1:
                    matched -= 1
            l += 1

        return matched == len(c1)
            