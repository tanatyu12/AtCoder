import sys
input = sys.stdin.readline
def main():
    card = []
    for _ in range(3):
        card.append(list(map(int, input().split())))
    bingo = [[0 for _ in range(3)] for _ in range(3)]
    N = int(input())
    for _ in range(N):
        b = int(input())
        for i in range(3):
            for j in range(3):
                if card[i][j] == b:bingo[i][j] = 1
    is_bingo = False
    for i in range(3):
        if bingo[i][0] == 1 and bingo[i][1] == 1 and bingo[i][2] == 1:
            is_bingo = True
            break
        if bingo[0][i] == 1 and bingo[1][i] == 1 and bingo[2][i] == 1:
            is_bingo = True
            break
    if bingo[0][0] == 1 and bingo[1][1] == 1 and bingo[2][2] == 1:
        is_bingo = True
    if bingo[0][2] == 1 and bingo[1][1] == 1 and bingo[2][0] == 1:
        is_bingo = True
    if is_bingo:
        print("Yes")
    else:
        print("No")
if __name__ == "__main__":
    main()