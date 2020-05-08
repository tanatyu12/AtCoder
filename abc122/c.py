import sys
input = sys.stdin.readline
def main():
    N, Q = map(int, input().split())
    S = input().rstrip("\r\n")
    s = [0] * (N+1)
    s[0] = 0
    s[1] = 0
    for i in range(1, N):
        exists_AC = (S[i-1] == "A" and S[i] == "C")
        s[i+1] = s[i] + int(exists_AC)
    for _ in range(Q):
        l, r = map(int, input().split())
        print(s[r]-s[l])
if __name__ == "__main__":
    main()