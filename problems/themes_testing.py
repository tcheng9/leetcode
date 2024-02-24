# Python code to count the number of occurrences
def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x,
                                        countX(lst, x)))



class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
	    
        m, n = len(matrix), len(matrix[0])
        
        def dfs(i, j, prev):
            
            # base condition : check "out of boundaries" situation and 
            # also if "current <= previous" then these are invalid conditions. 
            if i < 0 or j < 0 or i >= m or j >= n or matrix[i][j] <= prev:
                return 0
            
            # expand and look in all four directions using simple depth first search
            left = dfs(i, j - 1, matrix[i][j])
            right = dfs(i, j + 1, matrix[i][j])
            top = dfs(i - 1, j, matrix[i][j])
            bottom = dfs(i + 1, j, matrix[i][j])
            
            # return max depth of longest increasing path and 
            # plus 1 to consider the current element.
            return max(left, right, top, bottom) + 1
             
        
        # compute the longest increasing path for each element and
        # update the max value as answer.
        ans = -1
        for i in range(m):
            for j in range(n):
                ans = max(ans, dfs(i, j, -1))
        return ans