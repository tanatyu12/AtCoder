import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    ans = N
    for i in range(M):
        ans -= A[i]
    if ans < 0:ans = -1
    print(ans)
if __name__ == "__main__":
    main()