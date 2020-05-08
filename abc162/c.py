import sys
input = sys.stdin.readline
from math import gcd
def main():
    K = int(input())
    ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            for k in range(1, K+1):
                g = gcd(i, j)
                g = gcd(g, k)
                ans += g
    print(ans)
if __name__ == "__main__":
    main()