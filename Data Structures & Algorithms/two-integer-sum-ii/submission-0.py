class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in memo:
                memo[numbers[i]] = i
            else:
                return [memo[target - numbers[i]] + 1, i + 1]