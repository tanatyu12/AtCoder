import sys
input = sys.stdin.readline
def should_write(i, j, T):
    if T[i][j] == "#" and (T[i+1][j-1] == "X" or T[i+1][j] == "X" or T[i+1][j+1] == "X"):
        return True
    else:
        return False
def main():
    N = int(input())
    T = []
    for _ in range(N):
        ti = list(input().rstrip())
        T.append(ti)
    for i in range(N-1)[::-1]:
        for j in range(1, 2*N-2):
            if should_write(i, j, T):T[i][j] = "X"
    for i in range(N):
        print("".join(T[i]))
if __name__ == "__main__":
    main()