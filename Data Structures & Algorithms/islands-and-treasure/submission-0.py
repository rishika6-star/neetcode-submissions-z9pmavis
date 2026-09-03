from collections import deque

class Solution:
    def islandsAndTreasure(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        INF = 2147483647
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        directions = [
            (1, 0),   # down
            (-1, 0),  # up
            (0, 1),   # right
            (0, -1)   # left
        ]

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Check boundaries
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue

                # Skip water and already visited cells
                if grid[nr][nc] != INF:
                    continue

                # Distance = current distance + 1
                grid[nr][nc] = grid[r][c] + 1

                # Add the cell to queue
                queue.append((nr, nc))

        