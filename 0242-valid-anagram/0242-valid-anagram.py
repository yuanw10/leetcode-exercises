class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict = {}
        for le in s:
            # if s_dict.has_key(le):
            #     s_dict[le] = s_dict[le]+1
            # else:
            #     s_dict[le] = 1
            s_dict[le] = s_dict.get(le, 0)+1
        for le in t:
            if not s_dict.has_key(le) or s_dict[le] <= 0:
                return False
            else:
                s_dict[le] = s_dict[le]-1
        return True