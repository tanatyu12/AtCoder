import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)
    total = sum(A)
    Q = int(input())
    for _ in range(Q):
        B, C = map(int, input().split())
        total = total + (C - B) * cnt[B]
        cnt[C] += cnt[B]
        cnt[B] = 0
        print(total)
if __name__ == "__main__":
    main()