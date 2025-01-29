class RecentCounter(object):

    def __init__(self):
        self.queue = []
        self.windowstart = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.queue.append(t)

        while self.windowstart < len(self.queue) and self.queue[self.windowstart] < t - 3000:
            self.windowstart += 1
        return len(self.queue) - self.windowstart
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)