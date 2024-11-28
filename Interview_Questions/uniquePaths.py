'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Constraints:
1 <= m, n <= 100
'''

class Solution:
    def __init__(self):
        memo = [[]]     # Avoid redundant work
        self.m = 0
        self.n = 0

    def traversePaths(self, curr_m: int, curr_n: int):
        # out of bounds - no possible path to destination
        if curr_m >= self.m or curr_n >= self.n:
            return 0
        
        # path from here arleady traversed - return the memo
        if self.memo[curr_m][curr_n] != -1:
            return self.memo[curr_m][curr_n]
        
        # only allowed moves are down & right, gather those path counts
        down, right = self.traversePaths(curr_m+1, curr_n), self.traversePaths(curr_m, curr_n+1)

        # store the possible down & right paths from here
        self.memo[curr_m][curr_n] = down+right

        # return path count from here
        return down+right


    def uniquePaths(self, m: int, n: int) -> int:
        # update memoization structure, with -1 indicating not yet visited
        self.memo = [[-1 for _ in range(n)] for _ in range(m)]

        # there are zero possible paths from the end destination to itself
        self.memo[m-1][n-1] = 1

        # store m & n for readability's sake
        self.m, self.n = m, n

        return self.traversePaths(curr_m=0, curr_n=0)





s = Solution()

print(s.uniquePaths(m=2,n=1))
print(s.uniquePaths(m=2,n=2))
print(s.uniquePaths(m=3,n=2))
print(s.uniquePaths(m=3,n=7))