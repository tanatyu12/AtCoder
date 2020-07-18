import sys
input = sys.stdin.readline
from collections import Counter
def main():
    N = int(input())
    cnt_list = []
    for _ in range(N):
        S = input().rstrip()
        cnt_list.append(S)
    cnt_list = Counter(cnt_list)
    keys = {'AC': 0, 'WA': 0, 'TLE': 0, 'RE': 0}
    for k, v in cnt_list.items():
        keys[k] = v
    print('AC', 'x', keys['AC'])
    print('WA', 'x', keys['WA'])
    print('TLE', 'x', keys['TLE'])
    print('RE', 'x', keys['RE'])
if __name__ == "__main__":
    main()