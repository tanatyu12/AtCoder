import sys
input = sys.stdin.readline
def main():
    S = list(input().rstrip())
    ok = False
    ans = len(S)
    while not ok:
        S.pop()
        ans -= 1
        if len(S) % 2 == 0 and S[:len(S)//2] == S[len(S)//2:]:
            ok = True
    print(ans)
if __name__ == "__main__":
    main()