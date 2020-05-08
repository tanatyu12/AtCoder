import sys
input = sys.stdin.readline
def main():
    x = int(input())
    ans = (x//11)*2
    rest = (x % 11)
    if rest > 6:
        ans += 2
    elif 0 < rest <= 6:
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()