"""
Clarifying Questions:
Input Constraints: What is the maximum size of the grid?
Edge Cases: Can the grid be empty? Should I handle this case?
Grid Validity: Are there any constraints on the values within the grid other than '0' and '1'?
Adjacent Cells: Do diagonally adjacent cells count as connected?

Approach:
Iterate through each cell in the grid.
When a '1' (land) is found, perform a Depth-First Search (DFS) or Breadth-First Search (BFS) to mark all connected land cells as visited.
Increase the island count whenever a new unvisited land cell is found.
Continue this process until all cells have been checked.

Algorithm:
Use a nested loop to go through each cell in the grid.
If a cell contains '1', initiate a DFS/BFS to traverse and mark the entire island as visited by changing '1's to '0's or using a separate visited set.
Increment the island count each time a DFS/BFS is initiated.

Test Cases:
Base Case: grid = [["0"]] should return 0.
Single Cell Island: grid = [["1"]] should return 1.
Example Case 1: Provided in the question.
Example Case 2: Provided in the question.
Complex Grid: A grid with multiple islands of different sizes and shapes.

Explanation:
The numIslands function starts by checking if the grid is empty.
The dfs function is used to recursively mark all connected '1's as '0's to signify they have been visited.
The nested loops go through each cell in the grid. When a '1' is found, the DFS is called, and the island count is incremented.
Finally, the function returns the total number of islands detected.

### Time Complexity
The time complexity of the solution is \( O(m \times n) \), where \( m \) is the number of rows and \( n \) is the number of columns in the grid. Here's why:

- In the worst case, every cell in the grid will be visited exactly once.
- Each cell is visited once during the nested loop traversal.
- If a cell contains '1' and initiates a DFS, the DFS will mark all connected '1's, ensuring each cell is only processed once.

Therefore, the overall time complexity is \( O(m \times n) \).

### Space Complexity
The space complexity of the solution is \( O(m \times n) \) in the worst case due to the recursion stack in DFS. Here's why:

- In the worst case, where the grid is entirely land (all '1's), the DFS might have to traverse all cells, resulting in a maximum depth of \( O(m \times n) \) in the recursion stack.
- Besides the recursion stack, the algorithm only uses a few additional variables, which do not contribute significantly to the space complexity.

Thus, the overall space complexity is \( O(m \times n) \).

Concepts:

Depth-First Search (DFS)
Concept:
DFS is an algorithm for traversing or searching tree or graph data structures.
It starts at the root (or an arbitrary node) and explores as far as possible along each branch before backtracking.
In the context of a 2D grid, it involves recursively visiting all neighboring cells (up, down, left, right) of each cell that contains '1' (land).

Steps in DFS for Counting Islands:
Start at an unvisited land cell (a '1' in the grid).
Mark the cell as visited (e.g., change it to '0' or use a separate visited structure).
Recursively apply DFS to all its adjacent cells (up, down, left, right).
Continue the process until all connected cells of the island are visited.
Repeat for each unvisited land cell in the grid.

--------------------------------------------------------------------------------------
def dfs(i, j, grid):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
        return
    grid[i][j] = '0'  # Mark as visited
    # Explore all adjacent cells
    dfs(i + 1, j, grid)
    dfs(i - 1, j, grid)
    dfs(i, j + 1, grid)
    dfs(i, j - 1, grid)

def numIslands(grid):
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j, grid)
    return count
--------------------------------------------------------------------------------------

Breadth-First Search (BFS)
Concept:
BFS is another algorithm for traversing or searching tree or graph data structures.
It starts at the root (or an arbitrary node) and explores the neighbor nodes at the present depth before moving on to nodes at the next depth level.
In the context of a 2D grid, it involves iteratively visiting all neighboring cells (up, down, left, right) using a queue.

Steps in BFS for Counting Islands:
Start at an unvisited land cell (a '1' in the grid).
Use a queue to manage the cells to be visited.
Mark the cell as visited and enqueue its adjacent cells (up, down, left, right).
Dequeue a cell, mark it as visited, and enqueue its unvisited adjacent cells.
Continue until all connected cells of the island are visited.
Repeat for each unvisited land cell in the grid.

--------------------------------------------------------------------------------------
from collections import deque

def bfs(i, j, grid):
    queue = deque([(i, j)])
    grid[i][j] = '0'  # Mark as visited
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
                grid[nx][ny] = '0'
                queue.append((nx, ny))

def numIslands(grid):
    if not grid:
        return 0
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                count += 1
                bfs(i, j, grid)
    return count
--------------------------------------------------------------------------------------

Summary:
DFS explores as far as possible along each branch before backtracking. It uses a stack (either the call stack in the recursive implementation or an explicit stack) to keep track of the next cell to visit.
BFS explores all neighbors at the present depth before moving on to nodes at the next depth level. It uses a queue to manage the cells to be visited next.
Both algorithms can be used to solve the problem of counting islands in a grid, with the choice depending on the specific requirements or constraints of the problem (e.g., iterative vs. recursive implementation).


"""

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        def dfs(i, j):
            if i<0 or j<0 or i>=len(grid) or j >= len(grid[0]) or grid[i][j] == '0': # This line is a conditional check that determines whether the DFS should continue exploring from the current cell
                return
            grid[i][j] = '0'
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)


        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j)
        return count
    
    
"""
# --------------------------------------------------------------------------------------
# Variant of the problem: Number of Islands II (HARD)
# --------------------------------------------------------------------------------------
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Union Find Data Structure (Disjoint Set) appraoch
"""    

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.count = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            self.count -= 1

    def addLand(self, x):
        if self.parent[x] == x:
            self.count += 1 

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def getIndex(x, y):
            return x * n + y
    
        uf = UnionFind(m * n)
        grid = [[0] * n for _ in range(m)]
        answer = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for r, c in positions:
            if grid[r][c] == 1:
                answer.append(uf.count)
                continue
            
            grid[r][c] = 1
            index = getIndex(r, c)
            uf.addLand(index)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    uf.union(index, getIndex(nr, nc))
            
            answer.append(uf.count)
        
        return answer