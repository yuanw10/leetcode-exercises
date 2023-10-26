class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        strs.sort(key=len)
        common_prefix = strs[0]
        for word in strs:
            for i in range(len(common_prefix)):
                if common_prefix[i] != word[i]:
                    common_prefix = common_prefix[0:i]
                    break
        return common_prefix 
