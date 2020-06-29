import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    INF = 10 ** 18
    ans = 1
    is_INF = False
    for a in A:
        ans *= a
        if ans > INF:
            is_INF = True
            break
    if is_INF:
        if 0 in A:
            print(0)
        else:
            print(-1)
    else:
        print(ans)
if __name__ == "__main__":
    main()