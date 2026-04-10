class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         table = dict()
         for n in nums:
            if n in table:
                return True
            table[n] = 1
         return False
