import sys
input = sys.stdin.readline
def chmin(dp, i, j, b):
    if dp[i][j] > b:
        dp[i][j] = b
        return True
    return False
def main():
    N, W = map(int, input().split())
    goods = []
    INF = 10 ** 9 + 1
    for _ in range(N):
        goods.append(list(map(int, input().split())))
    dp = [[INF for _ in range(100001)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        w, v = goods[i][0], goods[i][1]
        for j in range(100001):
            chmin(dp, i+1, j, dp[i][j])
            if j-v >= 0:chmin(dp, i+1, j, dp[i][j-v]+w)
    ans = 0
    for i in range(100001):
        if dp[N][i] <= W:ans = i
    print(ans)
if __name__ == "__main__":
    main()