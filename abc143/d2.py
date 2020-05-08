# 二分探索
import sys
input = sys.stdin.readline
import bisect
def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N-2):
        for j in range(i+1, N-1):
            idx = bisect.bisect_left(L, L[i]+L[j], j+1, N)
            ans += idx-j-1
    print(ans)
if __name__ == "__main__":
    main()