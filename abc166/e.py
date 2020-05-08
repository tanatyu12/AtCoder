import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    m = {}
    for i in range(N):
        x = i - A[i]
        if m.get(x) == None:
            m[x] = [1, 0]
        else:
            m[x][0] += 1
    for i in range(N):
        y = i + A[i]
        if m.get(y) != None:
            m[y][1] += m[y][0]
    ans = 0
    for key in m:
        ans += m[key][1]
    print(ans)
if __name__ == "__main__":
    main()