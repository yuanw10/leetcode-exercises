class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=1
        cur=0
        i=0
        while i<len(nums):
            if nums[cur]!=nums[i]:
                cur+=1
                nums[cur]=nums[i]
                k+=1
            i+=1
        return k