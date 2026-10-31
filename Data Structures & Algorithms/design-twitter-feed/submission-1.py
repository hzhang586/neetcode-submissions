import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.follows[userId] | {userId}
        heap = []
        feed = []
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid])-1
                timestamp,tweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(-timestamp,tweetId,uid,idx))
        
        while heap and len(feed) < 10:
            neg_time, tweetId, uid,idx = heapq.heappop(heap)
            feed.append(tweetId)
            idx -= 1
            if idx >= 0:
                time_stamp,tweetId = self.tweets[uid][idx]
                heapq.heappush(heap,(-time_stamp,tweetId,uid,idx))
        
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
