import sys
input = sys.stdin.readline
def chmax(dp, i, j, b):
    if dp[i][j] < b:
        dp[i][j] = b
        return True
    return False
def main():
    N, W = map(int, input().split())
    goods = []
    for _ in range(N):
        goods.append(list(map(int, input().split())))
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(N):
        w, v = goods[i][0], goods[i][1]
        for j in range(W+1):
            chmax(dp, i+1, j, dp[i][j])
            if j-w >= 0:chmax(dp, i+1, j, dp[i][j-w]+v)
    print(dp[-1][-1])
if __name__ == "__main__":
    main()