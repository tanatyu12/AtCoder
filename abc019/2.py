import sys
input = sys.stdin.readline
from itertools import groupby
def main():
    S = input().rstrip("\r\n")
    g = groupby(S)
    ans = ""
    for gi in g:
        l = list(gi[1])
        ans += gi[0]+str(len(l))
    print(ans)
if __name__ == "__main__":
    main()