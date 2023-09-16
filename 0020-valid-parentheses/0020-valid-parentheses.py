class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if len(s)%2 == 1 or len(s) == 0:
        #     return False

        # i = len(s)-1
        # stack = []
        # while i>=0:
        #     s_last = s[i]
        #     if len(stack) == 0:
        #         stack.append(s_last)
        #     else:
        #         st_last = stack[-1]
        #         if (s_last=="{" and st_last=="}") or (s_last=="(" and st_last==")") or (s_last=="[" and st_last=="]"):
        #             stack.pop()
        #         else:
        #             stack.append(s_last)
        #     i=i-1
        # return len(stack) == 0

        d = {"(":")", "{":"}", "[":"]"}
        stack=[]
        for le in s:
            if le in d:
                stack.append(le)
            elif len(stack)==0 or d[stack.pop()]!=le:
                return False
        return len(stack)==0