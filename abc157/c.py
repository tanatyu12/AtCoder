import sys
input = sys.stdin.readline
def main():
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        s, c = input().rstrip("\r\n").split()
        conditions.append((int(s)-1, c))
    ans = -1
    if N > 1:
        start = 10**(N-1)
    else:
        start = 0
    for i in range(start, 10**N):
        i_str = str(i)
        matched = True
        for s, c in conditions:
            if len(i_str) > s:
                matched = matched and i_str[s] == c
            else:
                matched = False
        if matched:
            ans = i
            break
    print(ans)
if __name__ == "__main__":
    main()