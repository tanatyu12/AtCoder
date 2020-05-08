import sys
input = sys.stdin.readline
import math
def main():
    A, B, N = map(int, input().split())
    x = min(N, B)
    ans = math.floor(A*x/B) - A * math.floor(x/B)
    print(ans)
if __name__ == "__main__":
    main()