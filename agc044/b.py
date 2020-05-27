import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int(input())
    P = list(map(int, input().split()))
    costs = [-1 for _ in range(N**2)]
    sit = [1 for _ in range(N**2)]
    for i in range(N**2):
        q, mod = divmod(i, N)
        up, down, left, right = q, N-q-1, mod, N-mod-1
        costs[i] = min(up, down, left, right)
    ans = 0
    for p in P:
        ans += costs[p-1]
        sit[p-1] = 0
        que = deque([])
        que.append((p-1, costs[p-1]))
        while len(que) != 0:
            v, d = que.popleft()
            if v > N and costs[v-N] > d:
                costs[v-N] = d
                que.append((v-N, d+sit[v-N]))
            if v < N**2-N-1 and costs[v+N] > d:
                costs[v+N] = d
                que.append((v+N, d+sit[v+N]))
            if v % N != 0 and costs[v-1] > d:
                costs[v-1] = d
                que.append((v-1, d+sit[v-1]))
            if (v+1) % N != 0 and costs[v+1] > d:
                costs[v+1] = d
                que.append((v+1, d+sit[v+1]))
    print(ans)
if __name__ == "__main__":
    main()