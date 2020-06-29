import sys
input = sys.stdin.readline
import bisect
def main():
    N = int(input())
    a = []
    for _ in range(N):
        ai = list(input().rstrip())
        a.append(ai)
    ans_left = []
    ans_right = []
    can_build = True
    for i in range(N//2, N):
        a[i].sort()
    for i in range(N//2):
        for j in range(N):
            idx = bisect.bisect_left(a[N-i-1], a[i][j])
            if -1 < idx < N and a[i][j] == a[N-i-1][idx]:
                ans_left.append(a[i][j])
                ans_right.append(a[N-i-1][idx])
                break
            else:
                continue
        if len(ans_left) < i+1:
            can_build = False
            break
    if not can_build:
        print(-1)
    else:
        if N % 2 == 1:
            ans_left.append(a[N//2][0])
        ans = ans_left + ans_right[::-1]
        print("".join(ans))
if __name__ == "__main__":
    main()