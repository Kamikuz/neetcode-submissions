class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        # sort the list (nlogn)
        nums.sort()

        for i, n in enumerate(nums):
            # find the left pointer whole value is negative
            if n > 0:
                break
            
            # skip the same numbers
            if i > 0 and n == nums[i - 1]:
                continue
            
            # set the left, right pointer
            l, r = i + 1, len(nums) - 1
            while l < r:
                # get total sum
                curr = n + nums[l] + nums[r]

                # if greater than 0
                if curr > 0:
                    # move the r pointer left
                    r -= 1
                elif curr < 0:
                    # 
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l <r:
                        l += 1
        return res
