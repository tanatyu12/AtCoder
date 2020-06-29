import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    loop_count = min(K, 42)
    for _ in range(loop_count):
        light_range_list = [[0, 0] for _ in range(N)]
        for i, a in enumerate(A):
            start, end = max(0, i-a), min(N, i+a+1)
            light_range_list[i][0] = start
            light_range_list[i][1] = end
        ans = [0] * N
        for light_range in light_range_list:
            start, end = light_range[0], light_range[1]
            ans[start] += 1
            if end < N:ans[end] -= 1
        for i in range(N-1):
            ans[i+1] = ans[i] + ans[i+1]
        A = ans
    print(" ".join(list(map(str, ans))))
if __name__ == "__main__":
    main()