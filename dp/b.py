# dp array
import sys
input = sys.stdin.readline
def chmin(dp, idx, b):
    if dp[idx] > b:
        dp[idx] = b
        return True
    return False
def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    INF = 10 ** 9
    dp = [INF] * N
    dp[0] = 0
    for i in range(N):
        for j in range(1, K+1):
            if i+j < N:chmin(dp, i+j, dp[i]+abs(h[i]-h[i+j]))
    print(dp[-1])
if __name__ == "__main__":
    main()