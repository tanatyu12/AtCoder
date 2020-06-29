import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, X, Y = map(int, input().split())
    grid = [["." for _ in range(403)] for _ in range(403)]
    for _ in range(N):
        x, y = map(int, input().split())
        grid[y+201][x+201] = "#"
    que = deque([])
    que.append((201, 201))
    dist = [[-1 for _ in range(403)] for _ in range(403)]
    dist[201][201] = 0
    while len(que) != 0:
        vx, vy = que.popleft()
        if vx == X + 201 and vy == Y + 201:
            break
        if vx + 1 < 403 and vy + 1 < 403 and dist[vy+1][vx+1] == -1 and grid[vy+1][vx+1] == ".":
            que.append((vx+1, vy+1))
            dist[vy+1][vx+1] = dist[vy][vx] + 1
        if vy + 1 < 403 and dist[vy+1][vx] == -1 and grid[vy+1][vx] == ".":
            que.append((vx, vy+1))
            dist[vy+1][vx] = dist[vy][vx] + 1
        if vx - 1 >= 0 and vy + 1 < 403 and dist[vy+1][vx-1] == -1 and grid[vy+1][vx-1] == ".":
            que.append((vx-1, vy+1))
            dist[vy+1][vx-1] = dist[vy][vx] + 1
        if vx + 1 < 403 and dist[vy][vx+1] == -1 and grid[vy][vx+1] == ".":
            que.append((vx+1, vy))
            dist[vy][vx+1] = dist[vy][vx] + 1
        if vx - 1 >= 0 and dist[vy][vx-1] == -1 and grid[vy][vx-1] == ".":
            que.append((vx-1, vy))
            dist[vy][vx-1] = dist[vy][vx] + 1
        if vy - 1 >= 0 and dist[vy-1][vx] == -1 and grid[vy-1][vx] == ".":
            que.append((vx, vy-1))
            dist[vy-1][vx] = dist[vy][vx] + 1
    print(dist[Y+201][X+201])
if __name__ == "__main__":
    main()