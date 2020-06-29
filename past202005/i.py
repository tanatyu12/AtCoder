import sys
input = sys.stdin.readline
def swap_rows(rows, A, B):
    tmp = rows[A-1]
    rows[A-1] = rows[B-1]
    rows[B-1] = tmp
def swap_cols(cols, A, B):
    tmp = cols[A-1]
    cols[A-1] = cols[B-1]
    cols[B-1] = tmp
def main():
    N = int(input())
    Q = int(input())
    rows = [i for i in range(N)]
    cols = [i for i in range(N)]
    is_tranpose = False
    for _ in range(Q):
        q = input().rstrip().split()
        if len(q) == 1:
            code = int(q[0])
        else:
            code, A, B = int(q[0]), int(q[1]), int(q[2])
        if code == 1:
            if is_tranpose:
                swap_cols(cols, A, B)
            else:
                swap_rows(rows, A, B)
        elif code == 2:
            if is_tranpose:
                swap_rows(rows, A, B)
            else:
                swap_cols(cols, A, B)
        elif code == 3:
            is_tranpose = not is_tranpose
        elif code == 4:
            if is_tranpose:
                row = rows[B-1]
                col = cols[A-1]
            else:
                row = rows[A-1]
                col = cols[B-1]
            ans = N * row + col
            print(ans)
if __name__ == "__main__":
    main()