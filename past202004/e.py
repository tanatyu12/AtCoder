import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N):
        x = i + 1
        j = 0
        ok = False
        while not ok:
            x = A[x-1]
            j += 1
            if x == i + 1:ok = True
        ans[i] = j
    print(" ".join(map(str, ans)))
if __name__ == "__main__":
    main()