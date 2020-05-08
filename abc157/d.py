import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def dfs(v, seen, overall, connected_components):
    seen[v] = True
    connected_components.add(v)
    for nv in overall[v]:
        if seen[nv] == True:continue
        dfs(nv, seen, overall, connected_components)
def main():
    N, M, K = map(int, input().split())
    overall = {}
    friends = {}
    blocks = {}
    for i in range(N):
        overall[i] = set()
        friends[i] = set()
        blocks[i] = set()
    for _ in range(M):
        a, b = map(int, input().split())
        overall[a-1].add(b-1)
        overall[b-1].add(a-1)
        friends[a-1].add(b-1)
        friends[b-1].add(a-1)
    for _ in range(K):
        c, d = map(int, input().split())
        blocks[c-1].add(d-1)
        blocks[d-1].add(c-1)
    ans = {}
    seen = [False] * N
    for i in range(N):
        if seen[i] == True:continue
        connected_components = set()
        dfs(i, seen, overall, connected_components)
        for v in list(connected_components):
            ans[v] = connected_components - {v}
    for i in range(N):
        print(len(ans[i]-friends[i]-blocks[i]), end=" ")
if __name__ == "__main__":
    main()