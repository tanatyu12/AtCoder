import sys
input = sys.stdin.readline
import string
import itertools
def main():
    S = input().rstrip()
    T = list(string.ascii_lowercase) + ['.']
    T_len = min(len(S), 3)
    T_list = []
    for c in T:
        T_list.append(c)
    if T_len > 1:
        for c1 in T:
            for c2 in T:
                T_list.append([c1, c2])
    if T_len > 2:
        for c1 in T:
            for c2 in T:
                for c3 in T:
                    T_list.append([c1, c2, c3])
    ans = 0
    for t in T_list:
        for i in range(len(S)-len(t)+1):
            matched = True
            cnt = 0
            for j in range(len(t)):
                matched = matched and (S[i+cnt] == t[j] or t[j] == ".")
                cnt += 1
            if matched:
                ans += 1
                break
    print(ans)
if __name__ == "__main__":
    main()