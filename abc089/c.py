import sys
input = sys.stdin.readline
from itertools import combinations
from collections import Counter
def main():
    N = int(input())
    s = Counter()
    for _ in range(N):
        s[input().rstrip("\r\n")[0]] += 1
    print(sum([s[a]*s[b]*s[c] for a,b,c in combinations("MARCH",3)]))
if __name__ == "__main__":
    main()