from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
                # l = mp[s[r]]+1
            mp[s[r]] = r
            res = max(res, r - l + 1)

            # print(l, r, res)
        return res
                


        
                