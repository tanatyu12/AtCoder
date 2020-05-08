import sys
input = sys.stdin.readline
def main():
    x, y = map(int, input().split())
    ans = abs(abs(x) - abs(y))
    if x * y < 0:
        ans += 1
    elif x > y and x * y == 0:
        ans += 1
    elif x > y:
        ans += 2
    print(ans)
if __name__ == "__main__":
    main()