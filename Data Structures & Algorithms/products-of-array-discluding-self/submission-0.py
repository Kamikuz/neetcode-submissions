class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        value = 1
        for i in range(len(nums)):
            res[i] = value
            value *= nums[i]
        value = 1
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= value
            value *= nums[i]

        return res
