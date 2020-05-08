import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def dfs(v, i):
    if i == 0:
        print(v)
        return
    for c in ["a","b","c"]:
        dfs(v+c,i-1)
def main():
    N = int(input())
    dfs("",N)
if __name__ == "__main__":
    main()