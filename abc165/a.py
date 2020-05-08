import sys
input = sys.stdin.readline
def main():
    K = int(input())
    A, B = map(int, input().split())
    ans = "NG"
    for v in range(A, B+1):
        if v % K == 0:
            ans = "OK"
            break
    print(ans)
if __name__ == "__main__":
    main()