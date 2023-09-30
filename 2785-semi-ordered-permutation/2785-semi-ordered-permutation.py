class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        min_index = nums.index(1)
        max_index = nums.index(len(nums))
        count += min_index  # num of swaps for 1

        # num of swaps for n
        if max_index < min_index:
            count += len(nums)-2-max_index
        else:
            count += len(nums)-1-max_index

        return count
