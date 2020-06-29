import sys
input = sys.stdin.readline
import math
from decimal import Decimal
def main():
    inp = input().split()
    a = int(inp[0])
    b = Decimal(inp[1])
    ans = a * b
    ans = math.floor(ans)
    print(ans)
if __name__ == "__main__":
    main()