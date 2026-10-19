class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for e in points:
            heapq.heappush(h, (e[0]**2 + e[1]**2, e))

        ret = []
        # print(h)
        for i in range(k):
            ret.append(heapq.heappop(h)[1])
        
        # print(ret)
        return ret
