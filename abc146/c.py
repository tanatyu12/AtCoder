import sys
input = sys.stdin.readline
import math
def can_buy(N, A, B, d, X):
    if X >= A * N + B * d:
        return True
    else:
        return False
def binary_search(ok, ng, A, B, X):
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        d = math.floor(math.log10(mid))+1
        if can_buy(mid, A, B, d, X):
            ok = mid
        else:
            ng = mid
    return ok
def main():
    A, B, X = map(int, input().split())
    MAX = 10 ** 9
    ans = 0
    ok = 0
    ng = MAX + 1
    ans = binary_search(ok, ng, A, B, X)
    print(ans)
if __name__ == "__main__":
    main()