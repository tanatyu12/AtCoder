import sys
input = sys.stdin.readline
def main():
    N = int(input())
    max_x = 100
    max_y = 100
    max_z = 100
    ans = [0] * N
    for x in range(1, max_x+1):
        for y in range(1, max_y+1):
            for z in range(1, max_z+1):
                a = (x+y+z)**2 - x*y - y*z - z*x
                if 1 <= a <= N:
                    ans[a-1] += 1
    for ni in ans:
        print(ni)
if __name__ == "__main__":
    main()