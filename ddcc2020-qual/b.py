import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    com_left = [0] * (N+1)
    com_right = [0] * (N+1)
    total = sum(A)
    for i in range(N):
        com_left[i+1] = com_left[i] + A[i]
        com_right[i] = total - com_left[i]
    ans = 2020202020
    for i in range(N):
        diff = abs(com_left[i] - com_right[i])
        ans = min(ans, diff)
    print(ans)
if __name__ == "__main__":
    main()