import random

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        total = float(sum(w))
        probs = []
        accum = 0.0
        for wi in w:
            accum += wi / total
            probs.append(accum)
        self.probs = probs

    def pickIndex(self):
        """
        :rtype: int
        """
        r = random.random()
        for i in range(len(self.probs)):
            if r <= self.probs[i]:
                return i
        return len(self.probs) - 1



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
