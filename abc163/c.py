import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = Counter(A)
    for i in range(1, N+1):
        print(c[i])
if __name__ == "__main__":
    main()