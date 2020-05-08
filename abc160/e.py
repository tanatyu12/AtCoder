import sys
input = sys.stdin.readline
def main():
    X, Y, A, B, C = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort(reverse=True)
    q = list(map(int, input().split()))
    q.sort(reverse=True)
    r = list(map(int, input().split()))
    r.sort(reverse=True)
    target = p[:X] + q[:Y] + r
    target.sort(reverse=True)
    ans = sum(target[:X+Y])
    print(ans)
if __name__ == "__main__":
    main()