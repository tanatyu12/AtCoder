import sys
input = sys.stdin.readline
def main():
    R, G, B, N = map(int, input().split())
    r_count = N // R
    g_count = N // G
    ans = 0
    for i in range(r_count+1):
        for j in range(g_count+1):
            k = N - R * i - G * j
            if k % B == 0 and k >= 0:
                ans += 1
    print(ans)
if __name__ == "__main__":
    main()