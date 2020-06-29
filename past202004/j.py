import sys
input = sys.stdin.readline
from collections import deque
def main():
    S = input().rstrip()
    S_list = deque([])
    for c in S:
        if c != ")":
            S_list.append(c)
        else:
            s = []
            current = ""
            while current != "(":
                current = S_list.pop()
                if current != "(":
                    s.append(current)
            s = s[::-1] + s
            S_list.extend(s)
    ans = "".join(S_list)
    print(ans)
if __name__ == "__main__":
    main()