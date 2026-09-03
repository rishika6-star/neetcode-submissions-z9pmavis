from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0

        # Find all rotten fruits and count fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0

        directions = [
            (1, 0),    # down
            (-1, 0),   # up
            (0, 1),    # right
            (0, -1)    # left
        ]

        # BFS
        while queue and fresh > 0:

            # Process everything that is rotten
            # at the current minute
            for _ in range(len(queue)):

                r, c = queue.popleft()

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Check boundaries
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue

                    # Only fresh fruits can become rotten
                    if grid[nr][nc] != 1:
                        continue

                    # Make it rotten
                    grid[nr][nc] = 2
                    fresh -= 1

                    # Process it in the next minute
                    queue.append((nr, nc))

            minutes += 1

        # If fresh fruits are still remaining,
        # they cannot be reached
        if fresh > 0:
            return -1

        return minutes





    