import sys
input = sys.stdin.readline
def main():
    X, Y = map(int, input().split())
    ans = "No"
    for i in range(101):
        for j in range(101):
            if i + j == X and 2 * i + 4 * j == Y:
                ans = "Yes"
                break
    print(ans)
if __name__ == "__main__":
    main()