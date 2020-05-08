import sys
input = sys.stdin.readline
def main():
    N = input().rstrip("\r\n")
    ans = "No"
    for s in N:
        if s == "7":
            ans = "Yes"
            break
    print(ans)
if __name__ == "__main__":
    main()