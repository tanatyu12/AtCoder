# dp array
import sys
input = sys.stdin.readline
def chmax(dp, i, k, b):
    if dp[i][k] < b:
        dp[i][k] = b
        return True
    return False
def main():
    N = int(input())
    activities = []
    for _ in range(N):
        activities.append(list(map(int, input().split())))
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0] = activities[0]
    for i in range(1, N):
        for j in range(3):
            for k in range(3):
                if j != k:chmax(dp, i, k, dp[i-1][j]+activities[i][k])
    print(max(dp[-1][0], dp[-1][1], dp[-1][2]))
if __name__ == "__main__":
    main()