class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s3) <= 1:
            return s1 + s2 == s3

        cnt = {}
        for c in (s1 + s2):
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        for c in s3:
            if c not in cnt or cnt[c] == 0:
                return False
            cnt[c] -= 1

        i, j, k = 0, 0, 0

        while i < len(s1) and j < len(s2) and k < len(s3):
            if s3[k] != s1[i] and s3[k] != s2[j]:
                return False

            if s1[i] == s2[j]:
                if self.isInterleave(s1[i+1:], s2[j:], s3[k+1:]):
                    return True
                else:
                    j += 1
            elif s3[k] == s1[i]:
                i += 1
            else:
                j += 1

            k += 1

        return s1[i:] + s2[j:] == s3[k:]
