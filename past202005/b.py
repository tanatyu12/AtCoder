import sys
input = sys.stdin.readline
def main():
    N, M, Q = map(int, input().split())
    correct_answers = [[False for _ in range(M)] for _ in range(N)]
    correct_answer_num = [0] * M
    for _ in range(Q):
        s = input().rstrip().split()
        if len(s) == 2:
            _, n = int(s[0]), int(s[1])
            ans = 0
            for i, mi in enumerate(correct_answers[n-1]):
                if mi == True:
                    ans += (N - correct_answer_num[i])
            print(ans)
        else:
            _, n, m = int(s[0]), int(s[1]), int(s[2])
            correct_answer_num[m-1] += 1
            correct_answers[n-1][m-1] = True
if __name__ == "__main__":
    main()