class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = nums[i] * -1
            left = i+1
            right = len(nums) - 1

            while left < right:
                curr_sum = nums[left] + nums[right]
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right])) 
                    left += 1
            
        return list(res)
