import sys
input = sys.stdin.readline
def main():
    N = int(input())
    S = input().rstrip()
    ans = []
    for c in S:
        code = ord(c) + N
        if code > 90:code = 65 + (code-91)
        ans.append(chr(code))
    print("".join(ans))
if __name__ == "__main__":
    main()