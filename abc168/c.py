import sys
input = sys.stdin.readline
import math
def main():
    A, B, H, M = map(int, input().split())
    radh = (H*60+M)/720 * 2*math.pi
    radm = M/60 * 2*math.pi
    hx, hy = A*math.cos(radh), A*math.sin(radh)
    mx, my = B*math.cos(radm), B*math.sin(radm)
    ans = math.sqrt((hx-mx)**2 + (hy-my)**2)
    print(ans)
if __name__ == "__main__":
    main()