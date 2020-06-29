import sys
input = sys.stdin.readline
def main():
    N = int(input())
    board = [[] for _ in range(5)]
    is_zero = ["###", "#.#", "#.#", "#.#", "###"]
    is_one = [".#.", "##.", ".#.", ".#.", "###"]
    is_two = ["###", "..#", "###", "#..", "###"]
    is_three = ["###", "..#", "###", "..#", "###"]
    is_four = ["#.#", "#.#", "###", "..#", "..#"]
    is_five = ["###", "#..", "###", "..#", "###"]
    is_six = ["###", "#..", "###", "#.#", "###"]
    is_seven = ["###", "..#", "..#", "..#", "..#"]
    is_eight = ["###", "#.#", "###", "#.#", "###"]
    is_nine = ["###", "#.#", "###", "..#", "###"]
    ans = []
    for i in range(5):
        board[i] = input().rstrip()
    c = ""
    for j in range(4, 4*N+1, 4):
        num = []
        for i in range(5):
            num.append(board[i][j-3:j])
        if num == is_zero:
            c = "0"
        elif num == is_one:
            c = "1"
        elif num == is_two:
            c = "2"
        elif num == is_three:
            c = "3"
        elif num == is_four:
            c = "4"
        elif num == is_five:
            c = "5"
        elif num == is_six:
            c = "6"
        elif num == is_seven:
            c = "7"
        elif num == is_eight:
            c = "8"
        elif num == is_nine:
            c = "9"
        ans.append(c)
    print("".join(ans))
if __name__ == "__main__":
    main()