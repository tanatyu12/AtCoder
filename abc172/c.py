import sys
input = sys.stdin.readline
import bisect
def main():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    cum_a = [0] * (N + 1)
    for i in range(N):
        cum_a[i+1] = cum_a[i] + A[i]
    cum_b = [0] * (M + 1)
    for i in range(M):
        cum_b[i+1] = cum_b[i] + B[i]
    ans = 0
    for i in range(N+1):
        rest = K - cum_a[i]
        if rest < 0:break
        b_idx = bisect.bisect_right(cum_b, rest)
        ans = max(ans, i + b_idx - 1)
    print(ans)
if __name__ == "__main__":
    main()