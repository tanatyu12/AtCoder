import sys
input = sys.stdin.readline
import math
def main():
    X = int(input())
    ans = 0
    val = 100
    while val < X:
        val += val // 100
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()