import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    A = [input().rstrip() for _ in range(N)]
    indices = [[] for _ in range(11)]
    for i in range(N):
        for j in range(M):
            v = A[i][j]
            if v == "S":
                v = 0
            elif v == "G":
                v = 10
            indices[int(v)].append((i, j))
    memo = [[0 for _ in range(M)] for _ in range(N)]

    def f(h, w, next_num):
        if next_num == 11:return 0
        if memo[h][w] > 0:return memo[h][w]
        res = 10 ** 9
        for nh, nw in indices[next_num]:
            cost = abs(h - nh) + abs(w - nw)
            res = min(res, f(nh, nw, next_num+1) + cost)
        memo[h][w] = res
        return res
    
    exists_path = True
    for i in range(11):
        if len(indices[i]) == 0:
            exists_path = False
            break
    if not exists_path:
        print(-1)
    else:
        print(f(indices[0][0][0], indices[0][0][1], 1))
if __name__ == "__main__":
    main()