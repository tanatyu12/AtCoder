import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def main():
    N = int(input())
    S = input().rstrip("\r\n")
    R = []
    G = []
    B = []
    for i, s in enumerate(S):
        if s == "R":
            R.append(i)
        elif s == "G":
            G.append(i)
        else:
            B.append(i)
    ans = len(R) * len(G) * len(B)
    for i in range(N):
        for j in range(i+1, N):
            k = 2 * j - i
            if k >= N:continue
            if S[i] != S[j] and S[j] != S[k] and S[k] != S[i]:
                ans -= 1
    print(ans)
if __name__ == "__main__":
    main()