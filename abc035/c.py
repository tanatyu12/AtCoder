import sys
input = sys.stdin.readline
def main():
    N, Q = map(int, input().split())
    table = [0 for i in range(N+2)]
    for _ in range(Q):
        l, r = map(int, input().split())
        table[l] += 1
        table[r+1] -= 1
    for i in range(1, N):
        table[i+1] += table[i]
    print("".join([str(v%2) for v in table[1:N+1]]))
if __name__ == "__main__":
    main()