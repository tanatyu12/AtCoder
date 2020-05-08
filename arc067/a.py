import sys
input = sys.stdin.readline
def prime_factorize(n, ex_table):
    for i in range(2, int(n**0.5)+1):
        if n % i != 0:continue
        while n % i == 0:
            ex_table[i] += 1
            n = n//i
    if n != 1:ex_table[n] += 1
def main():
    N = int(input())
    ex_table = {i:0 for i in range(2, N+1)}
    for i in range(1, N+1):
        prime_factorize(i, ex_table)
    ans = 1
    MOD = 10 ** 9 + 7
    for k in ex_table:
        ans *= (ex_table[k] + 1)
        ans %= MOD
    print(ans)
if __name__ == "__main__":
    main()