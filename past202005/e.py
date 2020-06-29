import sys
input = sys.stdin.readline
def main():
    N, M, Q = map(int, input().split())
    graph = {}
    for i in range(N):
        graph[i] = set()
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].add(v-1)
        graph[v-1].add(u-1)
    c = list(map(int, input().split()))
    for _ in range(Q):
        s = input().rstrip().split()
        if len(s) == 2:
            _, x = int(s[0]), int(s[1])
            col_x = c[x-1]
            print(col_x)
            for v in graph[x-1]:
                c[v] = col_x
        else:
            _, x, y = int(s[0]), int(s[1]), int(s[2])
            print(c[x-1])
            c[x-1] = y
if __name__ == "__main__":
    main()