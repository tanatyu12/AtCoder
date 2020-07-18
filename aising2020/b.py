import sys
input = sys.stdin.readline
def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i, ai in enumerate(a):
        if (i+1) % 2 == 1 and ai % 2 == 1:
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()