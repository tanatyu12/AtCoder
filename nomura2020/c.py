import sys
input = sys.stdin.readline
def main():
    N = int(input())
    A = list(map(int, input().split()))
    node_count = [0] * (N+1)
    for i, a in enumerate(A[::-1]):
        if i == 0:
            node_count[N] = a
            continue
        node_count[N-i] = node_count[N-i+1] + a
    can_build = True
    for i, a in enumerate(A):
        if i == 0:
            if N > 0 and a > 0:
                can_build = False
                break
            if N == 0 and a > 1:
                can_build = False
                break
            node_count[0] = min(node_count[0], 1)
            continue
        if (i < N and a >= node_count[i-1]*2) or (i == N and a > node_count[i-1]*2):
            can_build = False
            break
        node_count[i] = min(node_count[i], node_count[i-1]*2-A[i-1]*2)
    if can_build:
        ans = sum(node_count)
    else:
        ans = -1
    print(ans)
if __name__ == "__main__":
    main()