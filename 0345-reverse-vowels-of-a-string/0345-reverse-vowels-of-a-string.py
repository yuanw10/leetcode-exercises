class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        new_s = ""
        i, j = 0, len(s)-1
        while len(new_s) < len(s):
            if s[i] not in vowels:
                new_s += s[i]
            else:
                while s[j] not in vowels:
                    j -= 1
                new_s += s[j]
                j -= 1
            i += 1
        return new_s
            