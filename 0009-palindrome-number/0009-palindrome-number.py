class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        y = 0
        x_int = x
        while x > 0:
            re = x%10
            x = x//10
            y = y*10+re
        return x_int==y