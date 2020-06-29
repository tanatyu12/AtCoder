import sys
input = sys.stdin.readline
def main():
    inp = list(map(int, input().split()))
    ans = -1
    for i, x in enumerate(inp):
        if x == 0:
            ans = i + 1
    print(ans)
if __name__ == "__main__":
    main()