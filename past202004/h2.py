# DP ver
import sys
input = sys.stdin.readline
def chmin(dp, i, j, b):
    if dp[i][j] > b:
        dp[i][j] = b
        return True
    return False
def main():
    N, M = map(int, input().split())
    A = [input().rstrip() for _ in range(N)]
    indices = [[] for _ in range(11)]
    for i in range(N):
        for j in range(M):
            if A[i][j] == "S":
                indices[0].append((i, j))
            elif A[i][j] == "G":
                indices[10].append((i, j))
            else:
                indices[int(A[i][j])].append((i, j))
    INF = 10**9
    dp = [[INF for _ in range(M)] for _ in range(N)]
    start_n, start_m = indices[0][0]
    dp[start_n][start_m] = 0
    exists_path = True
    for i in range(1, 11):
        if len(indices[i]) == 0:
            exists_path = False
            break
        for to_n, to_m in indices[i]:
            for from_n, from_m in indices[i-1]:
                cost = abs(to_n-from_n) + abs(to_m-from_m) + dp[from_n][from_m]
                chmin(dp, to_n, to_m, cost)
    if exists_path:
        goal_n, goal_m = indices[10][0]
        print(dp[goal_n][goal_m])
    else:
        print(-1)
if __name__ == "__main__":
    main()