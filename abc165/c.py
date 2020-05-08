import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
import copy
def f(A, x, N, M, A_list):
    if len(A) == N:
        A_list.append(A)
        return
    A.append(x)
    for i in range(x, M+1):
        A_copy = copy.copy(A)
        f(A_copy, i, N, M, A_list)
def main():
    N, M, Q = map(int, input().split())
    q_list = []
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        q_list.append((a, b, c, d))
    # A = combinations_with_replacement(range(1, M+1), N)
    A_list = []
    f([], 1, N, M, A_list)
    ans = 0
    for Ai in A_list:
        v = 0
        Ai = list(map(int, Ai))
        for a, b, c, d in q_list:
            if Ai[b-1]-Ai[a-1] == c:v += d
        ans = max(ans, v)
    print(ans)
if __name__ == "__main__":
    main()