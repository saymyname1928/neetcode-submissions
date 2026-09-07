from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = ""
        res = 0
        for i in range(len(s)):
            if s[i] not in curr:
                curr += s[i]
            else:
                idx = curr.find(s[i])
                curr = curr[idx+1:] + s[i]

            res = max(res, len(curr))

        return res
                


        
                