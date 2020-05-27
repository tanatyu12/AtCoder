import sys
input = sys.stdin.readline
from collections import deque
import string
import copy
def main():
    Q = int(input())
    S = deque([])
    for _ in range(Q):
        query = input().rstrip().split(" ")
        if query[0] == "1":
            C = query[1]
            X = int(query[2])
            if len(S) > 0 and S[-1][0] == C:
                S[-1][1] += X
            else:
                S.append([C, X])
        else:
            D = int(query[1])
            delete = {c: 0 for c in string.ascii_lowercase}
            while D > 0 and len(S) > 0:
                head = S.popleft()
                ori_head = copy.copy(head)
                if head[1] > D:
                    head[1] -= D
                    delete[head[0]] += D
                    S.appendleft(head)
                else:
                    delete[head[0]] += head[1]
                D -= ori_head[1]
            ans = 0
            for k in delete:
                ans += delete[k] ** 2
            print(ans)
if __name__ == "__main__":
    main()