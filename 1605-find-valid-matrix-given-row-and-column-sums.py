class Solution(object):
    def restoreMatrix(self, rowSum, colSum):
        """
        :type rowSum: List[int]
        :type colSum: List[int]
        :rtype: List[List[int]]
        """
        m, n = len(rowSum), len(colSum)
        output = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                output[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= output[i][j]
                colSum[j] -= output[i][j]
        return output


rowSum = [3, 8]
colSum = [4, 7]

res = Solution().restoreMatrix(rowSum, colSum)
print(res)
