import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    s = [0] * (N+1)
    for i in range(N):
        s[i+1] = s[i] + A[i]
    ans = 0
    for v in Counter(s).values():
        ans += (v * (v-1) // 2)
    print(ans)
if __name__ == "__main__":
    main()