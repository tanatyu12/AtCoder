import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N, P = map(int, input().split())
    S = list(map(int, input().rstrip("\r\n")))
    S.reverse()
    ans = 0
    if P == 2 or P == 5:
        for i in range(N):
            if S[i] % P == 0:ans += N-i
    else:
        A = [0] * N
        tenpow = 1
        for i in range(N):
            A[i] = (S[i]*tenpow) % P
            tenpow *= 10
            tenpow %= P
        D = [0] * (N+1)
        for i in range(N):
            D[i+1] = (D[i] + A[i]) % P
        c = Counter(D)
        for v in c.values():
            ans += v*(v-1)//2
    print(ans)
if __name__ == "__main__":
    main()