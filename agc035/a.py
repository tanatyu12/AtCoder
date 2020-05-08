import sys
input = sys.stdin.readline
from collections import Counter
def judge(vals):
    return vals[0] ^ vals[1] ^ vals[2] == 0
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = "No"
    c = Counter(A)
    con1 = len(c) == 2 and c[0] * 3 == N
    items = list(c.items())
    con2 = len(c) == 3 and items[0][1] * 3 == N and items[1][1] * 3 == N and judge(list(c.keys()))
    con3 = c[0] == N
    if con1 or con2 or con3:ans = "Yes"
    print(ans)
if __name__ == "__main__":
    main()