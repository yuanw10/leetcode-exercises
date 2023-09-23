class Solution(object):
    def countAsterisks(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for i in range(len(s)):
            ch = s[i]
            if count < 2:
                stack.append(ch)
                if ch == '|':
                    count += 1
            if count == 2:
                while count > 0:
                    last = stack.pop()
                    if last == '|':
                        count -= 1

        ast_count = 0
        while len(stack) > 0:
            if stack.pop() == '*':
                ast_count += 1
        return ast_count