import sys
input = sys.stdin.readline
def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        target = i
        current = 1
        while True:
            target = i * current
            current += 1
            if target > N:
                break
            ans += target
    print(ans)
if __name__ == "__main__":
    main()