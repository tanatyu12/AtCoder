import sys
input = sys.stdin.readline
from itertools import groupby
def main():
    N = int(input())
    S = input().rstrip("\r\n")
    print(len(list(groupby(S))))
if __name__ == "__main__":
    main()