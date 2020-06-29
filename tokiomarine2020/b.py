import sys
input = sys.stdin.readline
def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())
    dist = abs(A-B)
    ans = V * T - W * T
    if ans >= dist:
        print("YES")
    else:
        print("NO")
if __name__ == "__main__":
    main()