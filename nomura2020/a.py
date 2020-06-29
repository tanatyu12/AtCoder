import sys
input = sys.stdin.readline
def main():
    H1, M1, H2, M2, K = map(int, input().split())
    h = H2 - H1
    m = M2 - M1
    print(max(0, h * 60 + m - K))
if __name__ == "__main__":
    main()