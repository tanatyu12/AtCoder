import sys
input = sys.stdin.readline
from collections import deque
def main():
    N, M = map(int, input().split())
    graph = {}
    for i in range(N):
        graph[i] = set()
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A-1].add(B-1)
        graph[B-1].add(A-1)
    que = deque([])
    que.append(0)
    seen = [0 for _ in range(N)]
    ans = [0 for _ in range(N)]
    while len(que) != 0:
        v = que.popleft()
        for node in graph[v]:
            if seen[node] == 1:continue
            ans[node] = v
            seen[node] = 1
            que.append(node)
    is_ok = True
    for i in range(N):
        if seen[i] == 0:
            is_ok = False
            break
    if is_ok:
        print("Yes")
    else:
        print("No")
    if is_ok:
        for i, a in enumerate(ans):
            if i == 0:continue
            print(a+1)
if __name__ == "__main__":
    main()