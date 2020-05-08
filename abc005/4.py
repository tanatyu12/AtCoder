import sys
input = sys.stdin.readline
def main():
    N = int(input())
    s = []
    s.append([0 for _ in range(N+1)])
    for _ in range(N):
        s.append([0] + list(map(int, input().split())))
    for i in range(N+1):
        for j in range(N+1):
            if i: s[i][j] += s[i-1][j]
    for i in range(N+1):
        for j in range(N+1):
            if j: s[i][j] += s[i][j-1]
    vals = [0] * (N*N+1)
    for x1 in range(N+1):
        for x2 in range(N+1):
            for y1 in range(N+1):
                for y2 in range(N+1):
                    area = (x2-x1) * (y2-y1)
                    val = s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]
                    vals[area] = max(vals[area], val)
    Q = int(input())
    for _ in range(Q):
        p = int(input())
        ans = 0
        for i in range(p+1):
            ans = max(ans, vals[i])
        print(ans)

if __name__ == "__main__":
    main()