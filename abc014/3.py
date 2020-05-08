import sys
input = sys.stdin.readline
def main():
    n = int(input())
    table = [0 for i in range(10**6+2)]
    for _ in range(n):
        a, b = map(int, input().split())
        table[a] += 1
        table[b+1] -= 1
    for i in range(len(table)-1):
        table[i+1] += table[i]
    print(max(table))
if __name__ == "__main__":
    main()