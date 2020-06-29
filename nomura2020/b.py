import sys
input = sys.stdin.readline
def main():
    T = list(input().rstrip())
    ans = ["D" if c == "?" else c for c in T]
    print("".join(ans))
if __name__ == "__main__":
    main()