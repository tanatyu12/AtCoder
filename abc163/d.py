import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    a = [i for i in range(N+1)]
    s = [0] * (N+2)
    for i in range(N+1):
        s[i+1] = s[i] + a[i]
    ans = 0
    MOD = 10**9+7
    for i in range(K, N+2):
        ans += (s[-1]-s[-i-1]-s[i]+1) % MOD
    print(ans % MOD)
if __name__ == "__main__":
    main()