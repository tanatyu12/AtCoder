import sys
input = sys.stdin.readline
def main():
    N = int(input())
    ans = 0
    if N % 1000 == 0:
        ans = 0
    else:
        ans = 1000 - (N+1000) % 1000
    print(ans)
if __name__ == "__main__":
    main()