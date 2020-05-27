import sys
input = sys.stdin.readline
import heapq
def main():
    N = int(input())
    tasks = {i: [] for i in range(1, N+1)}
    for _ in range(N):
        A, B = map(int, input().split())
        tasks[A].append(-1 * B)
    current = []
    ans = 0
    for i in range(1, N+1):
        for v in tasks[i]:
            heapq.heappush(current, v)
        ans += -1 * heapq.heappop(current)
        print(ans)
if __name__ == "__main__":
    main()