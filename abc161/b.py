import sys
input = sys.stdin.readline
def main():
    N,M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    th = (1 / (4*M)) * sum(A)
    ans = "Yes"
    for i in range(M):
        if A[i] < th:
            ans = "No"
            break
    print(ans)
if __name__ == "__main__":
    main()