import sys
input = sys.stdin.readline
from itertools import permutations
def main():
    t = [int(input()) for _ in range(5)]
    tp = permutations(t)
    ans = 1000*5
    for p in tp:
        total = 0
        for i,pi in enumerate(p):
            if i == 4:
                total += pi
                break
            a,b = divmod(pi,10)
            if b == 0:
                total += a*10
            else:
                total += a*10+10
        ans = min(ans,total)
    print(ans)
if __name__ == "__main__":
    main()