class Solution(object):
    def maxAscendingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        sum = nums[0]
        max_sum = sum

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                sum += nums[i+1]
            else:
                sum = nums[i+1]
            if sum > max_sum:
                max_sum = sum

        return max_sum
        