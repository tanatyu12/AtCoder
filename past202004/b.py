import sys
input = sys.stdin.readline
from collections import Counter
def main():
    S = input().rstrip()
    vote = Counter(S)
    ans = vote.most_common()[0][0]
    print(ans)
if __name__ == "__main__":
    main()