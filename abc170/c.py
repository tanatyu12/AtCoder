import sys
input = sys.stdin.readline
def main():
    X, N = map(int, input().split())
    p = set(list(map(int, input().split())))
    table = set()
    for i in range(1, 101):
        table.add(i)
    table = table - p
    lis = list(table)
    ans = -1
    diff = 10 ** 9
    for i, a in enumerate(lis):
        if abs(a-X) < diff:
            diff = abs(a-X)
            ans = a
        elif abs(a-X) == diff:
            ans = min(ans, a)
    if abs(X-ans) > abs(X-101):
        ans = 101
    if abs(X-ans) >= abs(X):
        ans = 0
    print(ans)
if __name__ == "__main__":
    main()