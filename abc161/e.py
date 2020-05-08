import sys
input = sys.stdin.readline
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors
def main():
    N = int(input())
    divisors = make_divisors(N)
    divisors2 = make_divisors(N-1)
    print(len(divisors)+len(divisors2))
if __name__ == "__main__":
    main()