import sys
input = sys.stdin.readline
def main():
    A, B = map(int, input().split())
    ans = 10001
    for x in range(1, 10001):
        if 0 <= 8*x - 100*A < 100 and 0 <= 10*x - 100*B < 100:
            ans = min(ans, x)
    if ans == 10001:ans = -1
    print(ans)
if __name__ == "__main__":
    main()