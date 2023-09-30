class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        min_index = nums.index(1)
        count += min_index  # num of swaps for 1
        nums.remove(1)
        nums.insert(0,1)
        max_index = nums.index(len(nums))
        count += len(nums)-1-max_index   # num of swaps for n
        return count
