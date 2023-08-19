class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diffMap = {}
        for i in range(len(nums)):
            if diffMap.has_key(nums[i]) and not diffMap.get(nums[i]) == i:
                return [diffMap.get(nums[i]), i]
            diff = target - nums[i]
            diffMap[diff] = i
        return []