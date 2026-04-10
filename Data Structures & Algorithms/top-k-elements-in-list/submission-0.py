class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the frequentce
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        # bucket sort 
        bucket = [[] for _ in range(len(nums))] # not use [[]] * ..., which will cuase the copy
        for n, c in count.items():
            bucket[c-1].append(n)
        
        # extract the top k elements
        res = []
        for f in range(len(nums)-1, -1, -1):
            for n in bucket[f]:
                res.append(n)
                if (len(res) == k):
                    return res