import sys
input = sys.stdin.readline
def main():
    K = int(input())
    S = input().rstrip()
    if len(S) <= K:
        print(S)
    else:
        print(S[:K]+"...")
if __name__ == "__main__":
    main()