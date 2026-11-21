class Solution:
    paths = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        if (m,n) in self.paths:
            return self.paths[(m,n)]
        else:
            result = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
            self.paths[(m,n)] = result
            return result
        
        


        