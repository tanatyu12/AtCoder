import sys
input = sys.stdin.readline
from collections import deque
def main():
    H, W = map(int, input().split())
    field = [input().rstrip("\r\n") for _ in range(H)]
    dv = 201
    counts = [[dv for _ in range(W)] for _ in range(H)]
    que = deque([(0, 0)])
    if field[0][0] == "#":
        counts[0][0] = 1
    else:
        counts[0][0] = 0
    while len(que) > 0:
        h, w = que.popleft()
        for dh, dw in [(1, 0), (0, 1)]:
            nh, nw = h + dh, w + dw
            if nh >= H or nw >= W:continue
            if counts[nh][nw] == dv:que.append((nh, nw))
            if field[h][w] != field[nh][nw]:
                counts[nh][nw] = min(counts[nh][nw], counts[h][w]+1)
            else:
                counts[nh][nw] = min(counts[nh][nw], counts[h][w])
    if field[-1][-1] == "#":counts[-1][-1] += 1
    print(counts[-1][-1]//2)
if __name__ == "__main__":
    main()