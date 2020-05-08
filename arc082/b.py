import sys
input = sys.stdin.readline
def main():
    N = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i+1 == p[i]:
            tmp = p[i]
            if i == N-1:
                p[i] = p[i-1]
                p[i-1] = tmp
            else:
                p[i] = p[i+1]
                p[i+1] = tmp
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()