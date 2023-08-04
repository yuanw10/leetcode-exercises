class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Option 1:
        # sort and return mid element
        # O(nlgn) time
        # nums.sort()
        # return nums[len(nums)//2]


        # Option 2:
        # randomized algorithm 
        # expiated time: O(n)
        while True:
            i = random.randint(0,len(nums)-1)
            freq = 0
            for n in nums:
                if n == nums[i]:
                    freq += 1
                if freq > len(nums)//2:
                    return nums[i]