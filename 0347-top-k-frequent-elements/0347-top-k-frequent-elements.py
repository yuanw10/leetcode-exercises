class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        for n in nums:
            freq[n]=1+freq.get(n,0)

        count=list(freq.values())
        count.sort(reverse=True)

        topK=[]

        for i in range(0,k):
            for k, v in freq.items():
                if count[i]==v:
                    topK.append(k)
                    freq.pop(k)
                    break

        return topK