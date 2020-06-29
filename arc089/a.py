import sys
input = sys.stdin.readline
def main():
    N = int(input())
    lis = []
    lis.append((0, 0, 0))
    for _ in range(N):
        t, x, y = map(int, input().split())
        lis.append((t, x, y))
    ans = "Yes"
    for i in range(1, N+1):
        t_diff = lis[i][0] - lis[i-1][0]
        d_diff = abs(lis[i][1] - lis[i-1][1]) + abs(lis[i][2] - lis[i-1][2])
        if t_diff % 2 != d_diff % 2 or t_diff < d_diff:
            ans = "No"
            break
    print(ans)
if __name__ == "__main__":
    main()