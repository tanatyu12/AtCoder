import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = A[-1]
    ans_cnt = 0
    for i in range(N-1)[::-1]:
        if ans_cnt == N-2:
            break
        ans += A[i]
        ans_cnt += 1
        if ans_cnt == N-2:
            break
        ans += A[i]
        ans_cnt += 1
        if ans_cnt == N-2:
            break
    print(ans)
if __name__ == "__main__":
    main()