import sys
input = sys.stdin.readline
def main():
    Na, Nb = map(int, input().split())
    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    print(len(A&B)/len(A|B))
if __name__ == "__main__":
    main()