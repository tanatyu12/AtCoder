import sys
input = sys.stdin.readline
from fractions import gcd
def main():
    A, B = map(int, input().split())
    g = gcd(A, B)
    ans = A // g * B
    print(ans)
if __name__ == "__main__":
    main()