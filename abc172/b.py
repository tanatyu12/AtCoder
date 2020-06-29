import sys
input = sys.stdin.readline
def main():
    S = input().rstrip()
    T = input().rstrip()
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()