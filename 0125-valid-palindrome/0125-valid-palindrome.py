class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while i <= j:
            if s[i].isalnum() and s[j].isalnum():
                if s[i].lower() == s[j].lower():
                    i = i+1
                    j = j-1
                else:
                    return False
            elif not s[i].isalnum():
                i = i+1
            else:
                j = j-1
        return True
            