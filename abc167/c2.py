# bit full search
import sys
input = sys.stdin.readline
def main():
    N, M, X = map(int, input().split())
    ans = 10 ** 9
    C_list = []
    A_list = []
    for _ in range(N):
        CA = list(map(int, input().split()))
        C_list.append(CA[0])
        A_list.append(CA[1:])
    for bit in range(2**N):
        cost = 0
        A = [0 for _ in range(M)]
        clear = True
        for i in range(N):
            if bit & 1<<i:
                cost += C_list[i]
                for j in range(M):
                    A[j] += A_list[i][j]
        for k in range(M):
            clear = clear and (A[k] >= X)
        if clear:
            ans = min(ans, cost)
    if ans == 10 ** 9:
        ans = -1
    print(ans)
if __name__ == "__main__":
    main()