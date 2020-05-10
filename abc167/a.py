import sys
input = sys.stdin.readline
def main():
    S = input().rstrip("\r\n")
    T = input().rstrip("\r\n")
    if S == T[:-1] and len(S) + 1 == len(T):
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()