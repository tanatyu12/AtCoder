# DP ver
import sys
input = sys.stdin.readline
def main():
    X = int(input())
    dp = [0] * (X+1)
    dp[0] = 1
    for base in range(100, X+1):
        can_buy = False
        for fraction in range(6):
            pre_cost = base - (100 + fraction)
            if dp[pre_cost] == 1:
                can_buy = True
                break
        if can_buy:dp[base] = 1
    print(dp[-1])
if __name__ == "__main__":
    main()