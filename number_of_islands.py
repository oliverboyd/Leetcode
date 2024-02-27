# https://leetcode.com/problems/number-of-islands/description/

def land_chase(grid,i,j):
    n = len(grid)
    m = len(grid[0])
    if i >= 0 and i <= n-1 and j >= 0 and j <= m-1 and grid[i][j] == "1":
        grid[i][j] = "#"
        land_chase(grid,i-1,j)
        land_chase(grid,i+1,j)
        land_chase(grid,i,j-1)
        land_chase(grid,i,j+1)

def num_islands(grid):
    n = len(grid)
    m = len(grid[0])
    total = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "1":
                land_chase(grid,i,j)
                total += 1
    return total