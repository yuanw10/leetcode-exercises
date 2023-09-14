class Solution(object):
    def similarPairs(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        word_sets = [set(word) for word in words]
        word_strs = [''.join(sorted(word)) for word in word_sets]
        count = {}
        for word in word_strs:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
        
        num_pairs = 0
        for word, num in count.items():
            for i in range(num):
                num_pairs += i
        return num_pairs



        