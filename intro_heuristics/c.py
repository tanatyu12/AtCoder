import sys
input = sys.stdin.readline
def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    for _ in range(D):
        si = list(map(int, input().split()))
        s.append(si)
    t_list = []
    last_list = [[0, 0] for _ in range(26)]
    scores = [0] * D
    score = 0
    for i in range(D):
        t = int(input())
        t_list.append(t)
        last_list[t-1][1] = last_list[t-1][0]
        last_list[t-1][0] = i+1

        current = s[i][t-1]
        minus = 0
        for j in range(26):
            if t - 1 != j:
                minus += c[j] * (i+1-last_list[j][0])
        current -= minus
        score += current
        scores[i] = score
        print(scores)
    M = int(input())
    for _ in range(M):
        d, q = map(int, input().split())
        old = t_list[d-1]
if __name__ == "__main__":
    main()