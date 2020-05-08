import sys
input = sys.stdin.readline
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
    N, P = map(int, input().split())
    res = prime_factorize(P)
    ans = 1
    for x, ex in res:
        ans *= max(1, x ** (ex // N))
    print(ans)
if __name__ == "__main__":
    main()