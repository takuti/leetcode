class Solution(object):
    def isInterleave_(self, s1, i, s2, j, s3, k, memo):
        if len(s1[i:]) + len(s2[j:]) != len(s3[k:]):
            return False

        while i < len(s1) and j < len(s2) and k < len(s3):
            if memo[i][j] != -1:
                return memo[i][j] == 1

            if s3[k] != s1[i] and s3[k] != s2[j]:
                memo[i][j] = 0
                return False

            if s1[i] == s2[j]:
                if self.isInterleave_(s1, i+1, s2, j, s3, k+1, memo) or \
                    self.isInterleave_(s1, i, s2, j+1, s3, k+1, memo) :
                    memo[i][j] = 1
                    return True
            elif s3[k] == s1[i]:
                i += 1
            else:
                j += 1

            k += 1

        return s1[i:] + s2[j:] == s3[k:]

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        memo = [[-1] * len(s2) for _ in range(len(s1))]

        return self.isInterleave_(s1, 0, s2, 0, s3, 0, memo)

