class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        i=0
        while len(haystack)-i>=len(needle):
            if haystack[i]==needle[0]:
                p=i
                q=0
                while haystack[p]==needle[q]:
                    p+=1
                    q+=1
                    if q==len(needle):
                        return i
            i+=1
        return -1

