import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    ans = [1 for i in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        if H[a-1] > H[b-1]:
            ans[b-1] = 0
        elif H[a-1] < H[b-1]:
            ans[a-1] = 0
        else:
            ans[a-1], ans[b-1] = 0, 0
    count = 0
    for v in ans:
        if v == 1:count+=1
    print(count)
if __name__ == "__main__":
    main()