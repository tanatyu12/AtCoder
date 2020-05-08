import sys
input = sys.stdin.readline
def main():
    S, L, R = map(int, input().split())
    if S < L:
        print(L)
    elif L <= S <= R:
        print(S)
    else:
        print(R)
if __name__ == "__main__":
    main()