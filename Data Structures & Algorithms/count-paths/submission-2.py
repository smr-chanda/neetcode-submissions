class Solution:
    paths = {}
    def uniquePaths(self, m: int, n: int) -> int:
        if (m,n) in self.paths:
            return self.paths[(m,n)]
        elif m == 1 or n == 1:
            return 1
        else:
            result = self.uniquePaths(m,n-1) + self.uniquePaths(m-1,n)
            self.paths[(m,n)] = result
            return result
        
        


        