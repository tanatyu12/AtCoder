import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n
    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    def same(self, x, y):
        if self.root(x) == self.root(y):
            return True
        return False
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return True

def main():
    N, Q = map(int, input().split())
    unionfind = UnionFind(N)
    for _ in range(Q):
        p, a, b = map(int, input().split())
        if p == 0:
            unionfind.unite(a-1, b-1)
        else:
            if unionfind.same(a-1, b-1):
                print("Yes")
            else:
                print("No")
if __name__ == "__main__":
    main()