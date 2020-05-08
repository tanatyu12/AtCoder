import sys
input = sys.stdin.readline
sys.setrecursionlimit(2147483647)
import itertools

a1, a2, a3 = map(int, input().split())
total = a1 + a2 + a3
ans = 0

def dfs(x, y, z, cnt):
    global a1, a2, a3, total, ans
    if x > a1 or y > a2 or z > a3:return
    if x < y or y < z:return
    if cnt == total:
        ans += 1
        return
    dfs(x+1, y, z, cnt+1)
    dfs(x, y+1, z, cnt+1)
    dfs(x, y, z+1, cnt+1)
def main():
    dfs(0, 0, 0, 0)
    print(ans)
    # perm_list = itertools.permutations(range(1, a1+a2+a3+1))
    # ans = 0
    # for perm in perm_list:
    #     size = max(a1, a2, a3)
    #     a1_list = [None] * size
    #     a2_list = [None] * size
    #     a3_list = [None] * size
    #     for i in range(len(perm)):
    #         if i < a1:
    #             a1_list[i] = perm[i]
    #         elif a1 <= i < a1+a2:
    #             a2_list[i-a1] = perm[i]
    #         else:
    #             a3_list[i-a1-a2] = perm[i]
    #     is_ans = True
    #     for i in range(a1-1):
    #         if a1_list[i] > a1_list[i+1]:
    #             is_ans = False
    #             break
    #     for i in range(a2-1):
    #         if a2_list[i] > a2_list[i+1]:
    #             is_ans = False
    #             break
    #     for i in range(a3-1):
    #         if a3_list[i] > a3_list[i+1]:
    #             is_ans = False
    #             break
    #     for x,y,z in zip(a1_list,a2_list,a3_list):
    #         if x != None and y != None and x > y:
    #             is_ans = False
    #             break
    #         if y != None and z != None and y > z:
    #             is_ans = False
    #             break
    #     if is_ans:ans += 1
    # print(ans)
if __name__ == "__main__":
    main()