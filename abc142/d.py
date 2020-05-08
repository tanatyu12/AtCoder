import sys
input = sys.stdin.readline
from fractions import gcd
def prime_factorize(n):
    res = []
    for i in range(2, int(n**0.5)+1):
        if n % i != 0:continue
        ex = 0
        while n % i == 0:
            ex += 1
            n = n//i
        res.append((i, ex))
    if n != 1:res.append((n, 1))
    return res
def main():
    A, B = map(int, input().split())
    g = gcd(A, B)
    res = prime_factorize(g)
    ans = len(res) + 1
    print(ans)
if __name__ == "__main__":
    main()