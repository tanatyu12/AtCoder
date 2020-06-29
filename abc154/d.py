import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    com = [0] * (N+1)
    for i in range(N):
        com[i+1] = (1+p[i]) / 2 + com[i]
    for i in range(K, N+1):
        ans = max(ans, com[i]-com[i-K])
    print(ans)
if __name__ == "__main__":
    main()