import sys
input = sys.stdin.readline
def main():
    D = int(input())
    c = list(map(int, input().split()))
    s = []
    for _ in range(D):
        si = list(map(int, input().split()))
        s.append(si)
    score = 0
    last_list = [0] * 26
    for i in range(D):
        t = int(input())
        last_list[t-1] = i+1
        current = s[i][t-1]
        minus = 0
        for j in range(26):
            if t - 1 != j:
                minus += c[j] * (i+1-last_list[j])
        current -= minus
        score += current
        print(score)
if __name__ == "__main__":
    main()