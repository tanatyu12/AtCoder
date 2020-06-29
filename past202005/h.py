import sys
input = sys.stdin.readline
def chmin(dp, idx, b):
    if dp[idx] > b:
        dp[idx] = b
        return True
    return False
def main():
    N, L = map(int, input().split())
    x = list(map(int, input().split()))
    T = list(map(int, input().split()))
    INF = 10 ** 9
    dp = [INF for _ in range(L+4)]
    dp[0] = 0
    next_hurdle = 0
    for i in range(L):
        if next_hurdle < N and i == x[next_hurdle]:
            chmin(dp, i+1, dp[i]+T[0]+T[2])
            chmin(dp, i+2, dp[i]+T[0]+T[1]+T[2])
            chmin(dp, i+4, dp[i]+T[0]+T[1]*3+T[2])
            next_hurdle += 1
        else:
            chmin(dp, i+1, dp[i]+T[0])
            if i + 2 <= L:
                chmin(dp, i+2, dp[i]+T[0]+T[1])
            elif i + 1 == L:
                chmin(dp, i+2, dp[i]+T[0]//2+T[1]//2)
            if i + 4 <= L:
                chmin(dp, i+4, dp[i]+T[0]+T[1]*3)
            elif i + 3 == L:
                chmin(dp, i+4, dp[i]+T[0]//2+T[1]*2+T[1]//2)
            elif i + 2 == L:
                chmin(dp, i+4, dp[i]+T[0]//2+T[1]+T[1]//2)
    ans = min(dp[L], dp[L+1], dp[L+2], dp[L+3])
    print(ans)
if __name__ == "__main__":
    main()