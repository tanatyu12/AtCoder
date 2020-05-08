import sys
input = sys.stdin.readline
def main():
    X = int(input())
    ans = [0] * 2

    for A in range(-1000, 1001):
        for B in range(-1000, 1001):
            if pow(A, 5) - pow(B, 5) == X:
                ans[0], ans[1] = A, B
                break
    print(ans[0], ans[1])
if __name__ == "__main__":
    main()