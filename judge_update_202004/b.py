import sys
input = sys.stdin.readline
def main():
    r_list = []
    b_list = []
    N = int(input())
    for _ in range(N):
        x, c = input().split()
        if c == "R":
            r_list.append(int(x))
        else:
            b_list.append(int(x))
    r_list.sort()
    b_list.sort()
    for r in r_list:
        print(r)
    for b in b_list:
        print(b)
if __name__ == "__main__":
    main()