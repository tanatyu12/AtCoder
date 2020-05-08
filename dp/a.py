# dp array
import sys
input = sys.stdin.readline
def chmin(dp, idx, b):
    if dp[idx] > b:
        dp[idx] = b
        return True
    return False
def main():
    N = int(input())
    h = list(map(int, input().split()))
    INF = 10 ** 9
    dp = [INF] * N
    dp[0] = 0
    dp[1] = abs(h[0]-h[1])
    for i in range(2, N):
        chmin(dp, i, dp[i-1]+abs(h[i]-h[i-1]))
        chmin(dp, i, dp[i-2]+abs(h[i]-h[i-2]))
    print(dp[-1])
if __name__ == "__main__":
    main()