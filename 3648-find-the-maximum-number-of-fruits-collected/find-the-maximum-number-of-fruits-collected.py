class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        self.n = len(fruits)
        # total = sum(fruits[i][i] for i in range(self.n))
        total = 0
        for i in range(self.n):
            total += fruits[i][i]
            fruits[i][i] = 0
        
        self.memo = [[-1] * self.n for _ in range(self.n)]

        # I get this fruits collected by digonal path

        # right_path = [0] * 3 # dp
        # bottom_path = [0] * 3 # dp

        # right_path[0] = fruits[0][n-1] # fruits at rightpath initial path
        # bottom_path[0] = fruits[n - 1][0]

        # window = 3 # there are three ways we can move left, right, straight

        def dfs_to_right(row, col):
            # row will increase decrease remain same   
            # column wil always increase
            # cant cross digonal
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0
            
            if self.memo[row][col] != -1:
                return self.memo[row][col]

            val = fruits[row][col]
            res = 0

            if row == col:
                res = max(res, dfs_to_right(row+1, col+1))
            elif row - 1 == col:
                res = max(res, dfs_to_right(row + 1, col + 1))
                res = max(res, dfs_to_right(row, col + 1))
            else:
                res = max(res, dfs_to_right(row + 1, col + 1))
                res = max(res, dfs_to_right(row, col + 1))
                res = max(res, dfs_to_right(row - 1, col + 1))
            
            self.memo[row][col] = val + res
            
            return val + res
        
        def dfs_to_bottom(row, col):
            if row < 0 or col < 0 or row >= self.n or col >= self.n:
                return 0
            
            if self.memo[row][col] != -1:
                return self.memo[row][col]

            val = fruits[row][col]
            res = 0

            if row == col:
                res = max(res, dfs_to_bottom(row + 1, col + 1))
            elif row == col - 1:
                res = max(res, dfs_to_bottom(row + 1, col + 1))
                res = max(res, dfs_to_bottom(row + 1, col))
            else:
                res = max(res, dfs_to_bottom(row + 1, col + 1))
                res = max(res, dfs_to_bottom(row + 1, col))
                res = max(res, dfs_to_bottom(row + 1, col - 1))

            self.memo[row][col] = val + res
            return self.memo[row][col]
        
        total += dfs_to_right(self.n - 1, 0)

        total += dfs_to_bottom(0, self.n - 1)

        return total