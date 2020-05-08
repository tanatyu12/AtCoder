import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    minus = 0
    minus_count = 0
    plus_list = []
    for i in range(N):
        diff = A[i] - B[i]
        if diff < 0:
            minus += diff
            minus_count += 1
        else:
            plus_list.append(diff)
    plus_list.sort(reverse=True)
    if minus == 0:
        print(0)
    else:
        ans = 0
        for v in plus_list:
            minus += v
            ans += 1
            if minus >= 0:break
        if minus < 0:
            print(-1)
        else:
            print(ans+minus_count)
if __name__ == "__main__":
    main()