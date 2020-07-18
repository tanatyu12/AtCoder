import sys
input = sys.stdin.readline
def main():
    H, W, K = map(int, input().split())
    field = ['' for _ in range(H)]
    for i in range(H):
        field[i] = input().rstrip()
    num_black = 0
    for i in range(H):
        for j in range(W):
            if field[i][j] == '#':
                num_black += 1
    ans = 0
    for bit in range(2**(H+W)):
        current = 'h'
        target_h = []
        target_w = []
        for i in range(H+W):
            if i < H:
                current = 'h'
            else:
                current = 'w'
            if bit & 1<<i:
                ord = i
                if current == 'w':
                    ord = i - H
                if current == 'h':
                    target_h.append(ord)
                else:
                    target_w.append(ord)
        cnt = 0
        for j in range(H):
            for k in range(W):
                if j in target_h or k in target_w:
                    if field[j][k] == '#':
                        cnt += 1
        if num_black - cnt == K:
            ans += 1
    print(ans)
if __name__ == "__main__":
    main()