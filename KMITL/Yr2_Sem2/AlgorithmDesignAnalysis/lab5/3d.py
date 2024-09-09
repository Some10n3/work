from collections import deque
 
def min_cookies_for_escape_interactive():
    N, M = map(int, input().split())
 
    maze = []
    for _ in range(N):
        row = list(map(int, input().split()))
        maze.append(row)
 
    # Initialize the dp array with infinity and set the starting point
    dp = [[float('inf')] * M for _ in range(N)]
    dp[0][0] = maze[0][0]
 
    # Use BFS to update the dp array
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
 
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if dp[nx][ny] > dp[x][y] + maze[nx][ny]:
                    dp[nx][ny] = dp[x][y] + maze[nx][ny]
                    queue.append((nx, ny))
 
    # The minimum number of cookies required to escape
    return dp[N - 1][M - 1]
 
result = min_cookies_for_escape_interactive()
print(result)