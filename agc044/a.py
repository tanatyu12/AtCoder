import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def main():
    T = int(input())
    for _ in range(T):
        N, A, B, C, D = map(int, input().split())
        memo = {}

        def f(n):
            if n == 0:return 0
            if n == 1:return D
            if n in memo:return memo[n]

            ret = min(
                D * n,
                D * (n%2) + A + f(n//2),
                D * abs(n - (n+1)//2*2) + A + f((n+1)//2),
                D * (n%3) + B + f(n//3),
                D * abs(n - (n+2)//3*3) + B + f((n+2)//3),
                D * (n%5) + C + f(n//5),
                D * abs(n - (n+4)//5*5) + C + f((n+4)//5)
            )

            memo[n] = ret
            return ret
        print(f(N))
if __name__ == "__main__":
    main()