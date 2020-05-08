import sys
input = sys.stdin.readline
def main():
    A, B, C, D = map(int, input().split())
    ans = "Yes"
    while A > 0 or C > 0:
        C -= B
        if C <= 0:
            break
        A -= D
        if A <= 0:
            ans = "No"
            break
    print(ans)
if __name__ == "__main__":
    main()