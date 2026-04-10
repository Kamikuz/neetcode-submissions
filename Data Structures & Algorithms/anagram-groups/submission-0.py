class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = [0] * 26
            for i in range(len(s)):
                key[ord(s[i]) - ord('a')] += 1
            anagrams[tuple(key)].append(s)
        
        return list(anagrams.values())