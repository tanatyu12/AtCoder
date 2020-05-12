# doubling
import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    TO_MAX = 60
    to = [[0 for _ in range(N)] for _ in range(TO_MAX+1)]
    for i in range(N):
        to[0][i] = A[i]-1
    for i in range(TO_MAX):
        for j in range(N):
            to[i+1][j] = to[i][to[i][j]]
    v = 0
    for i in range(TO_MAX+1)[::-1]:
        l = pow(2, i)
        if l <= K:
            v = to[i][v]
            K -= l
    print(v+1)   
if __name__ == "__main__":
    main()