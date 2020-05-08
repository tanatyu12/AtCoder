import sys
input = sys.stdin.readline
from collections import deque
from collections import Counter
def main():
    N, X, Y = map(int, input().split())
    graph = {}
    for i in range(N):
        graph[i] = set()
    for i in range(N-1):
        graph[i].add(i+1)
        graph[i+1].add(i)
    graph[X-1].add(Y-1)
    graph[Y-1].add(X-1)

    ans = []
    for i in range(N):
        dist = [-1] * N
        dist[i] = 0
        que = deque([])
        que.append(i)
        while len(que) != 0:
            v = que.popleft()
            for nv in graph[v]:
                if dist[nv] != -1:continue
                dist[nv] = dist[v] + 1
                que.append(nv)
        ans += dist
    ans = Counter(ans)
    for i in range(1, N):
        print(ans[i]//2)
if __name__ == "__main__":
    main()