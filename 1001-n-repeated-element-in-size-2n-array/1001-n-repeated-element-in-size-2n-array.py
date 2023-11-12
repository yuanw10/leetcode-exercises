class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # return middle item in sorted array
        # n = len(nums)/2
        # nums.sort()
        # return nums[n]

        # return repeated item
        items = set()
        for num in nums:
            if num in items:
                return num
            else:
                items.add(num)