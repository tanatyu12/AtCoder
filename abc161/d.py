import sys
input = sys.stdin.readline
from collections import deque
def main():
    K = int(input())
    que = deque(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
    if K <= 9:
        print(que[K-1])
    else:
        K -= 9
        while K >= 0:
            v = que.popleft()
            if v[-1] != "0":
                K -= 1
                v1 = v + str(int(v[-1])-1)
                if K == 0:
                    print(v1)
                    break
                que.append(v1)
            K -= 1
            v2 = v + v[-1]
            if K == 0:
                print(v2)
                break
            que.append(v2)
            if v[-1] != "9":
                K -= 1
                v3 = v + str(int(v[-1])+1)
                if K == 0:
                    print(v3)
                    break
                que.append(v3)
if __name__ == "__main__":
    main()