import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
def main():
    x,y,z = map(int, input().split())
    tmp = x
    x = y
    y = tmp
    tmp = x
    x = z
    z = tmp
    print(x, y, z)
if __name__ == "__main__":
    main()