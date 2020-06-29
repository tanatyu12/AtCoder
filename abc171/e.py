import sys
input = sys.stdin.readline
def main():
    N = int(input())
    a = list(map(int, input().split()))
    s = a[0]
    for i in range(1, N):
        s ^= a[i]
    ans = [str(x^s) for x in a]
    print(" ".join(ans))
if __name__ == "__main__":
    main()