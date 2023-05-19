class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        zeros = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zeros.add((i, j))
        
        for el in zeros:
            i, j = el
            matrix[i] = [0] * n
            for k in range(m):
                matrix[k][j] = 0


if __name__ == "__main__":
    # Let's solve Set Matrix Zeros:
    # https://leetcode.com/problems/set-matrix-zeroes/
    sol = Solution()
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    sol.setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    sol.setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
