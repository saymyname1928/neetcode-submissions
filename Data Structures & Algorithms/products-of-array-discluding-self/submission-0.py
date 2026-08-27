class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        acc = 1
        l = []
        for i in range(len(nums)):
            acc = acc * nums[i]
            l.append(acc)
        acc = 1

        r = []
        for i in range(len(nums)-1, -1, -1):
            acc = acc * nums[i]
            r.append(acc)
        r.reverse()

        ret = []
        for i in range(len(nums)):
            if i == 0:
                ret.append(r[i+1])
            elif i == len(nums) - 1:
                ret.append(l[i-1])
            else:
                ret.append(l[i-1]* r[i+1])
        return ret


        # l: [1, 2, 8, 48]
        # r: [48, 48, 24, 6]
        # ret: [, ]