from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        num_islands = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_islands += 1
                    # start bfs
                    bfs_q = deque()
                    bfs_q.append((i, j))
                    while len(bfs_q) > 0:
                        # print(f"inner q: {bfs_q}")
                        k, l = bfs_q.popleft()
                        if grid[k][l] == "0":
                            continue
                        else:
                            grid[k][l] = "0"
                            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                                k_n, l_n = k + dx, l + dy
                                if not (0 <= k_n < m and 0 <= l_n < n):
                                    continue
                                bfs_q.append((k_n, l_n))
        return num_islands
