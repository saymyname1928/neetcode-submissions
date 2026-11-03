class Twitter:

    def __init__(self):
        self.internal_cycle= 0
        self.user_feeds = collections.defaultdict(lambda: [])
        self.followers = collections.defaultdict(lambda: [])


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_feeds[userId].append([self.internal_cycle, tweetId])
        self.internal_cycle += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        newsfeed = []
        
        for followee in self.followers[userId] + [userId]:
            feeds = self.user_feeds[followee]
            # print(feeds)

            for feed in feeds:
                heapq.heappush(newsfeed, feed)
                if len(newsfeed) > 10:
                    heapq.heappop(newsfeed)

        ret = []
        for _ in range(len(newsfeed)):
            ret.append(heapq.heappop(newsfeed)[1])
        ret.reverse()
        return ret


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
        
        
