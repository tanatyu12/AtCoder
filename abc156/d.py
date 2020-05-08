import sys
input = sys.stdin.readline
def cmb(a, b, mod):
    m, n = 1, 1
    b = min(b, a-b)
    for i in range(1, b+1):
        m *= (a-i+1)
        m %= mod
        n *= i
        n %= mod
    return m * pow(n, mod-2, mod) % mod
def main():
    n, a, b = map(int, input().split())
    mod = 10 ** 9 + 7
    total = pow(2, n, mod) - 1
    cmb1 = cmb(n, a, mod)
    cmb2 = cmb(n, b, mod)
    ans = total - cmb1 - cmb2
    ans %= mod
    print(ans)
if __name__ == "__main__":
    main()