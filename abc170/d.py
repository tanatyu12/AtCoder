import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = Counter(A)
    A.sort()
    ans = set()
    table = {i:-1 for i in range(1, 10 ** 6 + 1)}
    for a in A:
        table[a] = 0
    for a in A:
        if table[a] == 0 and cnt[a] == 1:
            ans.add(a)
        elif table[a] == 1:
            continue
        i = 2
        target = a
        while True:
            target = a * i
            if target > A[-1]:
                break
            if table[target] == 0:
                table[target] = 1
            i += 1
    print(len(ans))
if __name__ == "__main__":
    main()