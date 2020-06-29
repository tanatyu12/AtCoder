import sys
input = sys.stdin.readline
def main():
    A, R, N = map(int, input().split())
    ans = A
    INF = 10 ** 9
    is_over = False
    for _ in range(1, N):
        ans *= R
        if ans > INF:
            is_over = True
            break
    if is_over:
        print("large")
    else:
        print(ans)
if __name__ == "__main__":
    main()