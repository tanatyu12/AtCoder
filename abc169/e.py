import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A_list = []
    B_list = []
    for _ in range(N):
        A, B = map(int, input().split())
        A_list.append(A)
        B_list.append(B)
    print(A_list)
    print(B_list)
if __name__ == "__main__":
    main()