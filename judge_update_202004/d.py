import sys
input = sys.stdin.readline
from math import gcd
def main():
    N, _ = map(int, input().split())
    A = list(map(int, input().split()))
    S = list(map(int, input().split()))
    g = [0] * N
    g[0] = A[0]
    for i in range(1, N):
        g[i] = gcd(A[i], g[i-1])
    for s in S:
        tmp = gcd(s, g[-1])
        if tmp != 1:
            print(tmp)
        else:
            left = 0
            right = N
            while left < right:
                m = (left + right) // 2
                if gcd(g[m], s) == 1:
                    right = m
                else:
                    left = m + 1
            print(left + 1)
if __name__ == "__main__":
    main()