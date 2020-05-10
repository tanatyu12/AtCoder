import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    visited = {i:0 for i in range(N)}
    visited[0] = 1
    count = 0
    pre_count = 0
    cicle_idx = 0
    is_cicle = False
    idx = 0
    ans = -1
    while not is_cicle:
        count += 1
        if count == K:
            ans = A[idx]
        idx = A[idx]-1
        if visited[idx] == 1:
            visited[idx] = 2
            is_cicle = True
            cicle_idx = idx
            break
        visited[idx] = 1
    if ans == -1:
        cicle = []
        will_push = False
        while True:
            idx = A[idx]-1
            if idx == cicle_idx:will_push = True
            if len(cicle) > 0 and visited[idx] == 2:break
            if will_push:
                cicle.append(idx)
        pre_count = count - len(cicle)
        ans_idx = (K - pre_count) % len(cicle)
        print(cicle[ans_idx]+1)
    else:
        print(ans)
if __name__ == "__main__":
    main()