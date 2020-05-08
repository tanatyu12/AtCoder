import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    a = set()
    for _ in range(K):
        _ = int(input())
        A = list(map(int, input().split()))
        for Ai in A:
            a.add(Ai)
    print(N-len(a))
if __name__ == "__main__":
    main()