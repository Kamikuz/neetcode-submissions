class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        quotient = {}
        for i in range(len(nums)):
            if (target - nums[i]) in quotient:
                return [quotient[target - nums[i]], i]
            quotient[nums[i]] = i
