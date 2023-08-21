class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # option1: use hashtable:
        # nums_dict = {}
        # for i in range(len(nums)):
        #     if nums_dict.has_key(nums[i]):
        #         return True
        #     nums_dict[nums[i]] = i
        # return False

        # option2: use set:
        nums_set = set()
        for n in nums:
            if n in nums_set:
                return True
            nums_set.add(n)
        return False