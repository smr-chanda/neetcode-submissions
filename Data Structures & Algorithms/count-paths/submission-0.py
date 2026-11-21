class Solution:
    paths = 0
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 and n == 1:
            return 1
        elif n == 1:
            return self.uniquePaths(m-1, n)
        elif m == 1:
            return self.uniquePaths(m, n-1)
        return self.uniquePaths(m, n-1) + self.uniquePaths(m-1, n)
        


        