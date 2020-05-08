import sys
input = sys.stdin.readline
def main():
    _, A, B, C, D = map(int, input().split())
    S = input().rstrip("\r\n")
    ans = "Yes"
    for i in range(A-1,C-1):
        if S[i] == "#" and S[i+1] == "#":
            ans = "No"
            break
    for i in range(B-1,D-1):
        if S[i] == "#" and S[i+1] == "#":
            ans = "No"
            break
    if C < D or ans == "No":
        print(ans)
    else:
        ans = "No"
        for i in range(B-1, D):
            if S[i-1] == "." and S[i] == "." and S[i+1] == ".":
                ans = "Yes"
        print(ans)
if __name__ == "__main__":
    main()