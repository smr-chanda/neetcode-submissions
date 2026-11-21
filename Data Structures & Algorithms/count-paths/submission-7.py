class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        dp1 = [1] * n
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    # dp[i][j] = 1
                    dp1[j] = 1
                else:
                    # dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    dp1[j] += dp1[j-1]
        
        return dp1[n-1]
                
        