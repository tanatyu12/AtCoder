# DP ver
import sys
input = sys.stdin.readline
from collections import deque
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [1] * (2**N)
    survivors = deque([i for i in range(2**N)])
    survivers_num_per_rounds = []
    survivors_num = 2**N
    while survivors_num >= 2:
        survivers_num_per_rounds.append(survivors_num)
        survivors_num = survivors_num // 2
    current_round = 0
    match_count = 0
    while len(survivors) != 0:
        a, b = survivors.popleft(), survivors.popleft()
        winner, loser = -1, -1
        if A[a] > A[b]:
            winner, loser = a, b
        else:
            winner, loser = b, a
        if len(survivors) > 0:
            survivors.append(winner)
        else:
            ans[winner] = current_round + 1
        ans[loser] = current_round + 1
        match_count += 1
        if match_count * 2 == survivers_num_per_rounds[current_round]:
            current_round += 1
            match_count = 0
    for x in ans:
        print(x)
if __name__ == "__main__":
    main()