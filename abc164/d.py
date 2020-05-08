import sys
input = sys.stdin.readline
from collections import Counter
def main():
    S = list(map(int, input().rstrip("\r\n")))
    N = len(S)
    P = 2019
    S.reverse()
    ans = 0
    if P == 2 or P == 5:
        for i in range(N):
            if S[i] % P == 0:ans += N-i
    else:
        D = [0] * (N+1)
        tenpow = 1
        for i in range(N):
            S[i] = S[i] * tenpow % P
            tenpow *= 10
            tenpow %= P
            D[i+1] = (S[i] + D[i]) % P
        c = Counter(D)
        for v in c.values():
            ans += v*(v-1)//2
    print(ans)
if __name__ == "__main__":
    main()