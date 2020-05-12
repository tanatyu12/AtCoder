# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
INF = 10 ** 9 + 100
ans = INF
def dfs(i, S, cost, C_list, A_list, N, M, X):
    global ans
    if i == N:
        ok = True
        for j in range(M):
            if S[j] < X:
                ok = False
                break
        if ok:ans = min(ans, cost)
        return
    dfs(i+1, S, cost, C_list, A_list, N, M, X)
    for j in range(M):
        S[j] += A_list[i][j]
    cost += C_list[i]
    dfs(i+1, S, cost, C_list, A_list, N, M, X)
    for j in range(M):
        S[j] -= A_list[i][j]
    cost -= C_list[i]
def main():
    global INF, ans
    N, M, X = map(int, input().split())
    C_list = []
    A_list = []
    for _ in range(N):
        C_A = list(map(int, input().split()))
        C_list.append(C_A[0])
        A_list.append(C_A[1:])
    S = [0 for _ in range(M)]
    cost = 0
    dfs(0, S, cost, C_list, A_list, N, M, X)
    if ans == INF:ans = -1
    print(ans)
if __name__ == "__main__":
    main()