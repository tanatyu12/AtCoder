import sys
input = sys.stdin.readline
def main():
    A, B, C, K = map(int, input().split())
    rest = K
    ans = 0
    ans += min(A, rest)
    if K > A:
        rest -= A
        if rest > B:
            rest -= B
            ans -= min(rest, C)
    print(ans)
if __name__ == "__main__":
    main()