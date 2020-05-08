import sys
input = sys.stdin.readline
def main():
    N = int(input())
    ans = set()
    for _ in range(N):
        s = input().rstrip("\r\n")
        ans.add(s)
    print(len(ans))
if __name__ == "__main__":
    main()