# しゃくとり法
import sys
input = sys.stdin.readline
def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    ans = 0
    for i in range(N):
        right = i + 2
        for left in range(i+1, N):
            while right < N and L[right] < L[i] + L[left]:
                right += 1
            ans += right - (left+1)
            if left == right:right += 1
    print(ans)
if __name__ == "__main__":
    main()