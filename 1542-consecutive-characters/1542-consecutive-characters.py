class Solution(object):
    def maxPower(self, s):
        """
        :type s: str
        :rtype: int
        # """
        max, count = 1, 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                count += 1
            else:
                count = 1
            if count > max:
                max = count
        return max