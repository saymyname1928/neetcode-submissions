class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        # 1. find how many times the array has been roated
        # To find k, we must search for the smallest element.
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = ((l + r) // 2)

            # if right hand side is not sorted, it contains the minimum
            # else, the left hand side contains the minimum
            if not nums[mid] < nums[r]:
                l = mid + 1
            else:
                r = mid
        min_idx = l

        # 2. un-rotate the array
        sorted_nums = nums[l:] + nums[:l]
        
        # 3. find the target using binary search
        l = 0
        r = len(nums) - 1
        ret = -1
        # print(sorted_nums)
        # print(target)
        while l <= r:
            mid = ((l+r) // 2)
            # print(l, r, mid)
            if target == sorted_nums[mid]:
                # print(sorted_nums, mid, target)
                ret = mid
                break
            elif target < sorted_nums[mid]:
                r = mid - 1
            else:
                l = mid + 1

        if ret == -1:
            return -1
        
        return (min_idx + ret) % len(nums)
        
