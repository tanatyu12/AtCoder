import sys
input = sys.stdin.readline
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n//i)
    return divisors
def main():
    n = int(input())
    ans = 10**9
    for i in range(1, n+1):
        divisors = make_divisors(i)
        for j in range(len(divisors)-1):
            ans = min(ans, abs(divisors[j]-divisors[j+1])+n-i)
    print(ans)
if __name__ == "__main__":
    main()