class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum = 0
        p, q = 0, len(mat)-1
        for i in range(len(mat)):
            sum += mat[i][p]
            if p != q:
                sum += mat[i][q]
            p += 1
            q -= 1
        return sum
        