# 累積和
import sys
input = sys.stdin.readline
import bisect
def main():
    N = int(input())
    L = list(map(int, input().split()))
    L.sort()
    MAX = 2000
    C = [0] * MAX
    S = [0] * (MAX+1)
    for val in L:
        C[val] += 1
    for i in range(MAX):
        S[i+1] = C[i] + S[i]
    ans = 0
    for i in range(N):
        for j in range(N):
            if i == j:continue
            left = abs(L[i]-L[j])+1
            right = L[i]+L[j]
            ans += S[right]-S[left]
            if left <= L[i] < right:ans -= 1
            if left <= L[j] < right:ans -= 1
    print(ans//6)
if __name__ == "__main__":
    main()