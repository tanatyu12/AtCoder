import sys
input = sys.stdin.readline
def main():
    N, K = map(int, input().split())
    x = list(map(int, input().split()))
    neg_dists = []
    pos_dists = []
    exists_zero = False
    for xi in x:
        if xi < 0:
            neg_dists.append(abs(xi))
        elif xi > 0:
            pos_dists.append(abs(xi))
        else:
            exists_zero = True
    neg_dists.sort()
    pos_dists.sort()
    ans = 10 ** 9
    count = K - int(exists_zero)
    for i in range(count):
        d = 0
        if i >= len(neg_dists):continue
        d += neg_dists[i]
        if len(pos_dists) == 0 or count-2-i >= len(pos_dists):continue
        d += pos_dists[count-2-i] + neg_dists[i]
        ans = min(ans, d)
    for i in range(count):
        d = 0
        if i >= len(pos_dists):continue
        d += pos_dists[i]
        if len(neg_dists) == 0 or count-2-i >= len(neg_dists):continue
        d += neg_dists[count-2-i] + pos_dists[i]
        ans = min(ans, d)
    if len(neg_dists) > 0 and count <= len(neg_dists):ans = min(ans, neg_dists[count-1])
    if len(pos_dists) > 0 and count <= len(pos_dists):ans = min(ans, pos_dists[count-1])
    if exists_zero and len(neg_dists) == 0 and len(pos_dists) == 0:ans = 0
    print(ans)
            
if __name__ == "__main__":
    main()