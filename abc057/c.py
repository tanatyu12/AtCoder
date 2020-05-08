import sys
input = sys.stdin.readline
def enum_divisors(n):
    res = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            res.append(i)
            res.append(n//i)
    return res
def f(a, b):
    return max(len(str(a)), len(str(b)))
def main():
    N = int(input())
    divisors = enum_divisors(N)
    ans = 10**8
    for i in range(len(divisors)-1):
        ans = min(ans, f(divisors[i], divisors[i+1]))
    print(ans)
if __name__ == "__main__":
    main()