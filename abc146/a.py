import sys
input = sys.stdin.readline
def main():
    S, T = map(str, input().rstrip().split(" "))
    ans = 0
    if "F" in S and "B" in T:
        ans = int(S[0]) + int(T[1]) - 1
    elif "B" in S and "F" in T:
        ans = int(S[1]) + int(T[0]) - 1
    elif "F" in S and "F" in T:
        ans = abs(int(S[0]) - int(T[0]))
    else:
        ans = abs(int(S[1]) - int(T[1]))
    print(ans)
if __name__ == "__main__":
    main()