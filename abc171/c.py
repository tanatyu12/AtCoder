import sys
input = sys.stdin.readline
import string
def main():
    def f(n):
        if n == -1:return
        a, b = divmod(n, 26)
        ans.append(string.ascii_lowercase[b])
        f(a-1)

    N = int(input())
    ans = []
    f(N-1)
    print("".join(ans[::-1]))
if __name__ == "__main__":
    main()