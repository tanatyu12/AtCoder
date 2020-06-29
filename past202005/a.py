import sys
input = sys.stdin.readline
def main():
    s = input().rstrip()
    t = input().rstrip()
    if s == t:
        print("same")
    elif s.lower() == t.lower():
        print("case-insensitive")
    else:
        print("different")
if __name__ == "__main__":
    main()